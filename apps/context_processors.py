from apps.home.models import userProfile
from agenda import settings

def user_image(request):
    try:
        imagen = None
        user = request.user
        up = userProfile.objects.get(user=user)
        imagen = up.photo
    except:
        imagen = "static/img/photo.jpg"
    return imagen


def my_processors(requests):
    context = {
        "get_image_profile":user_image(requests),
    }
    return context