from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'student_name',
        'resource_name',
        'booking_date',
        'booking_time',
        'status',
    )
    list_editable = ('status',)
