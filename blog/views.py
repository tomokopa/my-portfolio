from django.shortcuts import render, redirect

# forms関連
from .forms import ContactForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail


def top(request):
    return render(request, 'blog/top.html', {})

def works_portfolio(request):
    return render(request, 'works/portfolio.html', {})

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
                '【from】' + str(sender) + '\n' + '【name】' + subject + '\n' + '【category】' + category + '\n\n' + message,
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