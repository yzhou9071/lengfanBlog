from django.db import models
from django.utils.translation import ugettext as _

class BookDetail(models.Model) :
	"""Book Detail Model"""
	bookName = models.CharField(
			verbose_name = _(u'Book Name'),
			help_text = _(u' '),
			max_length = 255,
			)
	bookAuthor = models.CharField(
			verbose_name = _(u'Book Author'),
			help_text = _(u' '),
			max_length = 255,
			)
	bookProduct = models.CharField(
			verbose_name = _(u'Book Product'),
			help_text = _(u' '),
			max_length = 255,
			)
	bookDes = models.TextField(
			verbose_name = _(u'Book Des'),
			help_text = _(u' '),
			)
	bookStar = models.CharField(
			verbose_name = _(u'Book Star'),
			help_text = _(u' '),
			max_length = 255,
			)
	bookState = models.IntegerField(
			verbose_name = _(u'Book State'),
			help_text = _(u' '),
			default = 0
			)
	bookFlag = models.BooleanField(
			verbose_name = _(u'Book Flag'),
			help_text = _(u' '),
			default = False
			)
	bookHref = models.CharField(
			verbose_name = _(u'Book Href'),
			help_text = _(u' '),
			max_length = 255,
			blank = True
			)
	bookTime = models.DateTimeField(
			verbose_name = _(u'Collect Time'),
			help_text = _(u' '),
			auto_now_add = True
			)

	class Meta:
		app_label = _(u'books')
		verbose_name = _(u"bookDetail")
		verbose_name_plural = _(u"booksDetail")
		ordering = ['-bookTime',]
