from django.contrib import admin

from .models import User,LateNight,EarlyMorning,OverNight

# Register your models here.
admin .site.register(User)
admin .site.register(LateNight)
admin .site.register(EarlyMorning)
admin .site.register(OverNight)
