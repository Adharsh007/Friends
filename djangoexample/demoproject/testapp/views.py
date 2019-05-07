from django.contrib.auth import logout
from django.core.mail import send_mail
from django.db import connection
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.template import loader, Context
from testapp.forms import *
from testapp.models import  *
from testapp import config
from .models import *
#from django.db import connection


def hello_view(request):
    return render(request,'index.html')
def log(request):
    return render(request,'login.html')
def reg(request):
    return render(request,'register.html')
def saw(request):
    return render(request,'admin/homepage.html')
def nur(request):
    return render(request,'admin/addnurse.html')
def doc(request):
    return render(request,'admin/adddoctor.html')
def docto(request):
    return render(request,'doctor/doctorhomepage.html')
def nurs(request):
    return render(request,'nurse/nursehomepage.html')
def users(request):
    return render(request,'users/patienthomepage.html')
def med(request):
    return render(request,'admin/medicineadd.html')
def equipadd(request):
    return render(request,'admin/equipmentadd.html')
def response_send(request):
    return render(request,'doctor/responsepage.html')

#function for student/faculty registration
def add(request):
     if request.method=='POST':
       collegid=request.POST.get('cid')
       fullname=request.POST.get('name')
       des=request.POST.get('desi')
       dep=request.POST.get('dept')
       dateob=request.POST.get('dates')
       emails=request.POST.get('email')
       mobile=request.POST.get('mobile')
       passwords=request.POST.get('password')
       objs = logins()
       objs.username = collegid
       objs.password = passwords
       objs.role = des
       objs.save()
       obj=Register()
       obj.Collegeid=collegid
       obj.Name= fullname
       obj.Designation=des
       obj.Department=dep
       obj.Dob=dateob
       obj.Email=emails
       obj.Mobile=mobile
       obj.ids = objs
       obj.save()

       return render(request,'login.html')

     else:
         return render(request,'register.html')
# function to add nurse by admin
def nursereg(request):
    if request.method=='POST':
        nursid=request.POST.get('nid')
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        dob=request.POST.get('dates')
        email=request.POST.get('email')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        qualifi=request.POST.get('quai')
        experi=request.POST.get('experi')
        image=request.FILES['image']
        objs = logins()
        objs.username = email
        objs.password = email
        objs.role='nurse'
        objs.save()
        objec=nurse()
        objec.nurseid=nursid
        objec.name=name
        objec.gender= gender
        objec.dob=dob
        objec.email=email
        objec.address=address
        objec.mobile= mobile
        objec.qualification=qualifi
        objec.experience=experi
        objec.image=image
        objec.ids = objs
        objec.save()
        subject="Account created"
        message="account for demoproject is created\nlogindetails\n username:",objs.username,"\npassword:",objs.username
        frommail="nigyantony96@gmail.com"
        send_mail(subject,message,frommail,[objs.username],fail_silently=False)
        return render(request, 'homepage.html')

    else:
         return render(request, 'addnurse.html')
#function to add doctor by admin
def doct(request):
    if request.method == 'POST':
        doctorid=request.POST.get('doid')
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        dob=request.POST.get('dates')
        email=request.POST.get('email')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        qualification=request.POST.get('quali')
        experience=request.POST.get('experi')
        image_doc=request.FILES['image']
        objs = logins()
        objs.username = email
        objs.password = email
        objs.role='doctor'
        objs.save()
        objt=doctors()
        objt.doctorsid=doctorid
        objt.name=name
        objt.gender=gender
        objt.dob=dob
        objt.email=email
        objt.address=address
        objt.mobile=mobile
        objt.qualification=qualification
        objt.experience=experience
        objt.photo=image_doc
        objt.ids=objs
        objt.save()
        subject = "Account created"
        message = "account for demoproject is created\nlogindetails\n username:", objs.username, "\npassword:", objs.username
        frommail = "nigyantony96@gmail.com"
        send_mail(subject, message, frommail, [objs.username], fail_silently=False)
        return render(request, 'homepage.html')

    else:
        return render(request, 'adddoctor.html')
