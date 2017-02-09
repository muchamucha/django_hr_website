#-*- coding:UTF-8
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import Group
import datetime

class Company(models.Model):
	sn=models.CharField(max_length=100,default="")
	company=models.CharField(max_length=100,default="")
	def __unicode__(self):
		return self.company
class Procdure(models.Model):
	sn=models.CharField(max_length=50,primary_key=True)
	basic_class=models.CharField(max_length=100)
	product=models.CharField(max_length=100)
	step_name=models.CharField(max_length=100)
	company_id=models.ForeignKey(Company)
	def __unicode__(self):
		return self.step_name
class worker(models.Model):
	sn=models.CharField(u"序列",max_length=50,primary_key=True)
	name=models.CharField(u"姓名",max_length=50)
	birth_place=models.CharField(u"籍贯",max_length=50)
	birth_date=models.DateField(u"出生日期",auto_now=False)
	work_level=models.IntegerField(u"级别")
	def __unicode__(self):
		return self.name
class work_steam(models.Model):
	sn=models.CharField(max_length=50,primary_key=True)
	woker_id=models.ForeignKey(worker)
	company=models.ForeignKey(Company)
	step=models.ForeignKey(Procdure)
	quantity=models.IntegerField()
	def __unicode__(self):
		return self.sn
class score(models.Model):
	worker_id=models.ForeignKey(worker)
	score=models.IntegerField()
	def __unicode____(self):
		return str(self.worker_id)+str(self.score)
class test2(models.Model):
	serial_number=models.CharField(verbose_name=u'编号',max_length=10,default='')
	name=models.CharField(u'姓名',max_length=10,default='')
	typ=models.CharField(u'变更类型',max_length=10,default='')
	remark=models.TextField(verbose_name=u'变更说明', default='')
	create_time=models.DateTimeField(verbose_name=u'创建时间', default=datetime.datetime.now())
class left(models.Model):
	link_id=models.AutoField(primary_key=True,unique=True)
	label=models.CharField(max_length=10,default="link")
	link=models.CharField(max_length=200,default="")
	pic=models.ImageField(upload_to="static/images/",blank=True)
	authlevel=models.ManyToManyField(Group,blank=True)
	parent_id=models.ForeignKey('self',blank=True,null=True,verbose_name=u"父菜单")
	CHOICES=(("P",u"父菜单"),("S",u"子菜单"))
	menulevel=models.CharField(max_length=2,verbose_name=u"菜单级别",choices=CHOICES)
	def __unicode__(self):
		return self.label

#权限需要一对多
	
# admin.site.register(User) #当使用score自带用户使使用