from django.contrib import admin
from django.urls import path

from .views import anchoring, authority, rand_anchoring, requirement, thanks


urlpatterns = [
    path('admin/', admin.site.urls),
    path('thanks/', thanks, name='thanks'),

    path('exp/anc/<int:version>/', anchoring, name='anchoring'),
    path('exp/aut/<int:version>/', authority, name='authority'),

    path('exp/req/', requirement, name='requirement'),
    path('exp/req/<int:pk>/', requirement, name='requirement'),

    path('experiment/', rand_anchoring, name='rand_anchoring'),
]
