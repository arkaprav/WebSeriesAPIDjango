from django.urls import path
from .views import *

urlpatterns = [
    path('webseries/list', WebSeriesListAV.as_view(), name='webseries_list'),
    path('webseries/<int:pk>', SingleWebSeriesAV.as_view(), name='single_webseries'),
    path('platform/list', StreamPlatformListAV.as_view(), name='stream_platform'),
    path('platform/<int:pk>', SingleStreamPlatformAV.as_view(), name='single_platform'),
    path('webseries/<int:pk>/review', ReviewListAV.as_view(), name='review_list'),
    path('webseries/<int:pk>/post-review', ReviewCreateAV.as_view(), name='review_post'),
    path('webseries/review/<int:pk>', SingleReviewAV.as_view(), name='single_review'),
]