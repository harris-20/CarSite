from django.shortcuts import render

from urllib import response
from django.http import HttpResponse
from .models import CarType, Vehicle, Buyer,OrderVehicle, GroupMember
from django.shortcuts import get_object_or_404
from django.views import View
from .forms import ContactForm,OrderVehicleForm, VehicleSearchForm

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
# Create your views here.
'''''
def homepage(request):
    # Get up to 10 vehicles sorted by price in descending order
    cartype_list = CarType.objects.all().order_by('vehicles__car_price')[:10]
    #cartype_list = CarType.objects.distinct().order_by('vehicles__car_price')[:10]

    response = HttpResponse()
    heading1 = '<p>' + 'Different Types of Cars:' + '</p>'
    response.write(heading1)

    for cartype in cartype_list:
        para = '<p>' + str(cartype.id) + ': ' + str(cartype) + '</p>'
        response.write(para)

    return response
'''
def homepage(request):
    cartype_list = CarType.objects.all().order_by('id')
    return render(request, 'carapp/homepage.html', {'cartype_list': cartype_list})

def about(request):
    return HttpResponse('This is a Car Showroom')

#def contact_us(request):
 #   return HttpResponse('Contact us at at 2269752336')

def vehicles(req):
    form =OrderVehicleForm()
    vehicles_all=Vehicle.objects.all()
    return render(req,'carapp/vehicles.html',{'form': form,'vehicles_all':vehicles_all})

def contacts(req):
    form =ContactForm()
    return render(req,'carapp/contact.html',{'form': form})

def cardetail(request,cartype_no):
    #cartype=CarType.objects.get(id=cartype_no)
    cartype=get_object_or_404(CarType, id=cartype_no)
    vehicles=Vehicle.objects.filter(car_type__name=cartype.name)
    response = HttpResponse()
    for vehicle in vehicles:
        para="<p>"+ vehicle.car_name +"</p>"
        response.write(para)

    return response


def groupdetail(request):
    print("HI")
    members = GroupMember.objects.all().order_by('first_name')
    response = HttpResponse()
    for member in members:
        heading=("<h3>"+member.first_name+"</h3>")
        response.write(heading)
        para=("<p>"
              + member.first_name + "<br>"
              + member.last_name + "<br>"
              + str(member.semester) + "<br>"
              + member.personal_page + "<br>"
              "</p>")
        response.write(para)
    return response

def orderhere(request):
    res=HttpResponse()
    res.write("You can place your order here.")
    return res

def search(request):
    form = VehicleSearchForm(request.GET)
    vehicles = Vehicle.objects.all()

    if form.is_bound and form.is_valid:  # Checking if form is valid
        if 'id' in form.data:
            id = form.data['id']
            vehicle = get_object_or_404(Vehicle, pk=id)  # Retrieving vehicle by primary key
            return render(request, "carapp/search_vehicle.html", {'found': vehicle, 'vehicles': vehicles})

    return render(request, "carapp/search_vehicle.html", {'vehicles': vehicles})

def orderhere(request):
    msg = ''
    vehiclelist = Vehicle.objects.all()
    if request.method == 'POST':
        form = OrderVehicleForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            # if order.vehicle.orders <= order.vehicle.instock:
           # if order.vehicle.orders.count() <= order.vehicle.inventory:
            #if order.quantity <= order.vehicle.inventory:
            #if order.vehicle.orders.count() <= order.vehicle.inventory:
                #order.vehicle.inventory -= 1
            if order.quantity <= order.vehicle.inventory:
                order.vehicle.inventory -= order.quantity
                order.vehicle.save()
                order.save()
                msg = 'Your vehicle has been ordered'
            else:
                msg = 'We do not have sufficient stock to fill your order.'
                return render(request, 'carapp/nosuccess_order.html', {'msg': msg})
    else:
        form = OrderVehicleForm()
    return render(request, 'carapp/orderhere.html', {'form': form, 'msg': msg, 'vehiclelist': vehiclelist})