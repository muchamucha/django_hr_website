#leftmenu.py
#-*- coding:UTF8
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.models import User,Group
from django.http import HttpResponse
def layout(request):
	grouplist=[]
	user=auth.authencate(username=request.username,password=request.password)
	for group in Group.objects.all():
		if user in User.objects.filter(group__name=group.name):
			grouplist.append(group.name) #grouplist用于渲染左边菜单的权限

	return render(request,)	

