from django.shortcuts import (
    render, get_object_or_404, redirect)
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View

from .models import Republican

# Create your views here.

def homepage(request):
    return render(
        request,
        'index.html',
    )

class SenatorList(View):
    template_name = 'senator_list.html'

    def get(self, request):
        senators = Republican.objects.filter(gov_type='S')
        context = {
            'senators': senators
        }
        return render(
            request,
            self.template_name,
            context
        )


