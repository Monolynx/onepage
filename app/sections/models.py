from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField

from app import settings


class WidgetAbstract(CMSPlugin):

    def __str__(self):
        return u'{0}'.format(self.pk)

    class Meta:
        abstract = True


class BaseAbstract(WidgetAbstract):
    title = models.CharField(_('Title'), max_length=31, null=False, blank=False)
    content = models.CharField(_('Content'), max_length=1023, null=False, blank=False)
    image = FilerImageField(null=False, default='')

    def __str__(self):
        return u'{0}'.format(self.title)

    class Meta:
        abstract = True


class Section(WidgetAbstract):
    title = models.CharField(_('Title'), max_length=63, null=False, blank=False)
    slug = models.SlugField(max_length=63)
    content = models.TextField(null=True, blank=True)
    template = models.CharField(max_length=1023, null=True, blank=True, choices=settings.SECTION_TEMPLATES)
    show_on_menu = models.BooleanField(_('Show on menu'), null=False, blank=False, default=True)
    show_title_on_section = models.BooleanField(_('Show title on section'), null=False, blank=False, default=True)
    active = models.BooleanField(_('Active'), null=False, blank=False, default=True)

    def __str__(self):
        return u'{0}'.format(self.title)

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')


class SectionItem(BaseAbstract):
    template = models.CharField(max_length=1023, null=False, blank=False, choices=settings.SECTION_ITEM_TEMPLATES)

    class Meta:
        verbose_name = _('Section Item (title, content, image)')
        verbose_name_plural = _('Section Items')


class PortfolioCategory(models.Model):
    title = models.CharField(_('Title'), max_length=63, null=False, blank=False)

    def __str__(self):
        return u'{0}'.format(self.title)

    class Meta:
        verbose_name = _('Portfolio Category')
        verbose_name_plural = _('Portfolio Categories')


class Portfolio(BaseAbstract):
    categories = models.ManyToManyField(PortfolioCategory, verbose_name=_('Categories'), null=False, blank=False)

    def copy_relations(self, oldinstance):
        self.categories = oldinstance.categories.all()

    class Meta:
        verbose_name = _('Portfolio')
        verbose_name_plural = _('Portfolios')
