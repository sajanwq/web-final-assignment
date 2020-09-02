from django.shortcuts import render, redirect

from Admin.forms import adminForms
from Admin.models import admin

# Creating  views for retreiving data.
def index(request):
    data = admin.objects.all()
    return render(request, "admin/admindetail.html", {'datas': data})

# Creating  views for creating data.
def create(request):
    if request.method == "POST":
        print(request.POST)
        form = adminForms(request.POST)
        form.save()
        return redirect("/Admin/retrieve_path/")
    else:
        form = adminForms()
    return render(request, "admin/create.html", {'datas': form})


# creating function for edit
def edit(request, p_id):
    try:
        data = admin.objects.get(Id=p_id)
        return render(request, "admin/edit.html", {'datas': data})
    except:
        print("no data")
        return redirect("/Admin/retrieve_path")


# creating function for update
def update(request, p_id):
    data = admin.objects.get(Id=p_id)
    form = adminForms(request.POST, instance=data)
    print(form)
    if form.is_valid():
        try:
            form.save()
            return redirect("/Admin/retrieve_path/")
        except:
            print("the form is invalid")
    return render(request, "admin/edit.html", {'datas': data})

#creating function for delete button
def delete(request, d_id):
    try:
        value = admin.objects.get(Id=d_id)
        value.delete()
        return redirect("/Admin/retrieve_path")
    except:
        print("no data")


