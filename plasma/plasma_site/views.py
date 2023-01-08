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
        'about_contact': about_contact
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
    context = {
        'bullets': {
                    },
        'articles': {
            'reg_intro': Article.objects.get(title='reg_intro'),
            'cookies': Article.objects.get(title='cookies'),
            'licence': Article.objects.get(title='licence'),
            'refs': Article.objects.get(title='refs'),
            'disclaimer': Article.objects.get(title='disclaimer'),
            'copyrights': Article.objects.get(title='copyright'),
            'links': Article.objects.get(title='links'),
            'disclaimer2': Article.objects.get(title='disclaimer2'),
        }
    }
    return render(request, 'plasma_site/reg.html', context)


def privacy_policy(request):
    context = {
        'bullets': {
                    },
        'articles': {
            'intro_priv': Article.objects.get(title='intro_priv'),
            'rodo1': Article.objects.get(title='rodo1'),
            'rodo2': Article.objects.get(title='rodo2'),
            'rights': Article.objects.get(title='rights'),
            'links2': Article.objects.get(title='links2'),
            'protection': Article.objects.get(title='protection'),
            'reaveal': Article.objects.get(title='reaveal'),
            'contact_info': Article.objects.get(title='contact_info'),
        }
    }

    return render(request, 'plasma_site/privacy_policy.html', context)


def success(request):
    context = {}
    return render(request, 'plasma_site/success.html', context)
