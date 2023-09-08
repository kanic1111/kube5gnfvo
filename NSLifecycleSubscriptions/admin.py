from django.contrib import admin
from NSLifecycleSubscriptions.models import *
# Register your models here.
admin.site.register(LccnSubscription)
admin.site.register(LccnSubscriptionLink)
admin.site.register(LifecycleChangeNotificationsFilter)
admin.site.register(NsInstanceSubscriptionFilter)

