from django.contrib import admin

# Register your models here.
from .models import Intern
from .models import Buddy

# create a class for the admin-model integration
class InternAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = (
        "name",
        "university",
        "course",
        "LoB",
        "location",
        "interest1",
        "interest2",
        "interest3",
        "programming1",
        "programming2",
        "request_time"
    )


class BuddyAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = (
        "name",
        "university",
        "course",
        "LoB",
        "location",
        "interest1",
        "interest2",
        "interest3",
        "programming1",
        "programming2",
        "time_available"
    )

# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Intern, InternAdmin)
admin.site.register(Buddy, BuddyAdmin)
