from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.showSignUpForm),
    path('CalcForm', views.showCalc),
    path('Results', views.showRes),
    path('SignUp', views.SignUp),
    path('Calc_butterfly', views.Calc_butterfly),
    path('data', views.checkUserDatas)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)