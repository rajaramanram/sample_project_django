from django.db import models


# Create your models here.
class usage_log(models.Model):
    user_id = models.AutoField(primary_key=True)
    User = models.CharField(max_length=256)
    #Month = models.DateField()
    Month = models.CharField(max_length=256)
    Source = models.CharField(max_length=256)
    Total_calls = models.IntegerField()
    #First_api_call = models.DateTimeField()
    First_api_call = models.CharField(max_length=256)
    #Last_api_call = models.DateTimeField()
    Last_api_call = models.CharField(max_length=256)
    Last_checked_row = models.IntegerField()

class log_entry(models.Model):
    #user_log_id = models.ForeignKey(usage_log, on_delete=models.CASCADE)
    Api_url = models.CharField(max_length=256)
    Method = models.CharField(max_length=50)
    User_email = models.EmailField()
    Milliseconds = models.IntegerField()
    Code = models.IntegerField()
    User_agent = models.CharField(max_length=256)
    #Time = models.DateTimeF ield()
    Time = models.CharField(max_length=256)
