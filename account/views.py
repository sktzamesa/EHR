from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(
        request,
        'home.html'
    )

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Extracting data from the form
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create a new user with the provided username, email, and password
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = name
            user.save()

            # Log the user in and redirect to the homepage
            login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'patient_dashboard.html')
    else:
        return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'patient_dashboard.html', {'username': request.user.username})

