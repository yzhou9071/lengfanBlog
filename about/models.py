from django.db import models
from django.utils.translation import ugettext as _

class AboutDownload(models.Model) :
	"""Download Model"""
	downloadTitle = models.CharField(
			verbose_name = _(u'Title'),
			help_text = _(u' '),
			max_length = 255,
			)
	downloadHref = models.CharField(
			verbose_name = _(u'Href'),
			help_text = _(u' '),
			max_length = 255,
			)
	downloadTime = models.DateField(
			verbose_name = _(u'Show Time'),
			help_text = _(u' '),
			)
	downloadNum = models.IntegerField(
			verbose_name = _(u'PV'),
			help_text = _(u' '),
			default = 0
			)

	class Meta:
		app_label = _(u'about')
		verbose_name = _(u"Download")
		verbose_name_plural = _(u"Downloads")
		ordering = ['-downloadTime',]

class AboutAuthorDetail(models.Model) :
	"""AuthorDetail Model"""
	authorDetailDes = models.CharField(
			verbose_name = _(u'Detail Des'),
			help_text = _(u' '),
			max_length = 255,
			)
	authorDetailTime = models.DateField(
			verbose_name = _(u'Show Time'),
			help_text = _(u' '),
			)
	authorDetailFlag = models.IntegerField(
			verbose_name = _(u'Detail Flag'),
			help_text = _(u' '),
			default = 0
			)
	authorDetailHref = models.CharField(
			verbose_name = _(u'Detail Href'),
			help_text = _(u' '),
			max_length = 255,
                        blank = True
			)

	class Meta:
		app_label = _(u'about')
		verbose_name = _(u"AuthorDetail")
		verbose_name_plural = _(u"AuthorDetails")
		ordering = ['-authorDetailTime',]
