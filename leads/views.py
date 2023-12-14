from django.shortcuts import render , redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView , DetailView, CreateView, UpdateView
from .models import lead, Agent
from .forms import LeadForm , LeadModelForm


def landing_page(request):
   return render(request, "landing.html")


#classview example

class LeadListView(ListView):
   template_name="leads/lead_list.html"
   queryset = lead.objects.all() #here in function we need to create dictionary context but queryset is a defualt  context with name object_name.
   


def lead_list(request):
  leads = lead.objects.all()
  #leads is now a list of data querysets
  context = {
    "leads": leads
  }
  print(context)
  #how to understand the dictionary logic and visuallise it?
  return render(request, "leads/lead_list.html" , context)

class LeadDetailView(DetailView):
   template_name="leads/lead_details.html"
   queryset = lead.objects.all() #here in function we need to create dictionary context but queryset is a defualt  context with name object_name.
   context_object_name = "lead"

def lead_detail(request, pk):
    print(pk)
    Lead = lead.objects.get(id=pk)
    #there is alead confusion
    context = {
       "lead": Lead
    }
    
    return render(request, "leads/lead_details.html", context)  

class LeadCreateView(CreateView):
   template_name="leads/lead_create.html"
   form_class = LeadModelForm
   
   def get_success_url(self):
      return "/leads"


def lead_create(request):
   form = LeadModelForm()
   #first setting form empty by leaving leadform empty
   if request.method == "POST":
      print('Receoving a post request')
      form = LeadModelForm(request.POST)
      if form.is_valid():
         #first_name = form.cleaned_data['first_name']
         #last_name = form.cleaned_data['last_name']
         #age = form.cleaned_data['age']
         #agent = form.cleaned_data['agent']
         #lead.objects.create(
         #   first_name= first_name,
         #   last_name = last_name,
         #   age = age,
         #   agent = agent
         #)
         form.save()
         #form.save does the exact thing as above lines
          
         print("The lead has been created")

         return redirect("/leads")
         

   context={
      "form": form
   }
   return render(request, "leads/lead_create.html", context)


def lead_update(request, pk):
   Lead = lead.objects.get(id = pk)
   form = LeadModelForm(instance=Lead)
   if request.method == "POST":
      form = LeadModelForm(request.POST, instance=Lead)
      if form.is_valid():
         form.save()
         return redirect("/leads")
   context = {
      "form": form,
      "lead": Lead
     }
   return render (request, "leads/lead_update.html", context)




def lead_delete(request, pk):
   Lead = lead.objects.get(id = pk)
   Lead.delete()
   return redirect("/leads")



# def lead_update(request, pk):
#     Lead = lead.objects.get(id=pk)
#     form = LeadForm()
#    #first setting form empty by leaving leadform empty
#     if request.method == "POST":
#       form = LeadForm(request.POST)
#       if form.is_valid():
#          first_name = form.cleaned_data['first_name']
#          last_name = form.cleaned_data['last_name']
#          age = form.cleaned_data['age']
#          Lead.first_name = first_name
#          Lead.last_name = last_name
#          Lead.age = age
#          Lead.save()
#          #form.save does the exact thing as above lines
#          return redirect("/leads")
   
#     context = {
#       "form": form,
#       "lead": Lead
#     }
#     return render (request, "leads/lead_update.html", context)

    

