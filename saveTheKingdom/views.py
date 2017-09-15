from django.shortcuts import render
from .models import Wanderer
from .forms import newWanderer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

# Create your views here.

def story(request):
    num_wanderers = Wanderer.objects.all().count()
    return render(
        request,
        'story.html',
        context = {'num_wanderers':num_wanderers, 'bodyid':"story"},
    )

@login_required
def mission(request):
    request.session['status']='l'
    request.session['complete'] = True
    return render(
        request,
        'mission.html',
        context={'bodyid':"mission",'stat':request.session['status'], 'num_plants':(range(1,5,1)),'num_rows':[1,2]},
    )

def status_hero(request):
    if not request.is_ajax() or not request.method=='POST':
        return HttpResponseNotAllowed(['POST'])

    request.session['status'] = 'h'
    return HttpResponse('ok')


class WandererByGuideListView(LoginRequiredMixin,ListView):
    model = Wanderer
    template_name = 'wanderers_list.html'
    paginate_by = 30
    context_object_name = 'wanderers_list'

    def get_queryset(self):
        return Wanderer.objects.filter(guide=self.request.user).order_by('id')

def AllWanderers(request):
    allHeroes = Wanderer.objects.filter(status='h').order_by('id')
    allLosers = Wanderer.objects.filter(status='l').order_by('id')
    heroCount = allHeroes.count()
    loserCount = allLosers.count()
    return render(request,'wall_xeek.html', {'allHeroes':allHeroes,'allLosers':allLosers,'hCount':heroCount,'lCount':loserCount})

@login_required
def saveWanderer(request):
    if (request.session['complete']):
        if request.method == 'POST':
            
            w = Wanderer.objects.create(
                name= request.POST.get("nickname"),
                comment = request.POST.get("comment"),
                status = request.session['status'],
                guide = request.user
            )
            request.session['complete'] = False
            request.session['status']='l'
            return HttpResponseRedirect(reverse('my-wanderers'))
        
            
        
        return render(request, 'save_wanderer.html')
    # if mission not complete redirect to mission
    else: return HttpResponseRedirect(reverse('mission'))
    # return render(request,'save_wanderer.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('story'))
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
