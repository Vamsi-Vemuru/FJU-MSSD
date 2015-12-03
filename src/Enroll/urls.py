from django.conf.urls import url
from .import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^(?P<course_id>[0-9]+)/enrollment$', views.enrollment, name='enrollment'),
	url(r'^(?P<course_id>[0-9]+)/enrollment1$', views.enrollment1, name='enrollment'),
    url(r'^(?P<course_id>[0-9]+)/enrolled$', views.enrolled, name='enrolled'),
]