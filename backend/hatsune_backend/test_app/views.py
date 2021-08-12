from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>hello world</h1>')

def test(request):
    return JsonResponse({ 'data': 'hej' })

def ping(request):
    return JsonResponse(request.data)
