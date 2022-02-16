from django.contrib import admin

from .models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    search_fields = ["modelo"]
    list_display = (
        "id",
        "marca",
        "modelo",
        "tipo_car",
        "cor",
        "ano",
        "created_at",
        "modified_at",
    )


admin.site.register(Car, CarAdmin)
