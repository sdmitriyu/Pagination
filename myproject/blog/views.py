from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


def post_list(request):
    post_list = Post.objects.all()
    page_size = request.GET.get('page_size', 5)  # значение по умолчанию 5
    paginator = Paginator(post_list, page_size)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'post_list.html', {'page_obj': page_obj})