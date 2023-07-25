from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm, ArticlesUpdateForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, "news/news_home.html", {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/update.html'
    form_class = ArticlesUpdateForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена не верно'
    form = ArticlesForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


def update(request):
    error = ''
    if request.method == 'POST':
        update_form = ArticlesUpdateForm(request.POST)
        if update_form.is_valid():
            update_form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена не верно'
    update_form = ArticlesUpdateForm
    data = {
        'form': update_form,
        'error': error
    }
    return render(request, 'news/update.html', data)
