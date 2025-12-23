from django import forms
from .models import Job,Application,Worker

class AdsEmployer(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('category', 'title', 'description', 'salary', 'location', 'phone_number',)



# class EmloyerProfileForm(forms.ModelForm):
#     class Meta:
#         model = EmployerProfile
#         fields = ('company_name',)


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('message',)


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ('full_name', 'profession', 'bio', 'location', 'phone_number',)