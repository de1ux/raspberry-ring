import nsq

def handler(message):
    print ("Got message %s" % message.body)
    return True

r = nsq.Reader(message_handler=handler,
        lookupd_http_addresses=['http://127.0.0.1:4161'],
        topic='new_image', channel='consumer1', lookupd_poll_interval=15)
nsq.run()