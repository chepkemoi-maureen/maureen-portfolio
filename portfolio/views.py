from django.shortcuts import render

# Create your views here.
from django.views import View


class HomeView(View):
    template_name = 'portfolio/index.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)
