from django.shortcuts import render


def index(request):
    """home page"""

    print(123)

    return render(request, 'exchanger/home.html')