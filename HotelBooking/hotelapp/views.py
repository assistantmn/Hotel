from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotel

def saveHotels(request):
    if request.method=='POST':
        hname=request.POST['hotelName']
        hlocation=request.POST['location']
        htype=request.POST['hotelType']
        hrating=request.POST['rating']
        hcontact=request.POST['contact']
        address=request.POST['address']
        himage=request.FILES['hotel_image']
        new_hotel=Hotel(hotelName=hname,location=hlocation,hotelType=htype,rating=hrating,contact=hcontact,hotel_image=himage,address=address)
    #name from models = name from function saveHotels
        Hotel.save(new_hotel)
        return HttpResponse("<h1>Success ....</h1>")
    else:
        return render(request, 'AddHotels.html')


def showHotels(request):
    data=Hotel.objects.all()
    return render(request, 'HotelList.html',{'hotels':data})

def updateHotel(request):
    if request.method=='POST':
        hname=request.POST['hotelName']
        hlocation=request.POST['location']
        htype=request.POST['hotelType']
        hrating=request.POST['rating']
        hcontact=request.POST['contact']
        address=request.POST['address']
        himage=request.FILES['hotel_image']
        
        hId=request.POST['hotelId']
        data=Hotel.objects.filter(hotelId=hId)
        data.update(hotelName=hname,location=hlocation,hotelType=htype,rating=hrating,contact=hcontact,hotel_image=himage,address=address)
    #name from models = name from function saveHotels
        
        return HttpResponse("<h1>Success ....</h1>")
    else:
        return render(request, 'UpdateHotels.html')

