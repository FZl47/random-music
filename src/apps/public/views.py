from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'public/index.html'
