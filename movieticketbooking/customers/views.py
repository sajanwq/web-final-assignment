
from django.shortcuts import render, redirect

from customers.forms import customerForms
from customers.models import customer
from django.contrib import messages
from movies.models import movie



# Creating  views for retreiving data.
def index(request):
    data = customer.objects.all()
    return render(request, "customers/details.html", {'table_data': data})

def delete(request, p_id):
    try:
        value = customer.objects.get(Id=p_id)
        print(value)
        value.delete()
        return redirect("/customers/retrieve_path")
    except:
        print("no data")

        # Creating  views for creating data.

def create(request):

    if request.method == "POST":
        print(request.POST)
        form = customerForms(request.POST)
        if customer.objects.filter(Email=request.POST['Email']).exists():
            print("email taken")
            messages.error(request, "sorry,email id already taken")
            return redirect("/customers/signup/")

        else:
            form.save()
        return redirect("/homepage/homepage_render/")
    else:
        form = customerForms()
        return render(request, "homepage/signup.html", {'forms': form})

