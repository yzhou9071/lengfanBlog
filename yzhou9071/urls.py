from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from blog.views import index

admin.autodiscover()

urlpatterns = patterns('',
		url(
			r'^static/(?P<path>.*)$', 
			'django.views.static.serve',	
			{'document_root':settings.STATIC_ROOT}
			),

		#admin urls
		url(
			r'^admin/', 
			include(admin.site.urls)
			),

		#blog urls
		url(
			r'^$', 
			index,
			name="home"
			),

		url(
			'^blog/$', 
			'blog.views.index', 
			name="blog_article_index"
			),
		url(
			'^blog/archive/(?P<slug>[-\w]+)/$', 
			'blog.views.category_archive', 
			name="blog_category_archive"
			),
		url(
			'^blog/(?P<slug>[-\w]+)/$', 
			'blog.views.single', 
			name="blog_article_single"
			),

		#about urls
		url(
			'^about/$', 
			'about.views.index', 
			name="about_index"
			),
		url(
			'^about/updateAboutDetailNum/*', 
			'about.views.updateAboutDetailNum', 
			),

		#book urls
		url(
			'^books/$', 
			'books.views.index', 
			name="books_index"
			),

		#photo urls
		url(
			'^photos/$', 
			'photos.views.index', 
			name="photos_index"
			),

		#repo urls
		url(
			'^repos/$', 
			'repos.views.index', 
			name="repos_index"
			),

		)
