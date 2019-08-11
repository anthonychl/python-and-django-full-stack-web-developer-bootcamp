from django.db import models
from django.utils.text import slugify # allows to remove chars that arent alphanumeric, swap 'spaces' for dashes (-), lowercase strings, set up that string basically so it can be used as a url
import misaka # allows link embedding, markdown text, misaka needs to be pip installed (requires VS C++ v14, and Win10 SDK)
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library() # this allows to use later get_ to fetch user_groups from GroupMember

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    slug = models.SlugField(allow_unicode=True, unique = True)
    description = models.TextField(blank=True,default= '')
    description_html = models.TextField(editable=False, default='',blank=True )
    members = models.ManyToManyField(User, through= 'GroupMember')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug':self.slug} )

    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name = 'memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name = 'user_groups', on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ('group', 'user')



