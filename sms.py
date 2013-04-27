from flask import Flask, request, redirect
import twilio.twiml
import re
 
app = Flask(__name__)
  
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    #print request.values
    text = request.values.get('Body',None)
    if text:
        print text
        if re.search('mov', text, flags=re.IGNORECASE):
            print "mooooooove along!"
    resp = twilio.twiml.Response()
    #resp.sms("Hello, Mobile Monkey")
    print "test"
    return str(resp)
                
if __name__ == "__main__":
    app.run(debug=True)
