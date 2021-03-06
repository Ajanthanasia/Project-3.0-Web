from django.contrib import admin
from django.utils import timezone
from .models import review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','qa','hotel','device_signature','created_at','updated_at')
    date_hierarchy = 'created_at'
    list_filter = ('created_at','updated_at')

    """"def days_since_creation(self,review):
        diff = timezone.now() - review.created_at
        return diff.days
    days_since_creation.short_description = 'Days Active'"""

admin.site.register(review,ReviewAdmin)