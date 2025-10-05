from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.
def crud(request):
    emp = Employee.objects.all()
    return render(request, 'crud.html', {'emp':emp})


def add_emp(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']

        try:
            Employee.objects.get(email=email)
            msg = "use another email this already exist"
        except Employee.DoesNotExist:
            Employee.objects.create(
                name=name,
                email=email,
                address=address, 
                phone=phone,
            )
            msg = "employee added successfully"

        return render(request, 'crud.html', {'msg':msg})

    return redirect('crud')