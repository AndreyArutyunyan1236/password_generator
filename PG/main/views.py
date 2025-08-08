from django.shortcuts import render
from .models import Options

import random as rd
import string as st

def generate(request):
    opt = Options()
    length = 8
    password = ''
    password_chars = []
    
    if request.method == 'POST':
        up = 'Upper' in request.POST
        low = 'Lower' in request.POST
        nums = 'Numbers' in request.POST
    
        Options.objects.create(
            upper= up,
            lower=low,
            numbers=nums,
        )
    
        chars = ''
        if low:
            chars += st.ascii_lowercase
        if up:
            chars += st.ascii_uppercase
        if nums:
            chars += st.digits
        
        password_chars = []
        for i in range(length):
            rand_char = rd.choice(chars)
            password_chars.append(rand_char)
        password = ''.join(password_chars)
    
    return render(request, 'main/generate.html', {'password': password})


