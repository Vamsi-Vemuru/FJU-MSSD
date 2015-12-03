from django.shortcuts import render
from .models import *

# Create your views here.
def faqs(request):
	# Ques = Faq.objects.all()
	
	#context = RequestContext(request,{'Quest':Ques})
	return render(request,'faq.html',{})

def askq(request):
	# email = EmailMessage('Hello', 'World', to=['user@gmail.com'])
	# email.send()
	return render(request,'ask.html',{})
def modulepage(request):
	courseobj = Course.objects.all()
	moduledataobj = Module_content.objects.all()
	mod_list = {}
	for course in courseobj:
		for module in moduledataobj:
			if course.title_text in mod_list:
				if str(course.course_id) == str(module.course_id):
					data = {
							'mt':module.module_title,
							'lo':module.objective,
							'chal':module.challenge,
							'sh':module.show_how,
							'ref':module.references
					}
					mod_list[course.title_text].append(data)
			else:
				if str(course.course_id) == str(module.course_id):
					data = {
							'mt':module.module_title,
							'lo':module.objective,
							'chal':module.challenge,
							'sh':module.show_how,
							'ref':module.references
					}
					# dic = {module.module_title:data}
					mod_list[course.title_text] = [data]
	print mod_list
	return render(request, "modulepage.html", {'mod_list':mod_list})
