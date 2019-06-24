from django.shortcuts import render
from django.http import HttpResponse
from chatapp import corp
import json
def index(request):
    return render(request,'chatbot.html')
def getdata(request):
    if request.method == 'POST' and request.is_ajax():
        print(request.is_ajax)
        value = request.POST['text']
        v1=corp.solution(value)
    return HttpResponse(json.dumps({'data':v1}),content_type='application/json')