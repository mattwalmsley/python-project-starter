from django.contrib import admin

# Register your models here.
from .models import Intern

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
        "programming 1",
        "programming 2",
        "request_time"
    )

# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Intern, InternAdmin)
