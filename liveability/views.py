from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import logging
log = logging.getLogger(__name__)

# Create your views here.

def index(request):
    log.debug("------")
    # return HttpResponse("Hello, world. You're at the polls index.")
    content = {

    }
    log.debug("------")
    return render(request, 'index.html', content)

@csrf_exempt
def form_handle(request):
    # log.debug('======')
    # return HttpResponse("Hello, world. You're at the polls index.")
    hc = request.POST.get('housing_cost')
    dc = request.POST.get('dining_cost')
    log.debug("------")
    log.debug(hc)
    log.debug(dc)


    content = {

    }
    # log.debug('======')
    return render(request, 'index.html', content)
