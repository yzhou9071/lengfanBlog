from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from models import Category, Article
from django.shortcuts import render_to_response
import calendar, datetime

def index(request) :
	"""The blog index"""
	allCategory = Category.objects.order_by('categoryID').all()
	articles = Article.objects.all()
	for itemCat in allCategory:
		category = get_object_or_404(Category, slug=itemCat.slug)
		article_queryset = Article.objects.filter(categories=category)
		itemCat.categoryID = len(article_queryset)
	for itemArt in articles:
		itemArt.content_markdown = itemArt.content_markdown[0:87]
	totalNum = len(articles)

	page = request.GET.get('page')
	article_queryset = Article.objects.all()
	paginator = Paginator(article_queryset, 20)
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		articles = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		articles = paginator.page(paginator.num_pages)

	return render(
		request,
		"blog/article/index.html",
		{
			"articles" : articles,
			"categories" : allCategory,
			"totalNum" : totalNum
		}
	)

def single(request, slug) :
	"""A single article"""
	article = get_object_or_404(Article, slug=slug)
	article.pv = article.pv + 1
	article.save()
	categoryName = article.categories.all()[0].title
	archive_dates = Article.objects.dates('publishDate','month', order='DESC')
	allCategory = Category.objects.all()
	for itemCat in allCategory:
		category = get_object_or_404(Category, slug=itemCat.slug)
		article_queryset = Article.objects.filter(categories=category)
		itemCat.categoryID = len(article_queryset)

	articles = Article.objects.order_by('publishTime').all()
	previousArticle = {'slug':'','title':''}
	nextArticle = {'slug':'','title':''}
	for itemArt in articles:
		if itemArt.id == article.id:
			if article.id != 1:
				previousArticle['slug'] = articles[itemArt.id - 1].slug
				previousArticle['title'] = articles[itemArt.id - 1].title
			if article.id != len(articles):
				nextArticle['slug'] = articles[itemArt.id].slug
				nextArticle['title'] = articles[itemArt.id].title
			break

	articles = Article.objects.filter(categories=category)
	totalNum = len(Article.objects.all())
	return render(
			request,
			"blog/article/single.html",
			{
				"article" : article,
				"archive_dates" : archive_dates,
				"categories" : allCategory,
				"categoryName" : categoryName,
				"previousArticle" : previousArticle,
				"nextArticle" : nextArticle,
				"totalNum" : totalNum
				}
			)

def category_archive(request, slug):
	"""The blog list by category"""
	archive_dates = Article.objects.dates('publishDate','month', order='DESC')
	allCategory = Category.objects.all()

	for itemCat in allCategory:
		category = get_object_or_404(Category, slug=itemCat.slug)
		article_queryset = Article.objects.filter(categories=category)
		itemCat.categoryID = len(article_queryset)

	category = get_object_or_404(Category, slug=slug)
	totalNum = len(Article.objects.all())

	page = request.GET.get('page')
	article_queryset = Article.objects.filter(categories=category)
	paginator = Paginator(article_queryset, 5)
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		articles = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		articles = paginator.page(paginator.num_pages)

	return render(
			request,
			"blog/article/category_archive.html",
			{
				"articles" : articles,
				"archive_dates" : archive_dates,
				"categories" : allCategory,
				"category" : category,
				"totalNum" : totalNum
				}
			)
