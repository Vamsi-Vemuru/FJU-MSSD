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
	categories = Course.objects.all()
	c_names = Module_content.objects.all()
	mod_list = {}
	for category in categories:
		for c_name in c_names:
			if category.title_text in mod_list:
				if str(category.course_id) == str(c_name.course_id):
					mod_list[category.title_text].append(c_name.module_title)
			else:
				if str(category.course_id) == str(c_name.course_id):
					mod_list[category.title_text] = [c_name.module_title]
	print mod_list
	return render(request, "modulepage.html", {'mod_list':mod_list})
