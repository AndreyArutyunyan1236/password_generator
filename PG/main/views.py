from django.shortcuts import render
from .models import Options

def generate(request):
    opt = Options()
    
    if request.method == 'POST':
        up = 'Upper' in request.POST
        low = 'Lower' in request.POST
        nums = 'Numbers' in request.POST
    
        Options.objects.create(
            upper= up,
            lower=low,
            numbers=nums,
        )
    
        if low:
            print("Lower is working")
    
    return render(request, 'main/generate.html', {})
