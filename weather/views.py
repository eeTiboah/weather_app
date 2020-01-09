from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
	'''url = 'http://api.openweathermap.org/data/2.5/weather?q=city&appid=69cc108c2c5f3c222700a6de6b5a0d91'
	city=City.objects.all()
	city_weather=requests.get(url.format(city)).json()
	print(city_weather)'''
	if request.method=='POST':
		form=CityForm(request.POST)
		form.save()
	cities=City.objects.all()
	form=CityForm()
	weather_data=[]
	for city in cities:
		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=69cc108c2c5f3c222700a6de6b5a0d91'
		city_weather=requests.get(url.format(city)).json()
		print(city_weather)
		weather_info= {
		'city':city.name,
		'temperature':city_weather['main']['temp'],
		'description':city_weather['weather'][0]['description'],
		'icon':city_weather['weather'][0]['icon']
		}
		weather_data.append(weather_info)
	return render(request, 'weather/index.html', {'weather_data':weather_data, 'form':form})


def delete(request, id):

    if request.method == 'POST':
        print(request)
        City.objects.filter(id=id).delete()

    return redirect('/')
