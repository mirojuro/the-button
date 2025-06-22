import time

from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def pig(request):
    return JsonResponse({"message": f"pong {time.time()}"})
