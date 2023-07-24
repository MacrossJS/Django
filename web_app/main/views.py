from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница!',
        'values': ["Some", "Lorem", 123],
        'obj': {
            'language': 'Python',
            'age': 34,
            'hobby': 'coding'
        }
    }
    return render(request, "main/index.html", data)


def about(request):
    return render(request, "main/about.html")


def shop(request):
    return render(request, "main/shop.html")


def inventory(request):
    return render(request, "main/inventory.html")
