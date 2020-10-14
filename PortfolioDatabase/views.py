from django.shortcuts import render, redirect  # program imports
from django.http import HttpResponse  # program imports
from .models import Hobby  # program imports
from .models import portfolio  # program imports
from .forms import HobbyForm
from .forms import contactForm
from .models import contact  # program imports
from .forms import portfolioForm
from django.template import loader


# Create your views here.
def index(request):
    Hobby_list = Hobby.objects.all()
    context = {
        'Hobby_list': Hobby_list,
    }
    return render(request, 'portfolio/index.html', context)


def detail(request, Hobby_id):
    hobby = Hobby.objects.get(pk=Hobby_id)
    context = {
        'hobby': hobby
    }
    return render(request, 'portfolio/detail.html', context)


def Home(request):  # function that returns a http request
    return render(request, 'portfolio/home.html')  # message that gets returned


def Hobbies(request):  # hobbies request function
    Hobby_list = Hobby.objects.all()
    context = {
        'Hobby_list': Hobby_list,
    }
    return render(request, 'portfolio/hobbies.html', context)


def Portfolio(request):  # portfolio function
    portfolio_list = portfolio.objects.all()  # portfolio object from  the database
    context = {
        'Portfolio_list': portfolio_list,
    }
    return render(request, 'portfolio/portfolio.html', context)  # portfolio message thats being returned


def detail2(request, portfolio_id):
    Portfolio = portfolio.objects.get(pk=portfolio_id)
    context = {
        'Portfolio': Portfolio
    }
    return render(request, 'portfolio/detail2.html', context)


def Contact(request):  # contact function
    contact_list = contact.objects.all()
    context = {
        'contact_list': contact_list,
    }
    return render(request, 'portfolio/contact.html', context)


def create_hobby(request):
    form = HobbyForm(request.POST or None)

    if (form.is_valid()):
        form.save()
        return redirect('PortfolioDatabase:index')

    return render(request, 'portfolio/hobby-form.html', {'form': form})


def update_portfolio1(request, id):  # contact function
    portfolio1 = portfolio.objects.get(id=id)
    form = portfolioForm(request.POST or None, instance=portfolio1)
    if (form.is_valid()):
        form.save()
        return redirect('PortfolioDatabase:Portfolio')

    return render(request, 'portfolio/portfolio-form.html', {'form': form, 'Portfolio': portfolio1})


def delete_portfolio1(request, id):  # contact function
    portfolio1 = portfolio.objects.get(id=id)

    if request.method == "POST":
        portfolio1.delete()
        return redirect('PortfolioDatabase:Portfolio')

    return render(request, 'portfolio/portfolio-delete.html', { 'portfolio1': portfolio1})


def create_contact(request):
    form = contactForm(request.POST or None)

    if (form.is_valid()):
        form.save()
        return redirect('PortfolioDatabase:Contact')

    return render(request, 'portfolio/contact-form.html', {'form': form})


def create_Portfolio(request):
    form = portfolioForm(request.POST or None)

    if (form.is_valid()):
        form.save()
        return redirect('PortfolioDatabase:Portfolio')

    return render(request, 'portfolio/portfolio-form.html', {'form': form})