# function for login
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('usern')
        password = request.POST.get('password')
        if (logins.objects.filter(username=username,password=password).exists()):
            log = logins.objects.filter(username=username,password=password)

            for value in log:
                userid = value.id
                config.userid = value.id
                print("printing config value")
                print(config.userid)
                request.session['mid'] = userid
                print(userid)
                usertype = value.role
                if usertype=='nurse':
                    Role=request.session['mid']
                    return render(request,'nurse/nursehomepage.html',{'user': Role, 'id': userid})
                elif usertype=='admin':
                    Role = request.session['mid']
                    return render(request, 'admin/homepage.html',{'user':Role,'id':userid})
                elif usertype=='doctor':
                    Role = request.session['mid']
                    return render(request, 'doctor/doctorhomepage.html', {'user': Role, 'id': userid})
                elif usertype=='student':
                    Role = request.session['mid']
                    return render(request, 'users/patienthomepage.html',{'user': Role, 'id': userid,'key':userid})
                elif usertype=='faculty':
                    Role = request.session['mid']
                    return render(request, 'users/patienthomepage.html',{'user': Role, 'id': userid,'key':userid})
                else:
                    context = {"error":"Incorrect Username and Password"}
                    return render(request, "index.html",context)
        else:
            context = {"error": "Incorrect Username and Password"}
            return render(request, "login.html", context)

    else:
        templates = loader.get_template("login.html")
        context = {}
        return HttpResponse(templates.render(context, request))
# function for logout
def signout(request):
    del request.session['mid']
    logout(request)
    return redirect('index')
#function to add medicine by admin
def medic(request):
    if request.method == 'POST':
        medid = request.POST.get('mid')
        medicinenames=request.POST.get('mname')
        suppliernames=request.POST.get('sname')
        places=request.POST.get('place')
        datet=request.POST.get('dates')
        billnos=request.POST.get('billno')
        quantitys=request.POST.get('quant')
        amounts=request.POST.get('amount')
        objm=medicine()
        objm.medicineid=medid
        objm.medicinename=medicinenames
        objm.suppliername=suppliernames
        objm.place=places
        objm.date=datet
        objm.billno=billnos
        objm.quantity=quantitys
        objm.amount=amounts
        objm.save()
        objc = stock()
        objc.medicineid = medid
        objc.medicinename = medicinenames
        objc.quantity = quantitys
        objc.amount = amounts
        #objc.idm  =objm
        objc.save()
        return render(request, 'admin/homepage.html')

    else:
        return render(request, 'medicineadd.html')

# function to add equipments by admin
def equp(request):
    if request.method == 'POST':
        equid=request.POST.get('eid')
        eqname=request.POST.get('ename')
        suppname=request.POST.get('suname')
        place=request.POST.get('place')
        date=request.POST.get('dates')
        bino=request.POST.get('billno')
        quanti=request.POST.get('quants')
        amout=request.POST.get('amot')
        obts=equipment()
        obts.equipmentid=equid
        obts.equipmentname=eqname
        obts.suppliername=suppname
        obts.place=place
        obts.date=date
        obts.billno=bino
        obts.quantity=quanti
        obts.amount=amout
        obts.save()
        return render(request, 'admin/homepage.html')

    else:
        return render(request, 'equipmentadd.html')
# function to take student profile to form
def pofiles(request):
    cursor = connection.cursor()
    list = []
    sql = "select * from testapp_register where ids_id='%s'" % (request.session['mid'])
    cursor.execute(sql)
    result1 = cursor.fetchall()
    for row1 in result1:
        dict = {'Collegeid': row1[1], 'Name': row1[2], 'Designation': row1[3], 'Dob': row1[4],
                'Email': row1[5], 'Mobile': row1[6],'Department':row1[8]}
        list.append(dict)
    return render(request, 'users/profileview.html', {'list': list})

    #function to edit student details
def edit(request):
    if request.method == 'POST':
        cursor=connection.cursor()
        collegid = request.POST.get('cid')
        fullname = request.POST.get('name')
        des = request.POST.get('desi')
        dept=request.POST.get('dept')
        emails = request.POST.get('email')
        mobile = request.POST.get('mobile')
        sql="update testapp_register set Collegeid='%s',Name='%s',Designation='%s',Department='%s',Email='%s',Mobile='%s' where id='%s'" %(collegid,fullname,des,dept,emails,mobile,request.session['mid'])
        cursor.execute(sql)
        html = "<script>alert('successfully changed! ');window.location='/patienthomepage/';</script>"
        return HttpResponse(html)
    return render(request,'users/patienthomepage.html')
    #function to take nurse profile to form
def nurseprofi(request,id):
    data=Register.objects.get(ids_id=id)
    return render(request,'nurse/nursepofile.html',{'data':data})
#function to take student data to form
def feed(request,id):
    data=Register.objects.get(ids_id=id)
    return render(request,'users/feedback.html',{'data':data})
#function to send feedback to admin by student
def feedbak(request,id):
    if request.method == 'POST':
        #key=request.session['Role']
        data=Register.objects.get(ids_id=id)
        obts = feedbacks()
        obts.name=data.Name
        comment=request.POST.get('comments')
        obts.comment=comment
        obts.fimd=data.ids_id
        key=obts.fimd
        obts.save()
        return render(request,'users/patienthomepage.html',{'key':key})
  #function to see feedback from students in admin side
