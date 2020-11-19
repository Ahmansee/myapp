from django.db import models

# Create your models here.
#class Email_ads(models.Model):
    #email = models.CharFeild(max_length = 55)

class Contact(models.Model):
    name    = models.CharField(max_length = 44, blank = False)
    email   = models.EmailField(max_length = 55, blank = False)
    sms     = models.TextField(max_length = 444, blank = False)
    sent_on = models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self):
        return self.email
    

