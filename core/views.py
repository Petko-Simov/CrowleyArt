from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def static_base(request: HttpRequest) -> HttpResponse:
    return render(request, 'base.html')