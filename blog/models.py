from django.db import models
from django.utils.translation import ugettext as _
from markdown import markdown

class Category(models.Model) :
    """Category Model"""
    categoryID = models.IntegerField(
        verbose_name = _(u'ID'),
        help_text = _(u' '),
		default = 0
    )
    title = models.CharField(
        verbose_name = _(u'Title'),
        help_text = _(u' '),
        max_length = 255
    )
    slug = models.SlugField(
        verbose_name = _(u'Slug'),
        help_text = _(u'Uri identifier.'),
        max_length = 255,
        unique = True
    )

    class Meta:
        app_label = _(u'blog')
        verbose_name = _(u"Category")
        verbose_name_plural = _(u"Categories")
        ordering = ['categoryID',]

    def __unicode__(self):
        return "%s" % (self.title,)

class Article(models.Model) :
    """Article Model"""
    title = models.CharField(
        verbose_name = _(u'Title'),
        help_text = _(u' '),
        max_length = 255
    )
    slug = models.SlugField(
        verbose_name = _(u'Slug'),
        help_text = _(u'Uri identifier.'),
        max_length = 255,
        unique = True
    )
    tags = models.CharField(
        verbose_name = _(u'Tags'),
        help_text = _(u' '),
        max_length = 255
    )
    content_markdown = models.TextField(
        verbose_name = _(u'Content (Markdown)'),
        help_text = _(u' '),
    )
    content_markup = models.TextField(
        verbose_name = _(u'Content (Markup)'),
        help_text = _(u' '),
    )
    categories = models.ManyToManyField(
        Category,
        verbose_name = _(u'Categories'),
        help_text = _(u' '),
        null = True,
        blank = True
    )
    pv = models.IntegerField(
        verbose_name = _(u'PV'),
        help_text = _(u' '),
		default = 0
    )
    publishDate = models.DateField(
        verbose_name = _(u'Publish Date'),
        help_text = _(u' '),
		auto_now_add = True
    )
    publishTime = models.DateTimeField(
        verbose_name = _(u'Publish Time'),
        help_text = _(u' '),
		auto_now_add = True
    )
    editTime = models.DateTimeField(
        verbose_name = _(u'Edit Time'),
        help_text = _(u' '),
		auto_now = True
    )

    class Meta:
        app_label = _(u'blog')
        verbose_name = _(u"Article")
        verbose_name_plural = _(u"Articles")
        ordering = ['-publishTime']

    def save(self):
        self.content_markup = markdown(self.content_markdown, ['codehilite'])
        super(Article, self).save()

    def __unicode__(self):
        return "%s" % (self.title,)
