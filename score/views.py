#-*- coding:UTF-8
from django.shortcuts import render,redirect
from score.models import score,worker
from django.http import HttpResponse
from score.forms import LogForm,WorkerForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def add(request):
	form=score.forms.WorkerForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect('/worker/')
	context={'form':form,}
	return render(request,'add.html',context)

def login(request):
	if request=="GET":
		form=LogForm()
		return render(request,"login.html",{'form':form})
	else:
		form=LogForm(request.POST)
		if form.is_valid():
			username=request.POST.get('username','')
			password=request.POST.get('password','')
			user=auth.authenticate(username=username,password=password)
			if user is not None and user.is_active:
				return redirect(index)
			else:
				return HttpResponse("get out")
		else:
			return render(request,"login.html",{'form':form})
def score_list(request):
	return HttpResponse(score.objects.all())
def worker_list(request):
	table=worker.objects.all()
	return render(request,'table.html',{'labels':WorkerForm,'table':table,'table_name':"工人名单","class":"worker"})
def test(request):
	return render(request,'test.html',{'form':LogForm})
# Create your views here.
@login_required
def index(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	u=User.objects.filter(username=username)
	#return render(request,'base.html')
	return HttpResponse(u)