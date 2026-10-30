from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Hotel, Room, Review
from .forms import HotelForm, RoomForm, ReviewForm
from bookings.models import Booking

def home(request):
    q=request.GET.get('q',''); rooms=Room.objects.filter(active=True,hotel__approved=True).select_related('hotel')
    if q: rooms=rooms.filter(Q(hotel__name__icontains=q)|Q(hotel__city__icontains=q)|Q(name__icontains=q)|Q(amenities__icontains=q))
    return render(request,'hotels/home.html',{'rooms':rooms,'q':q})
def hotel_detail(request,pk):
    hotel=get_object_or_404(Hotel,pk=pk,approved=True)
    return render(request,'hotels/hotel_detail.html',{'hotel':hotel})
def room_detail(request,pk):
    room=get_object_or_404(Room,pk=pk,active=True,hotel__approved=True)
    return render(request,'hotels/room_detail.html',{'room':room})
@login_required
def owner_hotel_create(request):
    if not hasattr(request.user,'profile') or request.user.profile.role!='owner': return redirect('dashboard')
    form=HotelForm(request.POST or None,request.FILES or None)
    if request.method=='POST' and form.is_valid():
        obj=form.save(commit=False); obj.owner=request.user; obj.approved=False; obj.save(); messages.success(request,'Hotel submitted for admin approval.'); return redirect('dashboard')
    return render(request,'hotels/hotel_form.html',{'form':form,'title':'Add your hotel'})
@login_required
def room_create(request,hotel_id):
    hotel=get_object_or_404(Hotel,pk=hotel_id,owner=request.user)
    form=RoomForm(request.POST or None,request.FILES or None)
    if request.method=='POST' and form.is_valid():
        room=form.save(commit=False); room.hotel=hotel; room.save(); messages.success(request,'Room saved.'); return redirect('dashboard')
    return render(request,'hotels/room_form.html',{'form':form,'hotel':hotel})
@login_required
def review_create(request,hotel_id):
    hotel=get_object_or_404(Hotel,pk=hotel_id,approved=True)
    eligible=Booking.objects.filter(guest=request.user,room__hotel=hotel,status='confirmed').exists()
    if not eligible: messages.error(request,'A confirmed stay is required to review this hotel.'); return redirect('hotel_detail',pk=hotel.pk)
    form=ReviewForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        review,created=Review.objects.get_or_create(hotel=hotel,guest=request.user,defaults={**form.cleaned_data,'booking':Booking.objects.filter(guest=request.user,room__hotel=hotel,status='confirmed').first()})
        if not created: messages.info(request,'You have already reviewed this hotel.')
        return redirect('hotel_detail',pk=hotel.pk)
    return render(request,'hotels/review_form.html',{'form':form,'hotel':hotel})
