from django.contrib import admin
from subscription.models import Subscription
import datetime

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'subscribed_today')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email')
    list_filter = ['created_at']

    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.date.today()

    subscribed_today.short_description = 'Subscribed today?'
    subscribed_today.boolean = True


admin.site.register(Subscription, SubscriptionAdmin)
