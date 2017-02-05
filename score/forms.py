#-*- coding:utf-8
from django import forms
from django.contrib.auth.models import User
from score.models import test,worker

class WorkerForm(forms.ModelForm):
	class Meta:
		model=worker
		fields=('name','birth_place','birth_date','work_level')
	# def __init__(self, *args, **kwargs):
	# 	super(LogForm, self).__init__(*args, **kwargs)
	# 	self.fields['serial_number'].widget=forms.TextInput({'class': 'form-control'})

# class WorkerLevelForm(forms.ModelForm):
# 	class Meta:
# 		model=worker.work_level
class LogForm(forms.Form):
	username=forms.CharField(
		required=True,
		label=u"用户名",
		error_messages={'required':u"输入用户名"},
		widget=forms.TextInput(
			attrs={
			'placeholder':u"用户名",
			}
			),
		)
	password=forms.CharField(
		required=True,
		label=u"密 码",
		error_messages={'required':u"输入密码"},
		widget=forms.PasswordInput(
			attrs={
			'placeholder':u"密码",			
			}),
		)
	# def clean(self):
	# 	if not self.is_valid():
	#  		raise forms.ValidationError(u"用户名和密码为必填项")
	# 	else:
	# 		cleaned_data = super(LogForm, self).clean()