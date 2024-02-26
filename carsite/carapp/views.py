from django.shortcuts import render

from urllib import response
from django.http import HttpResponse
from .models import CarType, Vehicle, Buyer,OrderVehicle, GroupMember
from django.shortcuts import get_object_or_404
from django.views import View
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