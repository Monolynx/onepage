from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from sections.models import Section, Service, Portfolio, PortfolioItem, PortfolioCategory


class WidgetPluginBase(CMSPluginBase):
    module = 'Widgets'
    cache = True

    def render(self, context, instance, placeholder):
        context[self.code] = instance
        return context


class SectionPlugin(WidgetPluginBase):
    model = Section
    name = _('Section')
    code = 'section'
    allow_children = True
    child_classes = ['ServicePlugin', 'PortfolioPlugin']
    render_template = 'widgets/section.html'

plugin_pool.register_plugin(SectionPlugin)


class ServicePlugin(WidgetPluginBase):
    name = _('Service Section')
    code = 'service'
    require_parent = True
    parent_classes = ['SectionPlugin']
    allow_children = True
    child_classes = ['ServiceItemPlugin']
    render_template = 'widgets/service.html'

plugin_pool.register_plugin(ServicePlugin)


class ServiceItemPlugin(WidgetPluginBase):
    model = Service
    name = _('Service Item')
    code = 'service_item'
    require_parent = True
    parent_classes = ['ServicePlugin']
    render_template = 'widgets/service_item.html'

plugin_pool.register_plugin(ServiceItemPlugin)


class PortfolioPlugin(WidgetPluginBase):
    model = Portfolio
    name = _('Portfolio Section')
    code = 'portfolio'
    require_parent = True
    parent_classes = ['SectionPlugin']
    allow_children = True
    child_classes = ['PortfolioItemPlugin']
    render_template = 'widgets/portfolio.html'

    def render(self, context, instance, placeholder):
        context = super(PortfolioPlugin, self).render(context, instance, placeholder)
        context['categories'] = PortfolioCategory.objects.order_by('title')
        return context

plugin_pool.register_plugin(PortfolioPlugin)


class PortfolioItemPlugin(WidgetPluginBase):
    model = PortfolioItem
    name = _('Portfolio Item')
    code = 'portfolio_item'
    require_parent = True
    parent_classes = ['PortfolioPlugin']
    render_template = 'widgets/portfolio_item.html'
    filter_horizontal = ('categories',)

plugin_pool.register_plugin(PortfolioItemPlugin)
