from django.db import models
from django.contrib.auth.models import User
from .role import Role

class UserProfile(models.Model):

    DEFAULT_EXAM_ID = 1

    user = models.ForeignKey(to=User)
    #profile_pic = models.ForeignKey(to=Image,blank=True,null=True)
    email_varified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    user_role = models.ForeignKey(to=Role, default=DEFAULT_EXAM_ID)

    

    def __unicode__(self):
        return self.user.username

    def to_dct(self):
        dct = {}
        dct['userprofile_id'] = self.id
        #dct['profile_pic'] = '/media/' + str(self.profile_pic.image_path) if self.profile_pic != None else ''
        dct['is_email_varified'] = self.email_varified
        dct['username'] = self.user.username
        dct['email'] = self.user.email
        dct['first_name'] = self.user.first_name
        dct['last_name'] = self.user.last_name
        return dct
