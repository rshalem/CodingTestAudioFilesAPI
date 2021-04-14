from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from audiofiles.views import AudioFileCreateAndReadView, AudioFileReadDetailUpdateDelete

app_name = 'audiofiles'

urlpatterns = [
    path('create/<audioFileType>', AudioFileCreateAndReadView.as_view(), name='create'),
    path('get/<audioFileType>', AudioFileCreateAndReadView.as_view(), name='get-all'),
    path('get/<audioFileType>/<int:pk>', AudioFileReadDetailUpdateDelete.as_view(), name='get-single'),
    path('update/<audioFileType>/<int:pk>', AudioFileReadDetailUpdateDelete.as_view(), name='update'),
    path('delete/<audioFileType>/<int:pk>', AudioFileReadDetailUpdateDelete.as_view(), name='delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
