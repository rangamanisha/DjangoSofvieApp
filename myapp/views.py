from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    dropone = StateModel.objects.all()
    company_data = CompanyModel.objects.all()
    if request.method == 'POST':
        c_name = request.POST.get('c_name')
        dob = request.POST.get('dob')
        state = request.POST.get('state')
        city = request.POST.get('city')
        create_obj = CompanyModel.objects.create(
            company_name=c_name,
            dob=dob,
            state = StateModel.objects.get(id=state),
            city = CityModel.objects.get(id=city),
        )
        messages.success(request,'Miner Successfully Added')

    context = {'dropone':dropone,'company_data':company_data}
    return render(request,'index.html',context)


def UpdateData(request,id):
    get_obj  = CompanyModel.objects.get(id=id)
    dropone = StateModel.objects.all()
    droptwo = CityModel.objects.filter(state_id = get_obj.state.id)
    print(droptwo)
    if request.method == 'POST':
        get_obj.company_name = request.POST.get('c_name')
        get_obj.dob = request.POST.get('dob')
        get_obj.state = StateModel.objects.get(id=request.POST.get('state'))
        get_obj.city = CityModel.objects.get(id=request.POST.get('city'))
        get_obj.save()
        messages.info(request,'Company Successfully Updated')
        return redirect('/')
    context = {'get_obj':get_obj,'dropone':dropone,'droptwo':droptwo}
    return render(request,'upobj.html',context)

def DeleteData(request,id):
    get_obj  = CompanyModel.objects.get(id=id)
    get_obj.delete()
    messages.error(request,'Company Successfully Deleted')
    return redirect('/')


def sub(request):
    state = request.GET.get('state')
    
    droptwo = CityModel.objects.filter(state_id = state)
    context = {'droptwo':droptwo,}
    return render(request,'subcategory.html',context)