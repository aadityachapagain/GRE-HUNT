import sys
import os
import datetime
import time
import json
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
gi.require_version('GdkPixbuf', '2.0')
from gi.repository import GdkPixbuf


def playbeep():
    os.system('paplay /opt/never_kill_your_time/Xylo.ogg')


def timenow():
    now = datetime.datetime.now()
    time = now.strftime('%H:%M')
    return time


def showNotification(title, body, image):
    notification = Notify.Notification.new(
        title,
        body
    )
    notification.set_icon_from_pixbuf(image)
    notification.set_image_from_pixbuf(image)
    notification.show()
    playbeep()

data = None
with open('/opt/never_kill_your_time/routine.json') as f:
    data = json.loads(f.read())


def main():
    now = datetime.datetime.now()
    Notify.init('never kill your time')
    image = GdkPixbuf.Pixbuf.new_from_file(
        '/opt/never_kill_your_time/notification.png')

    while True:
        for routine in data:
            if routine['time'] == timenow():
                showNotification(routine['title'], routine['body'], image)

        time.sleep(60)


def add(x, y, z):
    info = {
        'time': x,
        'title': y,
        'body': z
    }
    data.append(info)
    with open('/opt/never_kill_your_time/routine.json', 'w') as outfile:
        json.dump(data, outfile)


def update(x, y, z):
    for routine in data:
        if routine['time'] == x:
            routine['title'] = y
            routine['body'] = z
    with open('/opt/never_kill_your_time/routine.json', 'w') as outfile:
        json.dump(data, outfile)


def delete(x):
    for routine_i in data:
        if routine_i['time'] == x:
            data.remove(routine_i)
    with open('/opt/never_kill_your_time/routine.json', 'w') as outfile:
        json.dump(data, outfile)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'add':
            add(sys.argv[2], sys.argv[3], sys.argv[4])
        elif sys.argv[1] == 'update':
            update(sys.argv[2], sys.argv[3], sys.argv[4])
        elif sys.argv[1] == 'delete':
            delete(sys.argv[2])
    else:
        main()