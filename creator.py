#!/usr/bin/python
# Simple python script for capturing webcam images from a raspberry PI
# Produces image files with the currrent sytem time as the file name
import os
import datetime
import requests
from subprocess import call, check_output

RPI_CONFIGS = [
    {
        'savename': 'rpi1',
        'resolution': '1392x768'
    },
    {
        'savename': 'rpi2',
        'resolution': '544x288'
    }
]
RPI_CONFIG = RPI_CONFIGS[0]
NSQ_HOST = 'http://192.168.1.14:4151'
MAX_DISK_SIZE = 12000000000  # black friday sales blessed me with an ample 16gb
                             # micro sd for each of these computing beasts

host = '1' #check_output("ip addr show wlan0  | grep inet", shell=True).split('inet')[1].replace(' ', '').split('/24')[0] + ':9001/'

def publish_on_new_image(image_name):
        topic = 'new_image'
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        requests.post('%s/put?topic=%s' % (NSQ_HOST, topic), data=image_name, headers=headers)

def get_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def main():
    """ TODO - figure out avg filesize and periodically check for memory limit
    if get_size('rendered/') > MAX_DISK_SIZE:
        call(['killall watch'], shell=True)"""

    filestamp = (
        datetime.datetime.now()
            .strftime("%Y-%m-%d %H:%M:%S")
            .replace(',', '')
            .replace(' ','-') + '.jpg'
    )
    filename = ("%s_%s") % (RPI_CONFIG['savename'], filestamp)
    filepath = "rendered/" + filename
    call(
        # rpi command should be fswebcam -d /dev/video0 -r %s --save %s
        ['echo %s %s' % (RPI_CONFIG['resolution'], filepath)],
        shell=True
    )
    publish_on_new_image(host + filename)

if __name__ == '__main__':
    while True:
        main()
