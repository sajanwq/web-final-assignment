from django.shortcuts import redirect
from Admin.models import admin
from django.contrib import messages
#class where authentication is done
class Authentication:
    def is_admin_user(function):
        def wrap(request):
            print(request)
            try:
                admin.objects.get(Emai_ID=request.session['Email_ID'], Password=request.session['Password'])
                return function(request)
            except:
                print("no valid")
                messages.warning(request,'Invalid login.')
            return redirect('/homepage/loginpage_render/')
        return wrap
    def valid_id_admin(function):
        def wrap(request, id):
             try:
                admin.objects.get(Email_ID=request.session['Email_ID'], Password = request.session['Password'])
                return function(request,id)
             except:
                messages.warning(request,'Please enter valid email and password')
                return redirect('/homepage/loginpage_render/')
        return wrap