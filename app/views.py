from django.http import HttpResponse
from datetime import datetime

def hello(request):
    s = 'Hello World!'
    current_time = datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)
