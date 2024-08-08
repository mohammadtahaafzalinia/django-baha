from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from home_model.models import Home
from django.http import HttpResponse,HttpRequest
from googletrans import Translator
# Create your views here.


class about(ListView):
    template_name = 'about.html'
    model = AboutModel
    def get_context_data(self, *, object_list=None, **kwargs):
            name = AboutModel.objects.all()
            favo = Favorites.objects.all()
            service = Service.objects.all()
            opininos = Opinions.objects.all()
            price = Prices.objects.all()
            for i in name:
                name_user = i
            context = super(about,self).get_context_data(**kwargs)
            site_lan=self.request.COOKIES.get('site_language')
            if site_lan is None:
                site_lan = False
            elif site_lan is not None:
                 site_lan=eval(site_lan)
            context['favos']= favo
            context['services']= service
            context['opininos']= opininos
            context['prices']= price
            context['rtl_fa']= site_lan
            return context

# def stars(request:HttpRequest):
#     star=Opinions.objects.all()
#
#     return render(request,'about.html',{'stars':stare})

