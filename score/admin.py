from django.contrib import admin
from score.models import worker,Company,Procdure,work_steam,score
# Register your models here.

admin.site.register([worker,Company,Procdure,work_steam,score])