from django.http import HttpResponse

def index(request):

    return HttpResponse('coefficients')
    # return HttpResponse({'commerceValue' : commerceValue})
