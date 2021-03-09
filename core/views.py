from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

# Create your views here.
from .models import Item


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'home-page.html', context)


def checkout(request):
    return render(request, 'checkout.html')


# def home(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, 'home.html', context)


class HomeView(ListView):
    model = Item
    template_name = 'home.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"
