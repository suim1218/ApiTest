from ApiManager.models import Project, Module, TestCase
import json
import os
from wang_http import settings
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, render_to_response


def report(request):
    return render(request, 'result.html')
