#!/usr/bin/python3.10.4
# -*- coding: utf-8 -*-
# @Author  : yinchentao
# @Time    : 2023/2/18 14:17
# @File    : urls.py
from django.urls import path,include
from apps.basic import views

urlpatterns = [
    path('index/',views.index),
]

