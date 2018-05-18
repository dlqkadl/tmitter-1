from django.shortcuts import render

#home view
def home(request):
    return render(request, 'home.html')

def help(request):
    return render(request, 'help.html')

def about(request):
    return render(request, 'about.html')