def feedbackuser(request):
    data=Register.objects.all()
    data1=feedbacks.objects.all()
    return render(request,'admin/feedbackuser.html',{'data':data,'data1':data1})
#function to see nurselist by admin and to perform operations
def viewnurse(request):
    data=nurse.objects.all()
    return render(request,'admin/nurselist.html',{'data':data})
#function to see medicinelist by admin and to perform operations
def viewmedicine(request):
    data=medicine.objects.all()
    return render(request,'admin/medicinelist.html',{'data':data})
#function to see equipmentlist by admin and to perform operations
def viewequip(request):
    data=equipment.objects.all()
    return render(request,'admin/equipmentlist.html',{'data':data})
#function to see doctorlist by admin and to perform operations
def viewdoctor(request):
    data=doctors.objects.all()
    return render(request,'admin/doctorslist.html',{'data':data})
#function to take doctordetails to studentpage for sending questions
def questi(request):
    data=doctors.objects.all()
    return render(request,'users/questions.html',{'data':data})
#function to send questions to a particular doctor by a particular student
def questo(request):
     if request.method=='POST':
        rid=request.session['mid']
        data=Register.objects.get(ids=rid)
        data1 = logins.objects.get(id=rid)
        did=request.POST.get('doctor')
        data2=doctors.objects.get(id=did)
        qu=request.POST.get('questions')
        obst=question()
        obst.did=data2
        obst.question=qu
        obst.Collegeid=data.Collegeid
        obst.Name=data.Name
        obst.response=''
        obst.status=''
        obst.ids=data1
        obst.save()
        return render(request,'users/patienthomepage.html')
#function to delete a particular doctor by admin
def prodel(request,id):
    if (doctors.objects.filter(id=id).exists()):
        data = doctors.objects.get(id=id)
        data2=logins.objects.get(username=data.email)
        data2.delete()
        data.delete()
        return render(request, 'admin/homepage.html')
    else:
        return render(request, 'admin/doctorslist.html')
#function to delete a particular nurse by admin
def pp(request,id):
    if (nurse.objects.filter(id=id).exists()):
        data = nurse.objects.get(id=id)
        data2=logins.objects.get(username=data.email)
        data2.delete()
        data.delete()
        return render(request, 'admin/homepage.html')
    else:
        return render(request, 'admin/nurselist.html')
# function to delete a particular medicine by admin
def medde(request,id):
    if (medicine.objects.filter(id=id).exists()):
        data = medicine.objects.get(id=id)
        data2=stock.objects.get(id=data.id)
        data2.delete()
        data.delete()
        return render(request, 'admin/homepage.html')
    else:
        return render(request, 'admin/medicinelist.html')
#function to delete a particular equipment by admin
def eqdde(request,id):
    if (equipment.objects.filter(id=id).exists()):
        data = equipment.objects.get(id=id)
        data.delete()
        return render(request, 'admin/homepage.html')
    else:
        return render(request, 'admin/equipmentlist.html')
#function to dispaly questions from students to doctors in admin side
def questlist(request):
    data=question.objects.all()
    data1=doctors.objects.all()
    return render(request,'admin/question.html',{'data':data,'data1':data1})
#function to approve questions from students to doctors by admin
def approve(request,id):
    data=question.objects.get(id=id)
    data.status='Approved'
    data.save()
    return render(request,'admin/homepage.html',{'data':data})
#function to reject questions from students to doctors by admin
def reject(request,id):
    data = question.objects.get(id=id)
    data.status = 'Rejected'
    data.save()
    return render(request, 'admin/homepage.html', {'data': data})

#function to convert into dict

def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

# view for sending response
def response_view(request):

    print("inside response view")

    x=(request.session.get('mid'))
    print (x)

    cursor = connection.cursor()
    cursor.execute("""

    select
    testapp_question.id,testapp_question.Collegeid,testapp_question.Name,testapp_question.question from testapp_question
    left outer join testapp_doctors
    on
    (testapp_question.did_id=testapp_doctors.id)
    where testapp_doctors.ids_id=%d  """%(x))

    dict = {}
    dict = dictfetchall(cursor)
    print(dict)
    context = {
        'dict': dict
    }
    print (dict)
    return render(request,'doctor/studqestions.html',context)

def case_view(request):
    formcase = CaseForm()
    if request.method =='POST':
        formcase = CaseForm(request.POST)
        if formcase.is_valid():
            formcase.save()
            return redirect('/doctorhomepage')
    return render(request,'doctor/case.html',{'formcase':formcase})

