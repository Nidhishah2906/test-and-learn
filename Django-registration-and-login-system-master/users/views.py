from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import Course,Exam,Result

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm


def home(request):
    data = Course.objects.all()
    context = {
        'data':data,
    }
    return render(request, 'users/home.html',context)

def exam(request):
    return render(request,'users/q3-py.html')

def aboutus(request):

    return render(request, 'users/aboutus.html')

def contactus(request):
    return render(request, 'users/contactus.html')

def login(request):
    return render(request, 'users/login.html')

def singup(request):
    return render(request, 'users/singup.html')

def video(request,id):
    data = Course.objects.filter(pk=id)
    context = {
        'data':data,
    }
    return render(request,'users/video.html',context)

def payment(request,id):
    data = Course.objects.filter(pk=id)
    context = {
        'data':data,
    }
    return render(request, 'users/payment.html',context)

def note(request,id):
    data = Course.objects.filter(pk=id)
    context = {
        'data':data,
    }
    return render(request, 'users/note.html',context)

def q1(request,id):
    data = Exam.objects.filter(Course=id)
    context = {
        "data":data,
        "id":id,
    }
    return render(request, 'users/q1.html',context)

def result(request):
    if request.method == "POST":
        id = request.POST.get('id')
        # opt1 = request.POST.get('opt1')
        # opt2 = request.POST.get('opt2')
        # opt3 = request.POST.get('opt3')
        # opt4 = request.POST.get('opt4')
        # opt5 = request.POST.get('opt5')
        # opt6 = request.POST.get('opt6')
        # opt7 = request.POST.get('opt7')
        # opt8 = request.POST.get('opt8')
        # opt9 = request.POST.get('opt9')
        # opt10 = request.POST.get('opt10')
        # opt11 = request.POST.get('opt11')
        # opt12 = request.POST.get('opt12')
        # opt13 = request.POST.get('opt13')
        # opt14 = request.POST.get('opt14')
        # opt15 = request.POST.get('opt15')
        data5 = Course.objects.filter(id=id)
        for i in data5:
            course = i.Course
        name = request.POST.get('name')
        data = Exam.objects.all()
        count = 0
        c = 1
        for i in data:
            c = str(c)
            if i.answer == request.POST.get('opt'+c):
                c = int(c)
                c +=1
                count +=1
        result1 = 100*count/15
        obj = Result(name=name,course=course,result=result1)
        obj.save()
    
        data2=Result.objects.all()[:1]
        context = {
            "data2":data2,
        }
        return render(request,'users/result.html',context)
    return render(request,'users/result.html')

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})
