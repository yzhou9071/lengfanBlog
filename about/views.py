from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from models import AboutDownload,AboutAuthorDetail
from django.shortcuts import render_to_response
import calendar, datetime
from django.http import HttpResponse

def index(request) :
	"""The about index"""
	aboutDownload = AboutDownload.objects.all()
	aboutAuthorDetail = AboutAuthorDetail.objects.all()
	return render(
		request,
		"about/index.html",
		{
			"aboutDownload" : aboutDownload,
			"aboutAuthorDetail" : aboutAuthorDetail,
		}
	)

def updateAboutDetailNum(request) :
    req = request.GET
    req = req.copy()
    req.getlist('downloadTitle')
    downloadTitle = req['downloadTitle']
    aboutdownload = get_object_or_404(AboutDownload, downloadTitle=downloadTitle)
    aboutdownload.downloadNum = aboutdownload.downloadNum + 1
    aboutdownload.save()
    return HttpResponse("Success")
