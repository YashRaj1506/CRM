from django.shortcuts import render
from django.http import HttpResponse
from .models import lead

def lead_list(request):
  leads = lead.objects.all()
  #leads is now a list of data querysets
  context = {
    "leads": leads
  }
  #how to understand the dictionary logic and visuallise it?
  return render(request, "leads/lead_list.html" , context)

def lead_detail(request, pk):
    print(pk)
    Lead = lead.objects.get(id=pk)
    #there is alead confusion
    context = {
       "lead": Lead
    }
    return render(request, "leads/lead_details.html", context)  