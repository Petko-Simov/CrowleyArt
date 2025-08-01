from django.contrib import admin

from gallery.models import Tattoo


@admin.register(Tattoo)
class TattooAdmin(admin.ModelAdmin):
    list_display = (
        'tattoo_name',
        'style',
        'artist',
        'added_by',
        'price',
        'created_at',
    )

    list_filter = (
        'style',
        'artist',
        'created_at',
    )

    search_fields = (
        'tattoo_name',
        'style',
        'description',
    )

    ordering = ('-created_at',)

    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('tattoo_name', 'artist', 'image'),
        }),
        ('Details', {
            'fields': ('style', 'description', 'price'),
            'classes': ('collapse',),
        }),
        ('Metadata', {
            'fields': ('added_by', 'created_at'),
        }),
    )
























