from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Course)
admin.site.register(FJUUser)
admin.site.register(Module_content)
admin.site.register(Submissions)
admin.site.register(Enrollment_Details)
admin.site.register(Module_Details)
admin.site.register(Reward)