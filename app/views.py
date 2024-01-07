from django.shortcuts import render
from .models import Student

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')

def feedback(request):
    return render(request,'feedback.html')

def than(request):
    return render(request,'thanku.html')

def coursesthird(request):
    return render(request, 'coursesthird.html')

def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'services.html')

def grade(a, b):
    if a is not None and b is not None:
        total = a + b

        if 90 <= total <= 100:
            return 10
        elif 80 <= total < 90:
            return 9
        elif 65 <= total < 80:
            return 8
        elif 60 <= total < 65:
            return 7
        elif 50 <= total < 60:
            return 6
        elif 45 <= total < 50:
            return 5
        elif 40 <= total < 45:
            return 4
        else:
            return 0
    else:
        return 0


def calculate(dg,ag,pfg,mg,sg,ase_g,eg,og,pg):
    c = (dg * 5) + (ag * 6) + (pfg * 4) + (mg * 4) + (sg * 1) + (ase_g * 3) + (eg * 2) + (og * 3) + (pg * 4.5)
    sgpa = c / 32.5
    return sgpa

def calculater(dg,ag,pfg,mg,sg,ase_g,eg,og,pg):
    c = (dg * 5) + (ag * 6) + (pfg * 4) + (mg * 4) + (sg * 1) + (ase_g * 3) + (eg * 2) + (og * 3) + (pg * 4.5)
    sgpa = c / 32.5
    return sgpa

def result(request):
    if request.method=='POST':
        is_advance = request.POST.get('Advance')
        is_regular = request.POST.get('Regular')
        di=int(request.POST.get('dbms-internals'))
        de=int(request.POST.get('dbms-externals'))
        ai=int(request.POST.get('aoop-internals'))
        ae=int(request.POST.get('aoop-externals'))
        pfi=int(request.POST.get('pfsd-internals'))
        pfe=int(request.POST.get('pfsd-externals'))
        mi=int(request.POST.get('mp-internals'))
        me=int(request.POST.get('mp-externals'))
        si=int(request.POST.get('epics-internals'))
        se=int(request.POST.get('epics-externals'))
        asi=int(request.POST.get('ase-internals'))
        ase=int(request.POST.get('ase-externals'))
        ei=int(request.POST.get('ese-internals'))
        ee=int(request.POST.get('ese-externals'))
        oi=int(request.POST.get('os-internals'))
        oe=int(request.POST.get('os-externals'))
        pi=int(request.POST.get('pc-internals'))
        pe=int(request.POST.get('pc-externals'))
        ye=2
        if is_advance:
            sec="ADVANCE"
            gpa = calculate(grade(di,de), grade(ai,ae), grade(pfi,pfe) , grade(mi,me), grade(si,se), grade(asi,ase), grade(ei,ee), grade(oi,oe), grade(pi,pe))
        else:
            sec="REGULAR"
            gpa = calculater(grade(di,de), grade(ai,ae), grade(pfi,pfe) , grade(mi,me), grade(si,se), grade(asi,ase), grade(ei,ee), grade(oi,oe), grade(pi,pe))
        sgpa=round(gpa,2)
        id = request.POST.get('rollNumber')
        name = request.POST.get('name')
        branch=request.POST.get('dep')
        sem="Odd"
        student = Student(
            Name=name,
            RollNumber=id,
            Department=branch,
            Sem=sem,
            Year=ye,
            Sgpa=sgpa,
            Type=sec,
        )
        student.save()
        return render(request, 'result.html', {'sgpa': sgpa,'yea':ye, 'sec': sec ,'sem':sem,'name' :name,'id': id ,'br':branch})


def firstcalculate(dg,cg,ipg,dsg,ig,dtg):
    c = (dg * 2) + (cg * 5) + (ipg * 2) + (dsg * 4) + (ig * 5) + (dtg * 2)
    sgpa=c/20
    return sgpa

