from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse

# def test(request):
#     return HttpResponse("test")

def home(request):
    return render(request, 'homepage.html', {'name':'muna', 'height':160})