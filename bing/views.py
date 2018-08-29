from django.http import HttpResponse
from django.template import loader
from .models import Images


def index(request):
    imagesPath = Images.objects.all()
    template = loader.get_template('bing/index.html')
    context = {
        'imagesPath': imagesPath
    }
    return HttpResponse(template.render(context, request))


def today(request):
    response = "This is today."
    return HttpResponse(response)


def day(request, day_id):
    response = "Time is %s."
    return HttpResponse(response % day_id)


def last(request):
    last = Images.objects.order_by('startdate')[-1]
    output = '\n'.join(c for c in last.objects)
    return HttpResponse(output)
