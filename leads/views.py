from django.shortcuts import render
from django.http import HttpResponse
from .models import lead

def lead_list(request):
  leads = lead.objects.all()
  #leads is now  a list of data querysets
  context = {
    "leads": leads
  }
  return render(request, "leads/lead_list.html", context)