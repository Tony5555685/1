from django.contrib import admin
from hotelapi.models import booking,users
# Register your models here.
class usersAdmin(admin.ModelAdmin):
    list_display=('uid','created_time')
admin.site.register(users,usersAdmin)
class bookingAdmin(admin.ModelAdmin):
    list_display=('bid','roomtype','roomamount',  'datein', 'dateout' )
admin.site.register(booking,bookingAdmin)
