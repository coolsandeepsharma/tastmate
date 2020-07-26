from django.shortcuts import render, redirect
from .form import Custom_reg_form
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=="POST":
        register_form = Custom_reg_form(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("Account has been Created!, Login to Get Started!"))
            return redirect('register')
    else:
        register_form = Custom_reg_form()
    return render(request, 'register.html', {'register_form': register_form})
