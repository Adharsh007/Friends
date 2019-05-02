from django.contrib import admin
from testapp.models import *

# Register your models here.
class loginsAdmin(admin.ModelAdmin):
    list_display = ['username','password','role']
admin.site.register(logins,loginsAdmin)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ['ids','Collegeid','Name','Designation','Department','Dob','Email','Mobile']
admin.site.register(Register,RegisterAdmin)

class nurseAdmin(admin.ModelAdmin):
    list_display = ['ids','nurseid','name','gender','dob','email','address','mobile','qualification','experience','image']
admin.site.register(nurse,nurseAdmin)

class doctorsAdmin(admin.ModelAdmin):
    list_display = ['ids','doctorsid','name','gender','dob','email','address','mobile','qualification','experience','photo']
admin.site.register(doctors,doctorsAdmin)

class medicineAdmin(admin.ModelAdmin):
    list_display = ['medicineid','medicinename','suppliername','place','date','billno','quantity','amount']
admin.site.register(medicine,medicineAdmin)

class equipmentAdmin(admin.ModelAdmin):
    list_display = ['equipmentid','equipmentname','suppliername','place','date','billno','quantity','amount']
admin.site.register(equipment,equipmentAdmin)

class stockAdmin(admin.ModelAdmin):
    list_display = ['medicineid','medicinename','quantity','amount']
admin.site.register(stock,stockAdmin)

class feedbacksAdmin(admin.ModelAdmin):
    list_display = ['fimd','name','comment']
admin.site.register(feedbacks,feedbacksAdmin)

class questionAdmin(admin.ModelAdmin):
    list_display = ['ids','Collegeid','Name','did','question','response','status']
admin.site.register(question,questionAdmin)

class case_historyAdmin(admin.ModelAdmin):
    list_display = ['username','ids','Name','Diagnosis','clinicalhistory','treatment']
admin.site.register(case_history,case_historyAdmin)

class doctor_responseAdmin(admin.ModelAdmin):
    list_display = ['s_id','q_id','do_response']
admin.site.register(doctor_response,doctor_responseAdmin)

class request_appointmsAdmin(admin.ModelAdmin):
    list_display = ['ids','reason','appointdate']
admin.site.register(request_appointms,request_appointmsAdmin)

class student_feedbackAdmin(admin.ModelAdmin):
    list_display=['student_name','feedback']
admin.site.register(student_feedback,student_feedbackAdmin)
