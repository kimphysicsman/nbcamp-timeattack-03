from django.shortcuts import render, redirect
from .models import Category, Drink
import json
from django.http import JsonResponse

# Create your views here.


def home(request):
    return redirect('/menu')


def menu(request):
    if request.method == 'GET':
        all_categories = Category.objects.all()
        all_items = Drink.objects.all()
        return render(request, 'menu.html', {'drinks': all_items,
                                             'categories': all_categories})
    elif request.method == 'POST':
        data = json.loads(request.body)

        category_name = data['category']
        category = Category.objects.get(name=category_name)
        sub_items = Drink.objects.filter(category=category)

        drinks = {
            'drinks': sub_items,
        }

        return render(request, 'drink_box.html', drinks)
