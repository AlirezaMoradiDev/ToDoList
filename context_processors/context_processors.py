from home.models import Information


def footer(request):
    information = Information.objects.all().last()

    return {'information': information}

