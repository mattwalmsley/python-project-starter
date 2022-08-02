from django.contrib import admin

# Register your models here.
from .models import AnalyseMatches

# create a class for the admin-model integration
class AnalyseMatchesAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = ("name", "preference1", "preference2", "preference3")


# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(AnalyseMatches, AnalyseMatchesAdmin)
