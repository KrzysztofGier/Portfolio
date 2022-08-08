from django.urls import path
from infos.views import home, me, contact

urlpatterns = [
   path('', home),
   path('me/', me),
   path('contact/', contact)
]