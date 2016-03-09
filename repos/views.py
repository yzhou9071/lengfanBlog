from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
#from models import Userinfo
from django.shortcuts import render_to_response
import calendar, datetime

def index(request) :
	"""The repos index"""
	return render(
		request,
		"repos/index.html",
		{
		}
	)
