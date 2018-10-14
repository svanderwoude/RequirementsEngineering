from django.contrib import admin
from django.urls import path

from .views import anchoring, authority, thanks


urlpatterns = [
    path('admin/', admin.site.urls),
    path('thanks/', thanks, name='thanks'),

    path('exp/anc/<int:version>/', anchoring, name='anchoring'),
    path('exp/aut/<int:version>/', authority, name='authority'),
]
