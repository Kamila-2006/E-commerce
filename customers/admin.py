from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'address', 'created_at', 'updated_at')
    search_fields = ('user__name', 'phone', 'address')