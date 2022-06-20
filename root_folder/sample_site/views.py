from django.http.response import HttpResponse, HttpResponseNotFound, Http404

contents = {
		'sports': 'sport page',
		'finance': 'finance page',
		'politics': 'politics page'
}

def home_page(request):
    return HttpResponse("THis is the home page! by 217")

def topics(request, topic):
    if topic in contents.keys():
        return HttpResponse(contents[topic])
    else:
        # return HttpResponseNotFound(f"No relavant info for {topic}")
        raise Http404(f"404 for info {topic}")
        # pass