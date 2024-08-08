from django.shortcuts import render, redirect, reverse
from django.views.generic import *
from django.views.generic.edit import *
from .models import *
from .forms import *
from django.http import HttpRequest
from django.urls import reverse_lazy
from utils.send_email import send_email_replace
from home_model.models import Home


# Create your views here.


class contactView(CreateView):
    template_name = 'contact.html'
    model = Contact
    success_url = '/'

    def get_form_class(self):
        site_lan = self.request.COOKIES.get('site_language')
        if site_lan is None:
            site_lan = False
        elif site_lan is not None:
            site_lan = eval(site_lan)
        if site_lan:
            return Contact_form_en
        elif site_lan == False:
            return Contact_form

    def get_context_data(self, **kwargs):
        contact_us = ContactUs.objects.all()
        site_lan = self.request.COOKIES.get('site_language')
        user = self.request.COOKIES.get('user_language')
        user_id_last=Contact.objects.order_by('-id').first()
        user_id = (user_id_last.id)+1
        if site_lan is None:
            site_lan = False
        elif site_lan is not None:
            site_lan = eval(site_lan)
        for i in contact_us:
            contact_us_view = i
        contaxt = super(contactView, self).get_context_data(**kwargs)
        contaxt['contact'] = contact_us_view
        contaxt['rtl_fa'] = site_lan
        contaxt['form'] = Contact_form
        return contaxt

    def form_valid(self, form):
        contact: Contact = Contact.objects.filter(read_by_admin=False, response__isnull=False).first()
        site_lan = self.request.COOKIES.get('site_language')
        if site_lan is None:
            site_lan = False
        elif site_lan is not None:
            site_lan = eval(site_lan)
        if contact is not None:
            if site_lan == False:
                send_email_replace('پاسخ تماس با ما', contact.email_contact, {'replay_admin': contact}, 'email.html')
                contact.read_by_admin = True
                contact.save()
                return Contact_form
            elif site_lan:
                send_email_replace('contact us', contact.email_contact, {'replay_admin': contact}, 'en_email.html')
                contact.read_by_admin = True
                contact.save()
                return Contact_form_en
        else:
            return super().form_valid(form)
        return super().form_valid(form)
