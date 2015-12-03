from django.shortcuts import render,get_object_or_404
from .models import FJUUser, Course, Module_content, Enrollment_Details, Module_Details
from django.http import HttpResponseRedirect
from django.http import Http404
from django.utils import timezone
# import datetime
from datetime import datetime, timedelta
# Create your views here.

def index(request):
	return render(request, "Enroll/enrolled.html", {})

def enrollment(request,course_id):
	course_details = get_object_or_404(Course, pk= course_id)
	return render(request, "Enroll/enrollment.html", {'course_details' : course_details})

def enrollment1(request,course_id):
	email = FJUUser.objects.get(pk = "yaswanthraj671@gmail.com")
	start_date = request.POST.get('start_date')
	category = request.POST.get('category')
	working_format = request.POST.get('working_format')
	hours = int(request.POST.get('hours'))
	course_details = get_object_or_404(Course, pk= course_id)
	delta = timedelta(days= (course_details.duration / hours) + 7)
	s_date = datetime.strptime(start_date, '%Y-%m-%d')
	end_date = s_date + delta
	e = Enrollment_Details(email = email, course_id = Course.objects.get(pk = course_id) , start_date = start_date, end_date = end_date,category = category, working_format = working_format, hours = hours)
	e.save()

	enrollment_details = get_object_or_404(Enrollment_Details, pk = course_details.course_id)
	return render(request, "Enroll/enrolled.html", {'enrollment_details' : enrollment_details})

def enrolled(request, course_id):
	course_details = get_object_or_404(Enrollment_Details, pk= course_id)
	return render(request, "Enroll/enrolled.html", {'course_details' : course_details})