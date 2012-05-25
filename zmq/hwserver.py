#   ZMQ Hello world Server in python
#   benjaminfjones@gmail.com
#
#   Hello World server in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#
import zmq
import time

context = zmq.Context()

#  Socket to send replies

socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    print "Received msg ... [", message, "]"

    time.sleep(1) # do some important work

    print 'Sending reply [World] ...'
    socket.send("World")
