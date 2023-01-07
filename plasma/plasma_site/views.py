from django.shortcuts import render
from .models import Article

def index(request):
    intro = Article.objects.get(title='intro')
    party_des1 = Article.objects.get(title='party_des1')
    party_des2 = Article.objects.get(title='party_des2')
    about1 = Article.objects.get(title='about1')
    about2 = Article.objects.get(title='about2')
    about_contact = Article.objects.get(title='about_contact')
    context = {'arts': {
        'intro': intro,
        'party_des1': party_des1,
        'party_des2': party_des2,
        'about1': about1,
        'about2': about2,
        'about_contact' : about_contact
    },
    }

    return render(request, 'plasma_site/index.html', context)
