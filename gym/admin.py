from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Coach, Gym, Service, Pricing, Gallery


@admin.register(Coach)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url", "get_image")
    list_display_links = ("name",)
    list_filter = ("specialization",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="60"')

    get_image.short_description = "Изображение"

@admin.register(Gym)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_image")
    list_display_links = ("name",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="70" height="50"')

    get_image.short_description = "Изображение"


@admin.register(Service)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_image")
    list_display_links = ("name",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="70" height="50"')

    get_image.short_description = "Изображение"

@admin.register(Pricing)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")
    list_display_links = ("name",)


@admin.register(Gallery)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_image")
    list_display_links = ("name",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="70" height="50"')

    get_image.short_description = "Изображение"
