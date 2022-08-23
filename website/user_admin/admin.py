from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(QuestionBank)
admin.site.register(QuestionAnswer)
admin.site.register(CorrectAnswer)
admin.site.register(Subject)
admin.site.register(MyUser)