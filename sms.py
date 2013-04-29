import zmq
from flask import Flask, request#, redirect
import twilio.twiml
 
app = Flask(__name__)
address = "tcp://localhost:56890"
  
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    #text = None
    #print request.values
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    
    socket.connect(address)
    socket.send('from: ' + str(request.form.get('From', '')) + '\nmessage: ' + str(request.form.get('Body', '')), zmq.NOBLOCK)
    resp = twilio.twiml.Response()
    #resp.sms("Hello, Mobile Monkey")

    return str(resp)
                
if __name__ == "__main__":
    app.run(debug=True)
