from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
from .models import checkpoint

import os

from mysite.settings import GOOGLE_MAP_API_KEY


class ReactAppView(View):

    def get(self, request):
        try:
            with open(os.path.join(str(settings.BASE_DIR),
                                   'front',
                                   'build',
                                   'index.html')) as file:
                return HttpResponse(file.read())

        except:
            return HttpResponse(status=501, )

def show_map(request):
    checkpoints = checkpoint.objects.filter(checkpoint_id='a')
    context = {'Key': GOOGLE_MAP_API_KEY}
    for temp in checkpoints:
        context["lat"] = temp.latitude
        context["lng"] = temp.longitude

    return render(request,'mapping.html',context)