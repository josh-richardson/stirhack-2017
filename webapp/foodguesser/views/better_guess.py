import random

from django.http import HttpResponse

from foodguesser.models import Food
from django.contrib.staticfiles.templatetags.staticfiles import static


def random_image(request):
    images = Food.objects.all()
    image = static(str(random.choice(images)))
    return HttpResponse("{'image': '" + image + "'}")

