import nsq
from subprocess import call



def handler(message):
    # message can look like 192.168.1.101:9001/rpi1_2015-01-25-16:36:59.jpg
    host = message.body.split("_")
    node_name = host[0].split("/")[1]
    filename = host[1]
    call(
        # rpi command should be fswebcam -d /dev/video0 -r %s --save %s
        ['wget -O %s/%s http://%s' % (node_name, filename, message.body)],
        shell=True
    )
    return True

r = nsq.Reader(message_handler=handler,
        lookupd_http_addresses=['http://127.0.0.1:4161'],
        topic='new_image', channel='consumer1', lookupd_poll_interval=15)
nsq.run()