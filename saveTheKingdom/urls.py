from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.story, name='story'),
    url(r'^mission/$', views.mission, name='mission'),
    url(r'^myWanderers/$', views.WandererByGuideListView.as_view(), name='my-wanderers'),
    url(r'^mission/setStatusHero/$', views.status_hero, name='setStatusHero'),
    url(r'^mission/saveWanderer/$', views.saveWanderer, name='saveWand'),
    url(r'^wall/$', views.AllWanderers, name='wall'),
    url(r'^signup/$', views.signup, name='signup'),

]