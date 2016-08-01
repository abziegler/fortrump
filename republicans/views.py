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

class SenatorDetail(View):
    template_name = 'senator_detail.html'

    def get(self, request):
        senator = get_object_or_404(Republican, slug__iexact=slug)
        return render(
            request,
            'senator_detail.html',
            {'senator': senator}
        )


class RepresentativeList(View):
    template_name = 'representative_list.html'

    def get(self, request):
        representatives = Republican.objects.filter(gov_type='R')
        context = {
            'representatives': representatives
        }
        return render(
            request,
            self.template_name,
            context
        )

