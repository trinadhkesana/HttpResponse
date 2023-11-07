from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Jampandu(request):
    return HttpResponse('<hi><marquee>hai how are you</hi></marquee>')
def Jigelrani(request):
    return HttpResponse('<hi><marquee>i am busy with chittibabu</hi></marquee>')
