from django.contrib import admin

# Register your models here.
from .models import FJUUser, Course, Module_content, Enrollment_Details, Module_Details

class FJUUserAdmin(admin.ModelAdmin):
	list_display = ['email']
		
admin.site.register(FJUUser, FJUUserAdmin)
admin.site.register(Course)
admin.site.register(Module_content)
admin.site.register(Enrollment_Details)
admin.site.register(Module_Details)