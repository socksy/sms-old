import zmq
from flask import Flask, request, redirect
import twilio.twiml
import re
 
app = Flask(__name__)
address = "tcp://localhost:56890"
  
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    #print request.values
    text = request.values.get('Body',None)
    if text:
        context = zmq.Context()
        socket = context.socket(zmq.PAIR)
        socket.connect(address)
        socket.send(text)
    resp = twilio.twiml.Response()
    #resp.sms("Hello, Mobile Monkey")
    return str(resp)
                
if __name__ == "__main__":
    app.run(debug=True)
