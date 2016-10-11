from classytags.helpers import InclusionTag
from cms.models import CMSPlugin
from cms.templatetags.cms_tags import _get_placeholder
from django import template
from sections.models import Section, PortfolioCategory

register = template.Library()


@register.tag(name='section_menu')
class SectionMenu(InclusionTag):
    """
    Show menu from Section objects it active and show_on_menu checked
    """

    template = "templatetags/section_menu.html"
    name = "section_menu"

    def get_context(self, context, **kwargs):
        request = context['request']
        page = request.current_page
        sections = []
        placeholder = _get_placeholder(page, page, context, "homepage_content")
        objects = placeholder.get_plugins_list()
        for obj in objects:
            if isinstance(obj, CMSPlugin):
                plugin = obj
                instance, plugin = plugin.get_plugin_instance()
                if isinstance(instance, Section) and instance.active and instance.show_on_menu:
                    sections.append(instance)
        return {
            'sections': sections
        }


@register.tag(name='portfolio_categories')
class PortfolioCategories(InclusionTag):
    """
    Show menu from Section objects it active and show_on_menu checked
    """

    template = "templatetags/portfolio_categories.html"
    name = "categories"

    def get_context(self, context, **kwargs):
        return {
            'categories': PortfolioCategory.objects.all()
        }


@register.filter(name='chunks')
def chunks(iterable, chunk_size):
    if not hasattr(iterable, '__iter__'):
        # can't use "return" and "yield" in the same function
        yield iterable
    else:
        i = 0
        chunk = []
        for item in iterable:
            chunk.append(item)
            i += 1
            if not i % chunk_size:
                yield chunk
                chunk = []
        if chunk:
            # some items will remain which haven't been yielded yet,
            # unless len(iterable) is divisible by chunk_size
            yield chunk
