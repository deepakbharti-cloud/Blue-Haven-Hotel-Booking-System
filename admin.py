from django.contrib import admin
from .models import Hotel, Room, Review
class RoomInline(admin.TabularInline): model=Room; extra=0
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin): list_display=('name','city','owner','approved'); list_filter=('approved','city'); search_fields=('name','city'); inlines=[RoomInline]
admin.site.register(Room)
admin.site.register(Review)
