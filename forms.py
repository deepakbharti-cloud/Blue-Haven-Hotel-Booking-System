from django import forms
from .models import Hotel, Room, Review
class HotelForm(forms.ModelForm):
    class Meta: model=Hotel; fields=['name','city','address','description','cover_image']
class RoomForm(forms.ModelForm):
    class Meta: model=Room; fields=['name','room_type','description','price_per_night','capacity','amenities','image','active']
class ReviewForm(forms.ModelForm):
    class Meta: model=Review; fields=['rating','comment']; widgets={'comment':forms.Textarea(attrs={'rows':3})}
