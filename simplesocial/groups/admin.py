from django.contrib import admin

from . import models
# Register your models here.

class GroupMemberInline(admin.TabularInline): 
    model = models.GroupMember
# use a tabularinline class so when we open the admin area
# we can edit the GroupMember model under the Group model
# as if one was parent to the other
# now we dont need to register the GroupMember model only the Group model

admin.site.register(models.Group)