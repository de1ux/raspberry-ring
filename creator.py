# Simple python script for capturing webcam images from a raspberry PI
# Produces image files with the currrent sytem time as the file name
import os
import datetime
import requests
from subprocess import call

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
NSQ_HOST = 'http://127.0.0.1:4151'


def main():

    # publishes a new image to the new_images topic
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

    if get_size('rendered/') > :
        call(['killall watch'], shell=True)

    filestamp = (
        datetime.datetime.now()
            .strftime("%Y-%m-%d %H:%M:%S")
            .replace(',', '')
            .replace(' ','-') + '.jpg'
    )
    filepath = ("rendered/%s_%s") % (RPI_CONFIG['savename'], filestamp)
    call(
        # rpi command should be fswebcam -d /dev/video0 -r %s --save %s
        ['echo "%s %s"' % (RPI_CONFIG['resolution'], filepath)],
        shell=True
    )
    publish_on_new_image(filepath)

if __name__ == '__main__':
    main()
