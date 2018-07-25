from django.contrib.auth import authenticate, login, logout, get_user_model
User = get_user_model()
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm, LoginForm, RegisterForm


def home_page(request):
    context = {
        'title': 'Home Page!',
        'premium_content': 'Yeahh'
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {'title': 'About Page!'}
    return render(request, 'home_page.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {'title': 'Contact Page!',
               'form': contact_form}

    if contact_form.is_valid():
       print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, 'contact/view.html', context)


def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {'form': login_form}
    print("User logged in")
    print(request.user.is_authenticated)

    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        # return HttpResponse('hello')

        if user is not None:
            login(request, user)
            # context['form'] = LoginForm()
        else:
            print("Error")
    return render(request, 'account/login.html', context)



def register_page(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user =  User.objects.create_user(username, email, password)
    return render(request, "account/register.html", {'form': form})