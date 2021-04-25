from django.urls import path

from .views import UjianView

app_name = 'exam'
urlpatterns = [
    path('ujian/', UjianView.as_view(), name='ujian'),
]
