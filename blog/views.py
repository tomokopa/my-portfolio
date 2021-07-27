from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
# forms関連
from .forms import ContactForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def push_timer(request):
    return render(request, 'timer/push_timer.html', {})

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            category = form.cleaned_data['category']
            message = form.cleaned_data['message']
            sender = []
            sender.append(form.cleaned_data['sender'])
            recipients = [settings.EMAIL_HOST_USER]

            try:
                send_mail('【Portfolio Contact】' + subject,
                '【from】' + str(sender) + '\n' + '【category】' + category + '\n\n' + message,
                sender,
                recipients)
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')

            return redirect('contact_complete')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})

def contact_complete(request):
    return render(request, 'contact/contact_complete.html')