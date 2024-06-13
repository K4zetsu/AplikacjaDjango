from django.urls import path
from .views import *

urlpatterns = [
    path('',main_p),
    path('cennik/',price,name='price_url'),
    path('faq/',faq),
    path('kontakt/',kontakt),
    path('o_nas/',o_nas),
]
