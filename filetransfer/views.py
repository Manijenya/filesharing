# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging, json, string
import logging.handlers
from django.shortcuts import render,redirect,reverse,render_to_response

from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.db import connection
from .models import *
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from rest_framework.authentication import SessionAuthentication

logger_obj = logging.getLogger('logit')


class DasboardView(View):
    ''' 
    21-Sun-2019 To Dashboard page loaded.
    @param request: Request Object
    @type request : Object
    @return:   HttpResponse or Redirect the another URL
    @author: MKM
    '''
    template_name = "filetransfer/index.html"
     
    def get(self, request, *args, **kwargs):
        # if request.user.is_authenticated():
        cur = connection.cursor()
        if request.user.is_authenticated:
            file_list = File.objects.filter(is_active = True)
            #return render(self.request, 'photos/basic_upload/index.html', {'photos': photos_list})
            print "-----", request.user.username

            return render(request, self.template_name, {'username':request.user.username, 'upload_file':file_list,
                                                        'role': request.user.is_superuser})
        else:
            return HttpResponseRedirect('/')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DasboardView, self).dispatch(request, *args, **kwargs)
class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  def delete(self, request, *args, **kwargs):
    data=request.data['file_id']
    if data:
        File.objects.filter(pk=data).update(is_active=False)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
      return Response(status=status.HTTP_400_BAD_REQUEST)