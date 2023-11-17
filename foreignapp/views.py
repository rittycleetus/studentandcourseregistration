from django.shortcuts import render,redirect
from foreignapp.models import Course
from foreignapp.models import Student

# Create your views here.
def home(request):
    return render(request,'home.html')

def addstudent(request):
    return render(request,'addstudent.html')

def addcourse1(request):
    if request.method=='POST':
        cor_name=request.POST.get('cname')
        cor_fee=request.POST.get('cfees')
        course1=Course(course_name=cor_name,course_fees=cor_fee)
        course1.save()
        return redirect('/')

def addstudent(request):
    courses=Course.objects.all()
    return render(request,'addstudent.html',{'Course':courses})

def addstudent1(request):
    stu_name=request.POST['sname']
    stu_email=request.POST['semail']
    stu_age=request.POST['sage']
    stu_date=request.POST['sdate']
    stu_sel=request.POST['sel']
    course1=Course.objects.get(id=stu_sel)
    print(course1)
    student=Student(student_name=stu_name,student_email=stu_email,student_age=stu_age,joining_date=stu_date,course=course1)
    student.save()
    return redirect('showstudent')
        
def showstudent(request):
    stu=Student.objects.all()
    return render(request,'showstudent.html',{'foreigncourse':stu})

def editstudent(request,pk):
    student=Student.objects.get(id=pk)
    course=Course.objects.all()
    return render(request,'editstudent.html',{'student':student,'course':course})

def editstudent1(request,pk):
    if request.method=='POST':
        student=Student.objects.get(id=pk)
        student.student_name=request.POST['sname']
        student.student_email=request.POST['semail']
        student.student_age=request.POST['sage']
        student.joining_date=request.POST['sdate']
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        student.course=course1
        student.save()
        return redirect('showstudent')
    return render(request,'editstudent.html')


def deletestudent(request,pk):
    s=Student.objects.get(id=pk)
    s.delete()
    return redirect('showstudent')