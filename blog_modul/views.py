from django.db.models import Value,F
from django.db.models.functions import Length
from django.shortcuts import render,redirect,reverse
from django.views.generic import *
from .models import *
from home_model.models import Home
from about_modul.models import AboutModel
from django.http import HttpRequest,HttpResponse
from home_model.models import Home
from contact_modul.models import ContactUs
from django.contrib.auth.models import User
from .forms import *
# Create your views here.


class blog_view(ListView):
    template_name = 'blog.html'
    model = Blog_model
    context_object_name = 'blogs'
    def get_context_data(self, *, object_list=None, **kwargs):
        site_lan = self.request.COOKIES.get('site_language')
        if site_lan is None:
            site_lan = False
        elif site_lan is not None:
            site_lan = eval(site_lan)
        contaxt=super(blog_view, self).get_context_data(**kwargs)
        contaxt['rtl_fa']=site_lan
        return contaxt

class blogList_view(ListView):
    template_name = 'blog_list.html'
    model = Blog_model
    paginate_by = 3
    context_object_name = 'blogs'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(blogList_view, self).get_context_data(**kwargs)
        autor=Home.objects.all()
        category=Blog_category.objects.all()
        new=Blog_model.objects.order_by('-date')[:3].prefetch_related('blog_comment_set')
        for i in autor:
            name=i.name
        site_lan = self.request.COOKIES.get('site_language')
        if site_lan is None:
            site_lan = False
        elif site_lan is not None:
            site_lan = eval(site_lan)
        context['autor'] = name
        context['categorys'] = category
        context['news']=new
        context['rtl_fa']=site_lan
        return context




class blog_search(ListView):
    paginate_by = 3
    def get(self,request:HttpRequest,**kwargs):
        query=request.GET.get('search')
        blog_model=Blog_model.objects.filter(slug__icontains=query)
        autor = Home.objects.all()
        category = Blog_category.objects.all()
        new = Blog_model.objects.order_by('-date')[:3]
        for i in autor:
            name = i.name
        site_lan = self.request.COOKIES.get('site_language')
        if site_lan is None:
            site_lan = False
        elif site_lan is not None:
            site_lan = eval(site_lan)
        return render(request,'search_results.html',{'blogs':blog_model,'autor':name,'categorys':category,'news':new,'rtl_fa':site_lan})


def blog_cat(request:HttpRequest,cat):
        user=Home.objects.all()
        for i in user:
            autor=i
        site_lan = request.COOKIES.get('site_language')
        if site_lan is None:
            site_lan = False
        elif site_lan is not None:
            site_lan = eval(site_lan)
        category_name=Blog_model.objects.filter(category__url=cat)
        return render(request,'blog_category.html',{'categorys':category_name,'category_name':cat,'autor':autor,'rtl_fa':site_lan})

class blogDitail_view(DetailView):
    template_name = 'blog_ditail.html'
    model = Blog_model
    def get_context_data(self, **kwargs):
        about=AboutModel.objects.all()
        for i in about:
            user=i
        site_lan = self.request.COOKIES.get('site_language')
        if site_lan is None:
            site_lan = False
        elif site_lan is not None:
            site_lan = eval(site_lan)
        contaxt=super(blogDitail_view, self).get_context_data(**kwargs)
        replace_comment=kwargs.get('object')
        comment=Blog_comment.objects.filter(blog_id=replace_comment.id,replace=None,admin_approval=True)
        contaxt['user']=user
        contaxt['comments']=comment
        contaxt['rtl_fa']=site_lan
        contaxt['bot']=contact_form
        return contaxt

def blog_comment(request:HttpRequest):
    comment = request.GET.get('comment')
    blog = request.GET.get('blog_id')
    email = request.GET.get('email')
    user = request.GET.get('user')
    replace_iew= request.GET.get('replace')
    blog_comment_model=Blog_comment.objects.filter(email=email,blog_id=blog,user=user).all().count()
    site_lan = request.COOKIES.get('site_language')
    if site_lan is None:
        site_lan = False
    elif site_lan is not None:
        site_lan = eval(site_lan)
    if blog_comment_model < 3:
        if comment and blog and email and user and replace_iew is not None:
            new_comment = Blog_comment(text=comment, blog_id=blog, email=email, user=user, replace_id=replace_iew)
            new_comment.save()
        return render(request, 'blog_comment.html', {
            'comments': Blog_comment.objects.filter(blog_id=blog).order_by('-create_date').prefetch_related(),
             'rtl_fa':site_lan})
    return render(request,'blog_comment.html',{'comments':Blog_comment.objects.filter(blog_id=blog).order_by('-create_date').prefetch_related(),'rtl_fa':site_lan})


