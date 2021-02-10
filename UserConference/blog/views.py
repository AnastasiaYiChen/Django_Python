from django.shortcuts import render, redirect

from .forms import CreateListForm
from .models import Post, Eventsview, Selection


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    events = {
        'eventsview': Eventsview.objects.all()
    }
    print(Eventsview.objects.count)
    return render(request, 'blog/about.html', events)


def selections(request):
    select = {
        'selections': Selection.objects.all()
    }
    if request.method == 'POST':
        form = CreateListForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('selection')
    else:
        form = CreateListForm()
    return render(request, 'blog/selection.html', {'form': form, 'myselect': select})