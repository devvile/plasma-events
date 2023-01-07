from django.shortcuts import render
from .models import Article

def index(request):
    intro = Article.objects.get(title='intro')
    party_des1 = Article.objects.get(title='party_des1')
    party_des2 = Article.objects.get(title='party_des2')
    context = {
        'intro': intro,
        'party_des1': party_des1,
        'party_des2': party_des2
    }

    return render(request, 'plasma_site/index.html', context)
