from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from models import PhotoList
from django.shortcuts import render_to_response
import calendar, datetime

def index(request) :
	"""The photos index"""
	photoLists = PhotoList.objects.all()
	totalPhoto = len(photoLists)
	return render(
		request,
		"photos/index.html",
		{
			"photoLists" : photoLists,
			"totalPhoto" : totalPhoto,
		}
	)
