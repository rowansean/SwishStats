from django.shortcuts import render
import requests, os
from django.http import JsonResponse
import os
from dotenv import load_dotenv
load_dotenv()

# Create your views here.
def get_teams(request):
    url = "http://api.balldontlie.io/v1/teams"
    headers = {"Authorization": os.getenv('BALLDONTLIE_API_KEY')}
    # catch errors
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return JsonResponse(data)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"API FAILED TO REQUEST": str(e)})