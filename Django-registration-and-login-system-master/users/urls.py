from django.urls import path
from .views import home, profile, RegisterView,aboutus, contactus, login, singup, video, exam, payment, note,result,q1

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('aboutus/', aboutus, name='users-aboutus'),
    path('contactus/', contactus, name='users-contactus'),
    path('login/', login, name='users-login'),
    path('singup/', singup, name='users-singup'),
    path('video/<int:id>', video, name='users-video'),
    path('exam',exam,name="exam"),
    path('payment/<int:id>',payment, name='users-payment'),
    path('note/<int:id>', note, name='users-note'),
    path('q1/<int:id>', q1, name='users-q1'),
    path('result',result,name="users-result"),
]
