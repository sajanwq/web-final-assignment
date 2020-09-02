from django.shortcuts import render, redirect


#function for hompage render
def homepageindex(request):
    return render(request, "homepage/homepage.html")


#function for login render
#def loginindex(request):
   # return render(request, "homepage/login.html")

#function for tickets render
def ticketsindex(request):
    return render(request, "homepage/tickets.html")



def login(request):
    if request.method == "POST":
        try:
            request.session['Email_ID'] = request.POST['Email_ID']
            request.session['Password'] = request.POST['Password']
            return redirect("/Admin/retrieve_path/")
        except:
            print("Error")
    return render(request, "homepage/login.html")


