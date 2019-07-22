"""
Login View   and Logout URLS
"""
from django.conf.urls import url
from . import views
from .views import *

urlpatterns = [
    url(r'^$', DasboardView.as_view(), name="dashboard_page"),
    url(r'^upload/$', FileView.as_view(), name='file-upload'),
    #url(r'^student_list/$', student_list, name="student_list"),
]
