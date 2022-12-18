import json
from django.contrib import messages
from django.core.files.storage import FileStorage
from django.shortcuts import HttpResponse, HttpResponseRedirect, get_object_or_404, render, redirect
from django.templatetags.static import Static
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView

from .forms import *
from .models import *

