from django.shortcuts import render
from .models import Wanderer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import newWanderer
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
    paginate_by = 10
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
def save_wanderer(request):
    # only process save if user completed mission first
    if (request.session['complete']):
        form = newWanderer(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                w = Wanderer.objects.create(
                    name=form.cleaned_data['name'],
                    comment = form.cleaned_data['comment'],
                    status = request.session['status'],
                    guide = request.user
                )
                request.session['complete'] = False
                request.session['status']='l'
                return HttpResponseRedirect(reverse('my-wanderers'))
        else:
            form = newWanderer()
        
        return render(request, 'save_wanderer.html',{'form':form} )
    # if mission not complete redirect to mission
    else: return HttpResponseRedirect(reverse('mission'))