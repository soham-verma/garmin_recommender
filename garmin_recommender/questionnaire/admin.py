from django.contrib import admin
from .models import GarminWatch

@admin.register(GarminWatch)
class GarminWatchAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "fitness_tracking", "gps", "touchscreen", "battery_life")
    list_filter = ("fitness_tracking", "gps", "touchscreen", "rugged")
    search_fields = ("name", "description")
