from django.shortcuts import render
from .models import Customer 

# Create your views here.
def indexPageView(request) :
    result = Customer.objects.all()
    return render(request, 'kidsTable.html', {'data' : result})

   


def personView (request, personid):
   data = Customer.objects.all()
   context = { 
      'person' : data
   }
    
   return render (request, 'persons/person.html', context )

