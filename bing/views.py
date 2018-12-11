from django.http import HttpResponse
from django.template import loader
from .models import Images
from django.http import Http404
from django.shortcuts import render

# bing/templates/css
def index(request):
    imagesPath = Images.objects.all()
    template = loader.get_template('bing/index.html')
    context = {
        'imagesPath': imagesPath
    }
    return HttpResponse(template.render(context, request))


def index2(request):
    imagesPath = Images.objects.all()
    template = loader.get_template('index.html')
    context = {
        'imagesPath': imagesPath
    }
    return HttpResponse(template.render(context, request))


def today(request):
    response = "This is today."
    return HttpResponse(response)


def day(request, day_id):
    # response = "Time is %s."
    # return HttpResponse(response % day_id)
    try:
        image = Images.objects.all()[day_id]
    except Images.DoesNotExist:
        print('404 error')
        raise Http404("Image does not exist")
    return render(request, 'bing/day.html', {'image': image})


def last(request):
    last = Images.objects.order_by('startdate')[-1]
    output = '\n'.join(c for c in last.objects)
    return HttpResponse(output)


def detail(request):
    return
