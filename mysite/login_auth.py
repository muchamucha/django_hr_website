#-*- coding:utf-8
from django.contrib.auth import authenticate
def user_verify(user,pwd):
	user=authenticate(username=user,password=pwd)
	if user is not None:
		if user.is_active:
			return True
		else:
			return False
	else:
		return False