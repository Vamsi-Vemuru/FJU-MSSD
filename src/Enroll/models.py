from django.db import models

# Create your models here.
class FJUUser(models.Model):
    
    email = models.EmailField(max_length=200, primary_key = True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    display_name = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    confirm_password=models.CharField(max_length=15)
    def publish(self):
        self.save()

    def __str__(self):
        return self.email

class Course(models.Model):
	course_id = models.CharField(max_length=10, primary_key = True)
	course_title = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	specialization = models.CharField(max_length=200, blank = True)
	duration = models.IntegerField(default = 0)
	level = models.CharField(max_length = 20, default = "Easy")
	def __unicode__(self):
		return self.level
	def __unicode__(self):
		return self.title_text
	def __unicode__(self):
		return self.description
	def __unicode__(self):
		return self.specialization
	def __int__(self):
		return self.duration
	def __str__(self):
		return self.course_id

class Module_content(models.Model):
	course_id = models.ForeignKey(Course)
	module_no = models.IntegerField()
	module_title = models.CharField(max_length=200)
	objective = models.CharField(max_length=500)
	challenge = models.CharField(max_length=200, blank = True)
	show_how = models.CharField(max_length=500, blank = True)
	references = models.CharField(max_length=500, blank = True)
	def __unicode__(self):
		return self.course_id
	def __unicode__(self):
		return self.module_title
	def __unicode__(self):
		return self.objective
	def __unicode__(self):
		return self.challenge
	def __unicode__(self):
		return self.show_how
	def __unicode__(self):
		return self.references
	def __int__(self):
		return self.module_no

class Enrollment_Details(models.Model):
	email = models.ForeignKey(FJUUser)
	course_id = models.ForeignKey(Course, unique = True)
	start_date = models.DateField()
	end_date = models.DateField(default = None, blank = True)
	category = models.CharField(max_length = 200, blank= True)
	working_format = models.CharField(max_length = 200, blank = True)
	hours = models.IntegerField(blank = True)

class Module_Details(models.Model):
	course_id = models.ForeignKey(Enrollment_Details)
	module_no = models.ForeignKey(Module_content)
	due_date = models.DateField(default = None,blank = True)