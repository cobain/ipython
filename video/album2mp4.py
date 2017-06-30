#!/usr/bin/env python
from __future__ import print_function
from glob import glob
import argparse
import os
import subprocess
from PIL import Image
import platform

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

is_windows = platform.system() == 'Windows'


def which(program):
    if is_windows:
        program += '.exe'

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


executable = which('ffmpeg')
if executable is None:
    executable = which('avconv')
    if executable is None:
        quit("Please install ffmpeg or avconv")


def create_cover(cover, folder):
    """
    :return the cover art centered
    """
    cover_im = Image.open(cover)
    cover_im.thumbnail((1920, 1080), Image.ANTIALIAS)
    out_fname = folder + 'cover_temp.png'

    cover_out = Image.new('RGB', (1920, 1080))

    img_w, img_h = cover_im.size
    bg_w, bg_h = cover_out.size

    offset = ((bg_w - img_w) / 2, (bg_h - img_h) / 2)
    cover_out.paste(cover_im, offset)
    print("Generated cover:\t", out_fname)
    cover_out.save(out_fname)

    return out_fname


def do_process(folder, _cover, output, add_title, font, verbose):
    print("Folder:\t", folder)
    print("Cover:\t", _cover)
    print("Output:\t", output, "\n")
    cover = create_cover(_cover, folder)
    temps = []
    descr = []
    time = 0
    for song in sorted(glob(folder + '*.mp3')):
        out_name = song.split('.mp3')[0] + '.mp4'
        mp3info = EasyID3(song)
        mp3 = MP3(song)
        print(out_name)
        temps.append(out_name)
        descr.append("{0:0>2}:{1:0>2} - {2}".format(int(time) / 60, int(time) % 60, mp3info['title'][0]))
        args = [executable,
                '-loop', '1',
                '-y',
                '-i', cover,
                '-i', song
                ]
        if add_title:
            args += [
                '-vf',
                'drawtext=fontfile={}:text={}:fontcolor=white:fontsize=96:box=1:boxcolor=black@0.5:boxborderw=10:x=(w-tw)/2:y=(h/PHI)+th'.format(
                    font, "{}".format(mp3info['title'][0])
                )]
        args += [
            '-c:v', 'libx264',
            '-c:a', 'copy',
            '-b:a', '320k',
            '-shortest',
            '-r', '5', out_name]
        if verbose:
            print(" ".join(args))
        convert_out = subprocess.check_output(args, stderr=subprocess.STDOUT)
        if verbose:
            print(convert_out)
        time += mp3.info.length
    filelisttxt = 'filelist.txt'
    with open(filelisttxt, 'w') as file_list:
        for line in temps:
            file_list.write("file '{}'\n".format(line))
    out = subprocess.check_output(
        [executable, '-y', '-f', 'concat', '-safe', '0', '-i', filelisttxt, '-c', 'copy', output],
        stderr=subprocess.STDOUT)
    os.remove(filelisttxt)
    os.remove(cover)
    for t in temps:
        os.remove(t)
    if verbose:
        print(out)
    with open(output + '.txt', 'w') as descr_file:
        descr_file.write("{}\n".format(os.path.split(folder)[-2]))
        for line in descr:
            descr_file.write(line + os.linesep)
        descr_file.write("\nGenerated with https://github.com/jonnoftw/album2mp4")


if __name__ == "__main__":
    # folder is $1
    # cover art is $2
    cwd = os.getcwd()

    parser = argparse.ArgumentParser(
        description='Turn a folder of mp3 files into a single video suitable for youtube upload')
    parser.add_argument('-f', '--folder', metavar='folder', help='The folder containing the mp3 files', required=True,
                        default=cwd)
    parser.add_argument('-o', '--output', metavar='output', help='The name of the output file',
                        default=os.path.split(os.getcwd())[-1] + '.mp4')
    parser.add_argument('-c', '--cover', metavar='cover', help='Location of the cover art', default=cwd + '/cover.jpg')
    parser.add_argument('-s', '--song-title', help='Add the song title to the video', action='store_true')
    parser.add_argument('-p', '--font-path', metavar='font_path', help='Path to font file',
                        default='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
                        required=is_windows)
    parser.add_argument('-v', '--verbose', help='Provide verbose output', action='store_true')
    args = parser.parse_args()

    music_folder = args.folder
    if music_folder[-1] != os.path.sep:
        music_folder += os.path.sep
    cover = args.cover
    output = args.output
    add_title = args.song_title
    font = args.font_path
    verbose = args.verbose
    print("Converting folder of mp3 to mp4")
    from datetime import datetime

    startTime = datetime.now()
    do_process(music_folder, cover, output, add_title, font, verbose)

    print("Finished in", datetime.now() - startTime)
    print("Output in file:", output)
