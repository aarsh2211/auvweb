from django.shortcuts import render

def departments(request):
    return render(request, 'departments/departments.html')
def mechanical(request):
    return render(request, 'departments/mechanical.html')
def software(request):
    return render(request, 'departments/software.html')
def embedded(request):
    return render(request, 'departments/embedded.html')
