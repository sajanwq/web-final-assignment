from django.shortcuts import render, redirect
from Booking.models import booking
from Booking.forms import bookingForms

# Creating  views for retreiving data.
def index(request):
    datas = booking.objects.all()
    return render(request, "booking/bookingdetail.html", {'data': datas})




def createbook(request):
    if request.method == "POST":
        form = bookingForms(request.POST)
        form.save()
        return redirect("/homepage/homepage_render/")
    else:
        form = bookingForms()
    return render(request, "homepage/tickets.html", {'forms': form})

#creating function for delete button
def delete(request, id):
    try:
        value = booking.objects.get(Id=id)
        value.delete()
        return redirect("/Booking/retrieve_path")
    except:
        print("no data")





