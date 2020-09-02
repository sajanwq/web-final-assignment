from django.shortcuts import render, redirect
from movies.models import movie
from movies.forms import movieForms


# Creating  views for retreiving data.
def index(request):
    data = movie.objects.all()
    return render(request, "movies/retrieve.html", {'table_data': data})

# Creating  views for retreiving data in movie page
def datamovie(request):
    data = movie.objects.all()
    return render(request, "homepage/movies.html", {'table_data': data})



# Creating  views for creating data.
def create(request):
    if request.method == "POST":
        print(request.POST)
        form = movieForms(request.POST)
        form.save()
        return redirect("/movies/retrieve_path/")
    else:
        form = movieForms()
    return render(request, "movies/create.html", {'forms': form})


# creating function for edit
def edit(request, m_id):
    try:
        data = movie.objects.get(Id=m_id)
        return render(request, "movies/edit.html", {'values': data})
    except:
        print("no data")
        return redirect("/movies/retrieve_path")


# creating function for update
def update(request, p_id):
    data = movie.objects.get(Id=p_id)
    form = movieForms(request.POST, instance=data)
    if form.is_valid():
        try:
            form.save()
            return redirect("/movies/retrieve_path")
        except:
            print("the form is invalid")
    return render(request, "movies/edit.html", {'values': data})


#creating function for delete button
def delete(request, id):
    try:
        value = movie.objects.get(Id=id)
        print(value)
        value.delete()
        return redirect("/movies/retrieve_path")
    except:
        print("no data")
