from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
# Validate that the api is working
def index(request):
    response={
        "response": "working"
    }
    return JsonResponse(response)