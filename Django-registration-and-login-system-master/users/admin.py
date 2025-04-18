from django.contrib import admin
from .models import Profile,Course,contactus,Exam,Result

admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(contactus)
admin.site.register(Result)