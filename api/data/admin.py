from django.contrib import admin

from data import models


@admin.register(models.Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ('year',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('year',)


@admin.register(models.Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'unit')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('code', 'name', 'unit')


@admin.register(models.Program)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('prog', 'subp', 'proy', 'subpr', 'name')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(models.Rec)
class RecAdmin(admin.ModelAdmin):
    list_display = ('rec',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('rec',)


@admin.register(models.Sit)
class SitAdmin(admin.ModelAdmin):
    list_display = ('sit',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('sit',)


@admin.register(models.Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(models.Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'approval_init', 'approval_current', 'commitments', 'obligations',
        'payments'
    )
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('year',)
