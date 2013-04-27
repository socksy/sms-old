#!/cs/home/cs3099userc/Envs/sms/bin/python
import site
site.addsitedir("/cs/home/cs3099userc/Envs/sms/lib/python2.6/site-packages")
from wsgiref.handlers import CGIHandler
from hello import app

CGIHandler().run(app)
