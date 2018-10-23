from django.contrib import admin
from django.urls import path

from .views import anchoring, authority, rand_anchoring, thanks


urlpatterns = [
    path('admin/', admin.site.urls),
    path('thanks/', thanks, name='thanks'),

    path('exp/anc/<int:version>/', anchoring, name='anchoring'),
    path('exp/aut/<int:version>/', authority, name='authority'),

    path('experiment/', rand_anchoring, name='rand_anchoring'),
]
