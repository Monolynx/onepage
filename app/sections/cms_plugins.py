from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from sections.models import Section, Portfolio, SectionItem


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
    child_classes = ['SectionItemPlugin', 'PortfolioItemPlugin', 'CMSContactPlusPlugin']
    render_template = 'widgets/section.html'

    def get_render_template(self, context, instance, placeholder):
        return instance.template or self.render_template

plugin_pool.register_plugin(SectionPlugin)


class SectionItemPlugin(WidgetPluginBase):
    model = SectionItem
    name = _('Section Item')
    code = 'item'
    require_parent = True
    parent_classes = ['SectionPlugin']
    render_template = 'widgets/service_item.html'

    def get_render_template(self, context, instance, placeholder):
        return instance.template or self.render_template

plugin_pool.register_plugin(SectionItemPlugin)


class PortfolioItemPlugin(WidgetPluginBase):
    model = Portfolio
    name = _('Portfolio Item')
    code = 'portfolio_item'
    require_parent = True
    parent_classes = ['SectionPlugin']
    render_template = 'widgets/portfolio_item.html'
    filter_horizontal = ('categories',)

plugin_pool.register_plugin(PortfolioItemPlugin)
