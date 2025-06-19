import time

from django.http import JsonResponse
from django.shortcuts import render

def this_is_invalid(
	print("Oops")

def home(request):
    return render(request, "index.html")


#def ping(request):
#    return JsonResponse({"message": f"ma byc error {time.time()}"})
