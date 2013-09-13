#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer

port = 8000

handler = SimpleHTTPServer.SimpleHTTPRequestHandler
server = SocketServer.TCPServer(('', port), handler)

print('Listening on http://localhost:{}/'.format(port))
server.serve_forever()
