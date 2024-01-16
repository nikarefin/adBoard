from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import ConfirmationCode
from .forms import RegistrationForm
from django.core.mail import send_mail
from random import randint
from django.contrib.auth.models import Group


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=email, email=email,
                                            password=password)
            authorized_users = Group.objects.get(name="Authorized")
            user.groups.add(authorized_users)
            user.is_active = False
            user.save()

            code = str(randint(1000, 9999))
            ConfirmationCode.objects.create(email=email, code=code)

            send_mail(
                'Подтверждение почты',
                f'Ваш код подтверждения: {code}',
                'your_email@example.com',
                [email],
                fail_silently=False,
            )

            return redirect('confirm_code', email=email)
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def confirm_code(request, email):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            confirmation_code = ConfirmationCode.objects.get(email=email,
                                                             code=code)
            user = User.objects.get(email=email)
            user.is_active = True
            user.save()
            confirmation_code.delete()
            login(request, user)
            return redirect('ads')
        except ConfirmationCode.DoesNotExist:
            pass

    return render(request, 'accounts/confirm_code.html', {'email': email})


def resend_code(request, email):
    code = str(randint(1000, 9999))
    ConfirmationCode.objects.create(email=email, code=code)

    send_mail(
        'Подтверждение почты',
        f'Ваш новый код подтверждения: {code}',
        'your_email@example.com',
        [email],
        fail_silently=False,
    )

    return redirect('confirm_code', email=email)

