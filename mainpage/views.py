from django.shortcuts import HttpResponse, render
from django.core.mail import send_mail

from .forms import RegisterEmail
from .models import User


def landing_page(request):
    if request.method == 'POST':
        form = RegisterEmail(request.POST)

        if form.is_valid():
            name_get = form.cleaned_data.get('form_name')
            mail_get = form.cleaned_data.get('form_email')

            p = User(name=name_get, email=mail_get)
            p.save()

            send_email(name_get, mail_get)
            return HttpResponse('Thank you: {}, we will soon send email to: {} '.format(name_get, mail_get))
    else:
        form = RegisterEmail()

    return render(request, 'mainpage/main_page.html', {'form': form})


def send_email(name, mail):
    content = "Hello, {}. Thank you for dropping your email to our list".format(name)
    send_mail("Email list", content, "ouremailaddress@companyname.com", [mail], fail_silently=False)
