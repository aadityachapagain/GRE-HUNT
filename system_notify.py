# python packages
import sys
import os
import datetime
import time
import json
import gi

# project packages
from config.setting import ICON_PATH, MUSIC_PATH, APP_NAME, APP_DESC

gi.require_version('Notify', '0.7')
from gi.repository import Notify
gi.require_version('GdkPixbuf', '2.0')
from gi.repository import GdkPixbuf


def playbeep():
    os.system(f'paplay {MUSIC_PATH}')


def showNotification(title, body, image):
    notification = Notify.Notification.new(
        title,
        body
    )
    notification.set_icon_from_pixbuf(image)
    notification.set_image_from_pixbuf(image)
    notification.show()
    playbeep()

def main():
    now = datetime.datetime.now()
    Notify.init('never kill your time')
    image = GdkPixbuf.Pixbuf.new_from_file(f'{ICON_PATH}')
    for docs in get_random_record(1):
        showNotification(APP_NAME, APP_DESC, image)

if __name__ == '__main__':
        main()
