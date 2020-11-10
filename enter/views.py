from django.shortcuts import render


def enter_view(request, *args, **kwargs):
    context = {
        "title": "Enter",
    }
    return render(request, "pages/main.html", context)
