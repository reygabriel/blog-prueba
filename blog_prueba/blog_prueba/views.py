from django.shortcuts import render

# Vista basada en una función


def index_view(request):
    return render(request, 'index.html', {})