from django.shortcuts import render

# Create your views here.
def transform(request):
    return render(request,'transform.html')