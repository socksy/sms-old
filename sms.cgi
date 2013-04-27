#!/cs/home/bjl7/Envs/sms/bin/python
import site
site.addsitedir("/cs/home/bjl7/Envs/sms/lib/python2.6/site-packages")
print "Content-type: text/html\n\n"
from wsgiref.handlers import CGIHandler
from sms import app

CGIHandler().run(app)
