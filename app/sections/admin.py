from django.contrib import admin

from sections.models import PortfolioCategory


class PortfolioCategoryAdmin(admin.ModelAdmin):
    model = PortfolioCategory

admin.site.register(PortfolioCategory, PortfolioCategoryAdmin)
