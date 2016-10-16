from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from interfaceFactory import classDelegator

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def call_delegate(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        delegatorInstance = classDelegator.delegator()
        response = delegatorInstance.delegateAndCall("dummyClass","dummyMethod")
        return JSONResponse(data=response[0],status=response[1])

    elif request.method == 'POST':
        return JSONResponse(data = "Post Not Supported",status = 404)
