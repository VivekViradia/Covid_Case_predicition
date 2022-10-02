from django.shortcuts import render

# Create your views here.
import numpy as np
import pickle
# for create unique Id
import uuid
from django.shortcuts import render
from rest_framework import generics
from .models import *
# from .serializers import ImagesSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import StaticHTMLRenderer
from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect



class CovidAPIView(APIView):
    def post(self, request, *args, **kwargs):
        f = int(request.data['date_1'])
        print("--------",f)
        model =pickle.load(open('E:\GTU\Covid\lr_pkl','rb'))
        output = model.predict(np.array(f).reshape(-1,1))
        return Response({'message':"Done","Number Of Covid Cases":output})
