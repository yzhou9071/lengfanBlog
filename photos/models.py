from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
class PhotoList(models.Model) :
    """PhotoList Model"""
    photoTime = models.DateTimeField(
        verbose_name = _(u'Photo Time'),
		auto_now_add = True
    )
    photoTitle = models.CharField(
        verbose_name = _(u'Photo Title'),
        max_length = 255
    )
    photoDes = models.CharField(
        verbose_name = _(u'Photo Des'),
        max_length = 255
    )

    class Meta:
        app_label = _(u'photos')
        verbose_name = _(u"Photo")
        verbose_name_plural = _(u"Photos")
        ordering = ['-photoTime',]
