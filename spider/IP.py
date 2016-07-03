
import random

def ip_serach(ip_location,ip_mb):
    f = open('xy.txt', 'r')

    for line in f.readlines():
        if not len(line):
            continue
        line = line.strip()  
        line=line.split(' ')
        if ip_location in line[2] and ip_mb in line[3]:
            mm=int(line[0].split('.'))
            mm2=int(line[1].split('.'))
            ip=mm[0]+'.'+mm[1]+'.'+mm[2]+'.'+random.randint(mm[3],mm2[3])
            print ip
            break
        else:
            continue
         

