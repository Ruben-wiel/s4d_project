from django.shortcuts import render


# Lijst met de postinformatie
adposts = [
    {
        'author': 'CoreyMS',
        'title': 'Ad Post 1',
        'content': 'Boodschappen',
        'reward': '10 koekjes',
        'date_posted': 'May 12, 2020' 
    },
    {
        'author': 'Ruben',
        'title': 'Melk',
        'content': 'Ik heb melk nodig',
        'reward': 'Rune scimi',
        'date_posted': 'May 12, 2006' 
    }
]


# Create your views here.
def home(request):
    return render(request, 'website/home.html')

def details(request):
    return render(request, 'website/details.html', {'title': 'Details'})

def posts(request):
    context = {
        'adposts': adposts 
    }
    return render(request, 'website/posts.html', context)

def account(request):
    return render(request, 'website/account.html')

def about(request):
    return render(request, 'website/about.html')
