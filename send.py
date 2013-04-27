import zmq
import sys
port = "56890"
if len(sys.argv) >1:
    port = sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect('tcp://localhost:%s' % port)
socket.send('thigh')
