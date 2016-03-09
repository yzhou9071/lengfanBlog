from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from models import BookDetail
from django.shortcuts import render_to_response
import calendar, datetime

def index(request) :
	"""The books index"""
	bookDetail = BookDetail.objects.all()
	hasRead = 0
	unRead = 0
	totalBook = len(bookDetail)
	for bookItem in bookDetail:
		if bookItem.bookState == 1:
			hasRead = hasRead + 1
		else:
			unRead = unRead + 1
	return render(
		request,
		"books/index.html",
		{
			"bookDetail"	: bookDetail,
			"hasRead"   : hasRead,
			"unRead"    : unRead,
			"totalBook" : totalBook,
		}
	)
