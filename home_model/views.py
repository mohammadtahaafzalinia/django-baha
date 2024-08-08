from django.shortcuts import *
from django.views.generic import ListView,CreateView,View,TemplateView
import uuid
from django.http import HttpResponse,HttpRequest
from .models import *
from django.urls.resolvers import ResolverMatch
from django.contrib import messages
#====================unique url===========================
unique_id1 = uuid.uuid4()
unique_id2 = uuid.uuid4()
unique_id3 = uuid.uuid4()
unique_id4 = uuid.uuid4()
unique_id5 = uuid.uuid4()
unique_id6 = uuid.uuid4()
unique_id7 = uuid.uuid4()
unique_id8 = uuid.uuid4()
unique_id9 = uuid.uuid4()
#======================music===============================
def play_music(request):
    music_path = 'static/audio/music.mp3'
    with open(music_path, 'rb') as music_file:
        response = HttpResponse(music_file.read(), content_type='audio/mp3')
        response['Content-Disposition'] = 'inline'
        return response
# Create your views here.
class home(ListView):
    model = Home
    template_name = 'home.html'
    def get_context_data(self, *, object_list=None, **kwargs):
            name = Home.objects.all()
            for i in name:
                name_user = i
            context = super(home,self).get_context_data(**kwargs)
            site_lan=self.request.COOKIES.get('site_language')
            if site_lan is None:
                site_lan = False
            elif site_lan is not None:
                 site_lan=eval(site_lan)
            context['user']= name_user
            context['rtl_fa']=site_lan
            context['messages']=messages.success(self.request,'ارررههه')
            return context


# class home_lan(View):
#     def get(self, request:HttpRequest, code):
#         site_lan=request.COOKIES.get('site_language')
#         if site_lan is not None:
#             res = HttpResponse('checked cooky') and redirect(reverse('home'))
#             res.set_cookie('site_language', code)
#             return res
#         elif site_lan is None:
#             res = HttpResponse('created cooky') and redirect(reverse('home'))
#             res.set_cookie('site_language', code)
#             return res
#         return redirect(reverse('home'))




            # lang:Home=Home.objects.filter(language_code__exact=code).first()
            # if lang is not None:
            #     if lang.language == False:
            #        lang.language = True
            #        lang.save()
            #        return redirect(reverse('home'))
            #     elif lang.language:
            #         lang.language = False
            #         lang.save()
            #         return redirect(reverse('home'))
            # return redirect(reverse('home'))


#=====================render_partial========================

def theme_options(request:HttpRequest):
    site_lan = request.COOKIES.get('site_language')
    if site_lan is None:
        site_lan = False
    elif site_lan is not None:
        site_lan = eval(site_lan)
    return render(request, 'partial/theme_options.html',{'rtl_fa':site_lan})



def link(request):
    site_lan = request.COOKIES.get('site_language')
    if site_lan is None:
        site_lan = False
    elif site_lan is not None:
        site_lan = eval(site_lan)
    return render(request, 'partial/link.html',{'rtl_fa':site_lan})




def main_site(request):
    site_lan = request.COOKIES.get('site_language')
    if site_lan is None:
        site_lan = False
    elif site_lan is not None:
        site_lan = eval(site_lan)
    return render(request, 'partial/main_site.html',{'rtl_fa':site_lan})




def menu(request):
    site_lan = request.COOKIES.get('site_language')
    if site_lan is None:
        site_lan = False
    elif site_lan is not None:
        site_lan = eval(site_lan)
    return render(request, 'partial/menu.html',{'rtl_fa':site_lan})




def Home_section(request):
    site_lan = request.COOKIES.get('site_language')
    if site_lan is None:
        site_lan = False
    elif site_lan is not None:
        site_lan = eval(site_lan)
    return render(request, 'partial/Home_section.html',{'rtl_fa':site_lan})





def http_404(request):
    return render(request,'http_404.html',status=404)

def js(request):
    return render(request, 'partial/js.html')
def preloader(request):
    return render(request, 'partial/preloader.html')
