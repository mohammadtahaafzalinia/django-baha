from django.shortcuts import render
from .models import *
from django.views.generic import *
from home_model.models import Home
# Create your views here.


class resume_view(ListView):
    template_name = 'resume.html'
    model = Resume_model
    context_object_name = 'resumes'
    def get_context_data(self, *, object_list=None, **kwargs):
        resume_ed=Resume_educational.objects.all()
        skills=Skills.objects.all()
        work=Work_process.objects.all()
        site_lan = self.request.COOKIES.get('site_language')
        if site_lan is None:
            site_lan = False
        elif site_lan is not None:
            site_lan = eval(site_lan)
        contaxt=super(resume_view, self).get_context_data(**kwargs)
        contaxt['resume_eds']=resume_ed
        contaxt['skills']=skills
        contaxt['works']=work
        contaxt['rtl_fa']=site_lan
        return contaxt
