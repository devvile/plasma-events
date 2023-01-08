from django.shortcuts import render
from .models import Article, Link

def index(request):
    intro = Article.objects.get(title='intro')
    party_des1 = Article.objects.get(title='party_des1')
    party_des2 = Article.objects.get(title='party_des2')
    about1 = Article.objects.get(title='about1')
    about2 = Article.objects.get(title='about2')
    about_contact = Article.objects.get(title='about_contact')

    instagram = Link.objects.get(name='Instagram')
    tiktok = Link.objects.get(name='Tiktok')
    facebook = Link.objects.get(name='Facebook')

    context = {'arts': {
        'intro': intro,
        'party_des1': party_des1,
        'party_des2': party_des2,
        'about1': about1,
        'about2': about2,
        'about_contact' : about_contact
    }, 'socials': {
        'instagram': instagram,
        'facebook': facebook,
        'tiktok': tiktok,
    }
    }

    return render(request, 'plasma_site/index.html', context)


def tickets(request):
    context = {}
    return render(request, 'plasma_site/tickets.html', context)


def regulations(request):
    context = {}
    return render(request, 'plasma_site/reg.html', context)


def privacy_policy(request):
    context = {}
    return render(request, 'plasma_site/privacy_policy.html', context)


def success(request):
    context = {}
    return render(request, 'plasma_site/success.html', context)
