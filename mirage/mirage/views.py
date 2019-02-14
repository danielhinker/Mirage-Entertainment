from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext


class IndexView(TemplateView):
    template_name = "index.html"

class HireView(TemplateView):
    template_name = "hiring.html"
