#-*- coding:UTF-8
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
import datetime
# Create your models here.
class User(models.Model):
	username=models.CharField(max_length=50,primary_key=True)
	password=models.CharField(max_length=50,default='')
	group=models.CharField(max_length=50,default="User")
	def __unicode__(self):
		return self.username
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
class test(models.Model):
	serial_number=models.CharField(verbose_name=u'编号',max_length=10,default='')
	name=models.CharField(u'姓名',max_length=10,default='')
	typ=models.CharField(u'变更类型',max_length=10,default='')
	remark=models.TextField(verbose_name=u'变更说明', default='')
	create_time=models.DateTimeField(verbose_name=u'创建时间', default=datetime.datetime.now())
class nav_link(models.Model):
	
admin.site.register(User)