#!/usr/bin/python3.10.4
# -*- coding: utf-8 -*-
# @Author  : yinchentao
# @Time    : 2023/2/18 14:01
# @File    : base_model.py
from django.db import models


class BaseModel(models.Model):
	'''抽象基类'''
	create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
	update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

	class Meta:
		# 指定抽象基类
		abstract = True
