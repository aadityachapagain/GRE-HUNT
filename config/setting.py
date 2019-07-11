from os.path import abspath, dirname, join
import os

# paths for various project folder
ROOT_DIR = dirname(dirname(abspath(__file__)))
DATA_DIR = join(ROOT_DIR, 'data')

ICON_PATH = join(DATA_DIR, 'icon.png')

MUSIC_PATH = join(DATA_DIR,'alert.ogg')

APP_NAME = 'GRE-HUNT'