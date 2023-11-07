from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Trinadh(request):
    return HttpResponse('<hi><marquee>hai how are you</hi></marquee>')
def response(request):
    return HttpResponse('<hi><marquee>i am fine</hi></marquee>')
