from django.db import models
from django.db.models import Max
# Create your models here.

class Course(models.Model):
	course_id = models.CharField(max_length=10, primary_key = True)
	title_text = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	specialization = models.CharField(max_length=200, blank = True)
	duration = models.IntegerField(default = 0)
	level = models.CharField(max_length = 20, default = "Easy")
	def __unicode__(self):
		return  self.course_id

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

    def __unicode__(self):
        return self.email

class Module_content(models.Model):
	course_id = models.ForeignKey('Course')
	module_no = models.IntegerField()
	module_title = models.CharField(max_length=200)
	objective = models.CharField(max_length=500)
	challenge = models.CharField(max_length=200, blank = True)
	show_how = models.CharField(max_length=500, blank = True)
	references = models.CharField(max_length=500, blank = True)
	def __unicode__(self):
		return self.module_title

def get_filename(instance, filename):
	url = 'documents/%s/%s/%s' % (instance.username,instance.version,filename)
	return url


class Submissions(models.Model):
	submitTime = models.DateTimeField(auto_now=True)
	username = models.EmailField()
	module_no = models.ForeignKey('Module_content')
	submission = models.FileField()
	version = models.IntegerField(default=1)
	course_id = models.ForeignKey('Course')
	def __unicode__(self):
		return self.username
	def save(self):
		o = Document.objects.filter(username=self.username, module_no=self.module_no)
		
		if o.exists():
			o = o.all().aggregate(Max('version'))
			print o
			self.version = o['version__max'] + 1
		else:
			self.version = 1
		super(Document, self).save()

class Enrollment_Details(models.Model):
	email = models.ForeignKey('FJUUser')
	course_id = models.ForeignKey('Course')
	start_date = models.DateField()
	end_date = models.DateField(default = None, blank = True)
	category = models.CharField(max_length = 200, blank= True)
	working_format = models.CharField(max_length = 200, blank = True)
	hours = models.IntegerField(blank = True)
	def __unicode__(self):
		return self.email

class Module_Details(models.Model):
	course_id = models.ForeignKey('Enrollment_Details')
	module_no = models.ForeignKey('Module_content')
	due_date = models.DateField(default = None,blank = True)

class Reward(models.Model):
	username = models.ForeignKey('Submissions')
	reward = models.IntegerField(default=0)
	def __unicode__(self):
		return self.username