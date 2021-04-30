from django.shortcuts import render
from .models import destination

# Create your views here.
def index(request):
    dest1=destination()
    dest1.name='Delhi'
    dest1.desc='2 Flights daily from regular connections'
    dest1.price=20
    dest1.img='destination_1.jpg'
    dest1.offer=True


    dest2=destination()
    dest2.name='Mumbai'
    dest2.desc='3 Flights a week from regular connections'
    dest2.price=25
    dest2.img='destination_2.jpg'
    dest2.offer=False

    dest3=destination()
    dest3.name='Kolkata'
    dest3.desc='2 Flights a week from regular connections'
    dest3.price=15
    dest3.img='destination_3.jpg'
    dest3.offer=True


    dests=[dest1,dest2,dest3]

     #return render(request,'index.html',{'dests':dests})
    return render(request,'index1.html')