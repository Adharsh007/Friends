from datetime import datetime

from django.db import models
# Create your models here.
class logins(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    role=models.CharField(max_length=50)

    def __str__(self):
        return  self.username



class Register(models.Model):
    ids=models.ForeignKey(logins,on_delete=models.CASCADE)
    Collegeid=models.CharField(unique=True,max_length=30)
    Name=models.CharField(max_length=50)
    Designation=models.CharField(max_length=50)
    Department=models.CharField(max_length=50,)
    Dob = models.DateField()
    Email=models.EmailField()
    Mobile=models.CharField(max_length=50)

    def __str__(self):
        return self.Name



class nurse(models.Model):
    ids = models.ForeignKey(logins, on_delete=models.CASCADE)
    nurseid=models.CharField(unique=True,max_length=30)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=30)
    dob=models.DateField()
    email=models.EmailField()
    address=models.CharField(max_length=100)
    mobile=models.CharField(max_length=50)
    qualification=models.CharField(max_length=30)
    experience=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images')

    def __str__(self):
        return  self.name



class doctors(models.Model):
    ids = models.ForeignKey(logins, on_delete=models.CASCADE)
    doctorsid=models.CharField(unique=True,max_length=30)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    dob = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)
    qualification = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name



class medicine(models.Model):
    medicineid=models.CharField(unique=True,max_length=40)
    medicinename=models.CharField(max_length=200)
    suppliername=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    date=models.DateField()
    billno=models.CharField(max_length=50)
    quantity=models.IntegerField()
    amount=models.IntegerField()

    def __str__(self):
        return self.medicinename



class equipment(models.Model):
    equipmentid=models.CharField(unique=True,max_length=40)
    equipmentname=models.CharField(max_length=100)
    suppliername=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    date=models.DateField()
    billno=models.CharField(max_length=50)
    quantity = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return self.equipmentname



class stock(models.Model):
    #idm=models.ForeignKey(medicine,on_delete=models.CASCADE)
    medicineid = models.CharField(unique=True, max_length=40)
    medicinename = models.CharField(max_length=200)
    quantity = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return  self.medicinename



class feedbacks(models.Model):
    fimd=models.IntegerField()
    name=models.CharField(max_length=100)
    comment=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class question(models.Model):
    ids=models.ForeignKey(logins,on_delete=models.CASCADE)
    Collegeid = models.CharField(max_length=30)
    Name = models.CharField(max_length=50)
    did=models.ForeignKey(doctors,on_delete=models.CASCADE)
    question=models.CharField(max_length=500)
    response=models.CharField(max_length=500)
    status=models.CharField(max_length=50)

    def __str__(self):
        return self.Name

#model for storing patients details from doctor side
class case_history(models.Model):
    username = models.ForeignKey(logins,on_delete=models.CASCADE)
    ids = models.ForeignKey(doctors,on_delete=models.CASCADE)
    Name = models.ForeignKey(Register, on_delete=models.CASCADE)
    Diagnosis = models.TextField()
    clinicalhistory = models.TextField()
    treatment = models.TextField()

#model for providing response from the doctor
class doctor_response(models.Model):
    s_id=models.ForeignKey(logins,on_delete=models.CASCADE)
    q_id=models.ForeignKey(question,on_delete=models.CASCADE)
    do_response = models.TextField()
#model for storing requests from students to nurse
class request_appointms(models.Model):
    ids=models.ForeignKey(logins,on_delete=models.CASCADE)
    reason=models.TextField()
    appointdate=models.DateTimeField(default=datetime.now,blank=True)

#sending feedback from student to admin about the system
class student_feedback(models.Model):
    student_name = models.ForeignKey(Register,on_delete=models.CASCADE)
    feedback = models.TextField()
