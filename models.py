from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
class Hotel(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='hotels')
    name=models.CharField(max_length=180); city=models.CharField(max_length=100); address=models.TextField(); description=models.TextField()
    cover_image=models.ImageField(upload_to='hotels/',blank=True,null=True)
    approved=models.BooleanField(default=False); created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.name} — {self.city}'
    @property
    def average_rating(self):
        result=self.reviews.aggregate(models.Avg('rating'))['rating__avg']; return round(result,1) if result else None
class Room(models.Model):
    ROOM_TYPES=[('deluxe','Deluxe Room'),('executive','Executive Room'),('suite','Luxury Suite'),('family','Family Room')]
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='rooms')
    name=models.CharField(max_length=120); room_type=models.CharField(max_length=20,choices=ROOM_TYPES,default='deluxe')
    description=models.TextField(blank=True); price_per_night=models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0)])
    capacity=models.PositiveSmallIntegerField(default=2); amenities=models.CharField(max_length=300,blank=True); image=models.ImageField(upload_to='rooms/',blank=True,null=True)
    active=models.BooleanField(default=True); created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=['price_per_night']
    def __str__(self): return f'{self.hotel.name}: {self.name}'
class Review(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='reviews'); guest=models.ForeignKey(User,on_delete=models.CASCADE)
    booking=models.OneToOneField('bookings.Booking',on_delete=models.CASCADE,related_name='review')
    rating=models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)]); comment=models.TextField(blank=True); created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=['-created_at']