def doctor_response_view(request, id):
    respo = ResponseForm()
    print("inside response")
    #login_obj = logins.objects.get(id=id)
    sq_id = question.objects.get(id=id)
    print(sq_id.ids.id)
    print(type(sq_id.ids.id))
    login_obj = logins.objects.get(id=sq_id.ids.id)
    #l_id = int(sq_id.ids)
    #print(type(l_id))
    return render(request,'doctor/doctorresponsepage.html',{'respo':respo})

def request_appoint(request):
    x = config.userid
    print("inside appoinmt view")
    print(x)
    u_appoi = logins.objects.get(id=x)

    print(u_appoi)
    print("######################")
    print(type(u_appoi))
    print("######################")
    appoint = RequestForm()
    if request.method == 'POST':
        appoint =RequestForm(request.POST)
        if appoint.is_valid():
            a=appoint.save(commit=False)
            print("************")
            print(type(a))
            print("************")
            a.ids=u_appoi
            a.save()
            return redirect('/patienthomepage')
    return render(request,'users/requestappoint.html',{'appoint':appoint})

#view for student feedback
def student_feedback(request):
    x=config.userid
    print("****************inside student_feedback**************************")
    print(x)
    student = Register.objects.get(ids_id=x)
    print(student)
    feedback = student_feedback_form()
    if request.method == 'POST':
        feedback = student_feedback_form(request.POST)
        if feedback.is_valid():
            F=feedback.save(commit=False)
            F.student_name = student
            F.save()
            #return redirect("/patienthomepage")
    return render(request,'users/student_feedback.html',{'feedback':feedback})

#student_profile updation views
def update_student_view(request):
    x=config.userid
    print("Inside Update view")
    print(x)
    student = Register.objects.get(id=x)
    print(student)

    return render(request,'users/student_update.html',{'student':student})

#view for seeing feedback from admin side
def show_feedback_view(request):
    cursor = connection.cursor()
    cursor.execute("""
    select testapp_register.Collegeid,testapp_register.Name,testapp_student_feedback.feedback
    FROM  testapp_student_feedback
    LEFT OUTER JOIN testapp_register
    on (testapp_register.id = testapp_student_feedback.student_name_id)
    """)
    dict = {}
    dict = dictfetchall(cursor)
    print(dict)
    return render(request,'admin/viewfeedback.html',{'dict':dict})

#Approve questions from admin side
def approve_question_admin(request):
    cursor = connection.cursor()
    cursor.execute("""
    select testapp_question.id,testapp_question.Collegeid,testapp_question.Name,testapp_question.question
    FROM testapp_question
    """)
    dict = {}
    dict = dictfetchall(cursor)
    print(dict)
    return render(request,'admin/approvequestions.html',{'dict':dict})

#reject student questions from admin side
def reject_question_admin(request,id):
    q = question.objects.get(id=id)
    q.delete()
    return redirect('/app_questions')

#approve questions
def question_admin(request, id):
    aq = question.objects.get(id=id)
    ac = aq.Collegeid
    an = aq.Name
    ques = aq.question
    doctor = aq.did_id
    d_name = doctors.objects.get(id=doctor)

    print("******************* inside question approval********************")
    print(aq)
    print(ac)
    print(an)
    print(ques)
    print(doctor)
    print("doctor name is")
    print(d_name)

    ob= Approved_questions.objects.create(collegid =ac,Name=an,question=ques,doctor_id=doctor,doctor_name=str(d_name))
    ob.save()
    aq.delete()
    return redirect('/app_questions')

#docto is seeing questions belongs to them
def see_questions_doctor_view(request):
    print("********************inside Doctor view to his questions ******")
    x=config.userid
    print(x)
    cursor = connection.cursor()
    cursor.execute("""
    select testapp_approved_questions.id,testapp_approved_questions.collegid,testapp_approved_questions.Name,testapp_approved_questions.question
	from testapp_approved_questions
	LEFT outer join testapp_doctors
	on (testapp_approved_questions.doctor_id = testapp_doctors.id)
	left outer join testapp_logins
	on (testapp_doctors.ids_id = testapp_logins.id)
	where testapp_logins.id=%d """%(x))
    dict = {}
    dict = dictfetchall(cursor)
    print(dict)
    return render(request,'doctor/doctorquestionsresponse.html',{'dict':dict})


#doctor response views
def doctor_response_questions(request,id):
    print("hihihhihhhhihhhh")
    id = Approved_questions.objects.get(id=int(id))
    #print(id)
    form = Doctor_Response()
    if request.method == 'POST':
        form = Doctor_Response(request.POST)
        if form.is_valid():
            R=form.save(commit=False)
            R.question_id = id
            R.save()
    return render(request,'doctor/giving_response.html',{'form':form})
