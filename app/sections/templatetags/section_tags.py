from classytags.helpers import InclusionTag
from cms.models import CMSPlugin
from cms.templatetags.cms_tags import _get_placeholder
from django import template
from sections.models import Section

register = template.Library()


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


register.tag(SectionMenu)
