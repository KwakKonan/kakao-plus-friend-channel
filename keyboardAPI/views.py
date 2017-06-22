from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testResponse():
    return HttpResponse(status=200)