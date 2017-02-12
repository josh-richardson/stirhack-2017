import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','webapp.settings')

import django
django.setup()

import random
from foodguesser.models import Food, Score

first_names = ["David", "John", "Peter", "Simon", "Fred", "Maverick", "Edmund", "Francais","Gordon","Wesley",
     "Adam","Joshua","Tom","Ethan","Mark","Vik","Dan","Jorge","Randy","Aaron", "Alphonse", "Andre", "Martin",
     "Callum", "Conor", "Mohammed","Jim", "Kevin", "Sarah","Kate","Catherine","Mary","Francais","Shelly","Dot","Mel","Rachel","Kerry","Alice","Ruby",
     "Emma","Olivia","Eve","Ava","Isabella","Mia","Lily","Charlotte","Amelia","Claire","Victoria","Amy",
     "Joanne", "Hannah","Lucy","Kay","Mystique","Raven","Chelsea"
]

def populate():
    imagedir = "./static/images/populate/"
    imageprefix = "images/populate/"
    images = [f for f in os.listdir(imagedir) if os.path.isfile(os.path.join(imagedir, f))]

    for img in images:
        calories = (int)(img.split(".")[0].split("_")[0])
        print(img + ":" + str(calories) + "\n")
        add_food(imageprefix+img, calories)

    for user in range(0, 10):
        username = random.choice(first_names)
        score = random.randint(0, 100)
        add_score(username, score)


def add_score(username, score):
    s, created = Score.objects.get_or_create(username=username, score=score, guess_count=10)
    s.save()
    return s


def add_food(image, calories):
    f, created = Food.objects.get_or_create(image=image, calories=calories)
    f.save()
    return f


if __name__=="__main__":
    populate()
