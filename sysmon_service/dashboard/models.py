from django.db import models

# Create your models here.

class UserAccount(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    last_login_date = models.DateTimeField(null = True)

    def __str__(self):
        return self.username
    
class TimeUsage(models.Model):
    useraccount = models.ForeignKey(UserAccount, on_delete = models.CASCADE)
    date = models.DateField(auto_now_add = True)
    usage_json = models.JSONField(default = dict)
    previous_app = models.CharField(max_length = 500, default = None, null = True)
    previous_url = models.CharField(max_length = 2000, default = None, null = True)


