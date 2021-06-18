from django import forms
from .models import usage_log,log_entry



# creating_forms
class UsageForm(forms.ModelForm):
    class Meta():
        model = usage_log
        fields = ["User", 'Month', 'Source','Total_calls','First_api_call','Last_api_call','Last_checked_row']

class LogForm(forms.ModelForm):
    class Meta():
        model = log_entry
        Api_url = forms.CharField(max_length=256, required=False)
        Method = forms.CharField(max_length=50, required=False)
        User_email = forms.EmailField(required=False)
        Milliseconds = forms.IntegerField(required=False)
        Code = forms.IntegerField(required=False)
        User_agent = forms.CharField(max_length=256, required=False)
        # Time = forms.DateTimeField(required=False)
        Time = forms.CharField(max_length=256, required=False)
        fields = ['Api_url', 'Method','User_email','Milliseconds','Code','User_agent','Time']
