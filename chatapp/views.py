from django.shortcuts import render
from django.http import HttpResponse
import json
from chatapp import logic
# Create your views here.
i=0
def index(request):
    return render(request,'chatbot.html')
def getdata(request):
    if request.method == 'POST' and request.is_ajax():
        print(request.is_ajax)
        value = request.POST['text']
        print(value)
        if(value == "Employee Details"):
            return HttpResponse(json.dumps({'field1':'Employee Name','field2':'Phone number','field3':'any other'}),content_type='application/json')
        else:
            v1 = "Presently FAQ's are not developed"
        global i
        type=(i%2)
        i=i+1
        print('else')
    return HttpResponse(json.dumps({'type':type,'data':v1}),content_type='application/json')