def firstresult(request):
    if request.method=='POST':
        di = int(request.POST.get('dti-internals'))
        de = int(request.POST.get('dti-externals'))

        ci = int(request.POST.get('ctsd-internals'))
        ce = int(request.POST.get('ctsd-externals'))

        dti = int(request.POST.get('dtw-internals'))
        dte = int(request.POST.get('dtw-externals'))

        ii = int(request.POST.get('iot-internals'))
        ie = int(request.POST.get('iot-externals'))

        dsi= int(request.POST.get('ds-internals'))
        dse = int(request.POST.get('ds-externals'))

        ipi = int(request.POST.get('ipe-internals'))
        ipe = int(request.POST.get('ipe-externals'))

    gpa=firstcalculate(grade(di,de),grade(ci,ce),grade(ipi,ipe),grade(dsi,dse),grade(ii,ie),grade(dti,dte))
    sgpa=round(gpa,2)
    ye=1
    sec='-----'
    id = request.POST.get('rollNumber')
    name = request.POST.get('name')
    br = request.POST.get('dep')
    sem = 'Odd'
    # student = Student(
    #     Name=name,
    #     RollNumber=id,
    #     Department=br,
    #     Sem=sem,
    #     Year=ye,
    #     Sgpa=sgpa,
    #     Type=sec,
    # )
    # student.save()
    return render(request,'result.html',{'sgpa': sgpa,'yea':ye,'sem':sem, 'sec': sec ,'name' :name,'id': id,'br':br})

def firstco(request):
    return render(request,'firstcourses.html')

def evensc(request):
    return render(request,'Evens.html')


def Evenresult(request):
    if request.method == 'POST':
        is_advance = request.POST.get('Advance')
        is_regular = request.POST.get('Regular')
        psi = int(request.POST.get('psqt-internals'))
        pse = int(request.POST.get('psqt-externals'))
        mi = int(request.POST.get('mern-internals'))
        me = int(request.POST.get('mern-externals'))
        di = int(request.POST.get('ddai-internals'))
        de = int(request.POST.get('ddai-externals'))
        dai = int(request.POST.get('daa-internals'))
        dae = int(request.POST.get('daa-externals'))
        ci = int(request.POST.get('cloud-internals'))
        ce = int(request.POST.get('cloud-externals'))
        ati = int(request.POST.get('atfl-internals'))
        ate = int(request.POST.get('atfl-externals'))
        ni = int(request.POST.get('nps-internals'))
        ne = int(request.POST.get('nps-externals'))
        ye = 2

        # The following code block is the one you provided
        if is_advance:
            sec = "ADVANCE"
            gpa = EvencalculateA(grade(psi, pse), grade(mi, me), grade(di, de), grade(dai, dae), grade(ci, ce),
                                 grade(ati, ate), grade(ni, ne))
        else:
            sec = "REGULAR"
            gpa = EvencalculateRegular(grade(psi, pse), grade(mi, me), grade(di, de), grade(dai, dae), grade(ci, ce),
                                       grade(ati, ate), grade(ni, ne))

        sgpa = round(gpa, 2)
        roll = request.POST.get('rollnumber')
        name = request.POST.get('name')
        branch = request.POST.get('dep')
        sem = "Even"
        student = Student(
            Name=name,
            RollNumber=roll,
            Department=branch,
            Sem=sem,
            Year=ye,
            Sgpa=sgpa,
            Type=sec,
        )
        student.save()
        return render(request, 'result.html',
                      {'sgpa': sgpa, 'yea': ye, 'sec': sec, 'sem': sem, 'name': name, 'id': roll, 'br': branch})


def EvencalculateA(p,m,d,da,c,a,n):
    c = (p * 4) + (m * 4) + (d * 5) + (da * 6) + (c * 3) + (a * 3) +(n*6)
    sgpa=c/31
    return sgpa


def EvencalculateRegular(p,m,d,da,c,a,n):
    c = (p * 4) + (m * 2) + (d * 3) + (da * 4) + (c * 3) + (a * 3) +(n * 4)
    sgpa=c/23
    return sgpa

def firsteven(request):
    return render(request,'FirstEven.html')
