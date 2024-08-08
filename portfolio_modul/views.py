from django.shortcuts import render
from .models import *
from django.views.generic import *
from home_model.models import Home
# Create your views here.

class Portfolio_view(ListView):
    template_name = 'portfolio.html'
    model = Portfolio
    context_object_name = 'ports'
    def get_context_data(self, *, object_list=None, **kwargs):
        site_lan = self.request.COOKIES.get('site_language')
        if site_lan is None:
            site_lan = False
        elif site_lan is not None:
            site_lan = eval(site_lan)
        category=PortfolioCategory.objects.all()
        contaxt=super(Portfolio_view, self).get_context_data(**kwargs)
        contaxt['categorys']=category
        contaxt['rtl_fa']=site_lan
        return contaxt

class Video_view(DetailView):
    template_name = 'video.html'
    model = Portfolio

