from django import forms
from django.forms import DateInput
from testapp.models import *

class CaseForm(forms.ModelForm):
    class Meta:
        model = case_history
        fields = ['username','Name','ids','Diagnosis','clinicalhistory','treatment']

        labels ={
            "username": "College ID",
            "Name": "Student Name",
            "ids":  "Doctor Name",
            "Diagnosis": "Diagnosis",
            "clinicalhistory": "Clinical history",
            "treatment":"Treatment"

        }
class ResponseForm(forms.ModelForm):
    class Meta:
        model = doctor_response
        fields = ['do_response']

        labels={
            "do_response" : "Provide Response"
        }

class RequestForm(forms.ModelForm):
   class Meta:
        model = request_appointms
        fields = ['reason','appointdate']

        labels= {
            #"ids":"Student Name",
            "reason": "Reason for appointment",
            "appointdate": "Date of appointment"
        }
#desinging form from student_feedback
class student_feedback_form(forms.ModelForm):
    class Meta:
        model = student_feedback
        fields = ['feedback']

        labels = {
            "feedback" : "Give your Feedback"
        }
