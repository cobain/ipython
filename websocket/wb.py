from socketIO_client import SocketIO
import json
hosts = 'xxxx'
port = 1234


def on_connect(*args):
    print('connect')
    print(args)


def on_disconnect():
    print('disconnect')


def on_reconnect():
    print('reconnect')


def on_aaa_response(*args):
    print('on_aaa_response', args)


def on_message(*args):
    print(args)

data = open('data.json')
jsonObj = json.load(data)
machine_ids = []
for obj in jsonObj['content']:
    machine_ids.append(obj['machineId'])
print(len(machine_ids))

while True:
    for mid in machine_ids:

        socketIO = SocketIO(hosts, port, params={'machineId': mid})
        socketIO.on('connect', on_connect)
        socketIO.on('disconnect', on_disconnect)
        socketIO.on('reconnect', on_reconnect)
        socketIO.on('message', on_message)
        socketIO.wait(0.01)
