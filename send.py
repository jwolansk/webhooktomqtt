#!/usr/bin/env python
# -*- coding: utf-8 -*-

# add above 3.5
import web
import sys
import os
reload(sys)

from web.wsgiserver import CherryPyWSGIServer

import paho.mqtt.client as mqtt

ip = str(os.environ['IPADDRESS'])
port = int(os.environ['PORT'])

if port is None:
    port = 1883

sys.setdefaultencoding('utf8')

urls = (
    '/send?', 'send',
)

class send(object):
    def GET(self):
        data = web.input()
        client = mqtt.Client()
        client.connect(ip, port, 60)
        return client.publish(data.topic, data.msg, 0, int(data.retain))


class MyApplication(web.application):
    def run(self, port=80, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

if __name__ == "__main__":
    app = MyApplication(urls, globals())
    app.run()