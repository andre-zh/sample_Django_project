from django.http.response import HttpResponse

def home_page(request):
    return HttpResponse("THis is the home page! by 217")