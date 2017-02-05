from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from score.forms import LogForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
def login(request):
	if request=="GET":
		form=LogForm()
		return render(request,"login.html",RequestContext(request,{'form':form}))
	else:
		form=LogForm(request.POST)
		if form.is_valid():
			username=request.POST.get('username','')
			password=request.POST.get('password','')
			user=auth.authenticate(username=username,password=password)
			if user is not None and user.is_active:
				return HttpResponse("loging")
			else:
				return HttpResponse("get out")
		else:
			return render(request,"login.html",RequestContext(request,{'form':form}))
@login_required
def logout(request):
    auth.logout(request)
    return render(request,"login.html",RequestContext(request,{'form':form}))
