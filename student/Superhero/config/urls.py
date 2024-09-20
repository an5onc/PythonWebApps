from django.urls import path
from hero.views import HulkView, StoreView

urlpatterns = [
    path('' ,        HulkView.as_view()),
    path('StoreView/', StoreView.as_view()),
]