# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Photo
from django.contrib import admin

class PhotoAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp"]

	class Meta:
		model = Photo

admin.site.register(Photo, PhotoAdmin)