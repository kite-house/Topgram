from django.shortcuts import render

def error404(request, exception):
    return render(request, 'error.html', context={'error_code' : '404', 'error_description' : 'Заблудились?'})

def error500(request):
    return render(request, 'error.html', {'error_code' : '500', 'error_description' : 'Server Error'})