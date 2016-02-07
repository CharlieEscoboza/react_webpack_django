from django.shortcuts import render

# Create your views here.
def showHello(request):
	return	render(request, 'helloWorld.html')
