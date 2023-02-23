from django.shortcuts import render
import re

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def calculator(request, menu = DATA):
    servings = int(request.GET.get('servings', 1))
    name_pattern = r"(\<{1})([A-z]*)(\:)(\s{1})([A-Z]{3})(\s{1})(\'{1})(\/{1})([a-z]+)(\/{1})(\??)(([a-z]{8})?)(\=?)(\d?)(\'{1})(\>{1})"
    result = r"\9"
    delicious = re.sub(name_pattern, result, str(request))
    recipe = {}
    dishes = menu[delicious]
    for ingredients, mass in dishes.items():
        mass *= servings
        recipe[ingredients] = mass
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/home.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }