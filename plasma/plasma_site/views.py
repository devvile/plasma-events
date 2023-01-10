from django.shortcuts import render
from .models import Article, Link, Bullet

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
        'bullets': {'licence': Bullet.objects.filter(list='licence'),
                    'licence2': Bullet.objects.filter(list='licence2'),
                    'refs1': Bullet.objects.filter(list='refs'),
                    'refs2': Bullet.objects.filter(list='refs2'),
                    'refs3': Bullet.objects.filter(list='refs3'),
                    'disclaimer': Bullet.objects.filter(list='disclaimer'),
                    },
        'articles': {
            'reg_intro': Article.objects.get(title='reg_intro'),
            'cookies': Article.objects.get(title='cookies'),
            'licence1': Article.objects.get(title='licence1'),
            'licence2': Article.objects.get(title='licence2'),
            'licence3': Article.objects.get(title='licence3'),
            'refs1': Article.objects.get(title='refs1'),
            'refs2': Article.objects.get(title='refs2'),
            'refs3': Article.objects.get(title='refs3'),
            'refs4': Article.objects.get(title='refs4'),
            'disclaimer': Article.objects.get(title='disclaimer'),
            'copyrights': Article.objects.get(title='copyright'),
            'links': Article.objects.get(title='links'),
            'disclaimer2a': Article.objects.get(title='disclaimer2a'),
            'disclaimer2b': Article.objects.get(title='disclaimer2b'),
        }
    }
    return render(request, 'plasma_site/reg.html', context)


def privacy_policy(request):
    context = {
        'bullets': Bullet.objects.filter(list='prawo'),
        'articles': {
            'intro_priv': Article.objects.get(title='intro_priv'),
            'rodo1': Article.objects.get(title='rodo1'),
            'rodo2': Article.objects.get(title='rodo2'),
            'rights1': Article.objects.get(title='rights1'),
            'rights2': Article.objects.get(title='rights2'),
            'links2': Article.objects.get(title='links2'),
            'protection': Article.objects.get(title='protection'),
            'reaveal': Article.objects.get(title='reaveal'),
            'contact_info': Article.objects.get(title='contact_info'),
        }
    }

    return render(request, 'plasma_site/privacy_policy.html', context)


def success(request):
    context = {'success': Article.objects.get(title='success') }
    return render(request, 'plasma_site/success.html', context)
