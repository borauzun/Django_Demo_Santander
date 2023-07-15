from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def helloWorld(request):
    return JsonResponse({"msg":"Hello World2"}, safe=False)

@csrf_exempt
@api_view(["GET","POST","PUT"])
def helloWorld2(request):
    if request.method == 'POST':
        aToken=request.headers['Authorization']
        data = JSONParser().parse(request)

        return JsonResponse({"msg":"Hello World"}, safe=False)

@csrf_exempt
@api_view(["GET","POST","PUT"])
def addPerson(request):
    if request.method == 'POST':
        aToken=request.headers['Authorization']
        data = JSONParser().parse(request)

        return JsonResponse({"msg":"Hello World"}, safe=False)

@csrf_exempt
@api_view(["GET"])
def getId(request,name):
    if request.method == 'GET':
        pass