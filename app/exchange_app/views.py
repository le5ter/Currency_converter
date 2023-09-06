from django.shortcuts import render


def exchange(request):
    name = "Alexey"

    context = {
        'name': name
    }

    return render(request=request, template_name='exchange_app/index.html', context=context)
