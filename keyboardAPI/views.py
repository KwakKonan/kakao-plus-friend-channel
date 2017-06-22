from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def testResponse(request):
    data = {
      "type": "text"
    }
    print()
    return HttpResponse(json.dumps(data), status=200)
