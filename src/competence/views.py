import random
from django.shortcuts import render, redirect
from .models import Commentaire, Formation, Aleatoire
from .forms import ContactForm
from django.http import Http404


# Create your views here.


def index(request):
    jeux = list(Aleatoire.objects.all())
    aleatoire = random.sample(jeux, 4)
    formation = Formation.objects.all()
    commentaire = Commentaire.objects.all()
    return render(request, 'competence/index.html', {'commentaire': commentaire, 'formation': formation, 'aleatoire': aleatoire})



def contact(request):
    form = ContactForm()
    return render(request, 'competence/contact.html', {'form': form})


def service(request):
    formation = Formation.objects.all()
    return render(request, 'competence/service.html', {'formation': formation})


def error(request):
    return render(request, 'competence/error.html')


def handle_404(request, exception):
    return render(request, 'competence/error.html', status=404)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            contact_message.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'competence/contact.html', {'form': form})


def success(request):
    return render(request, 'competence/success.html')


def details(request, myid):
    formation = Formation.objects.get(id=myid)
    return render(request, 'competence/details.html', {'formation': formation})