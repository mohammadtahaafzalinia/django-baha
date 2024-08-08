from django import template
from googletrans.client import Translator
register=template.Library()

@register.filter
def trans(value):
    g = Translator().translate(value).text
    return g

@register.filter
def trans_fa(value):
    g = Translator().translate(value,dest='fa').text
    return g

@register.filter
def cut_replac(value):
    return value.replace('_',' ')
