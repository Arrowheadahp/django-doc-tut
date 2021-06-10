from django.urls import path
from django.urls.resolvers import URLPattern

from .views import indexView, resultsView, detailView, vote

app_name = 'polls'
urlpatterns = [
    path('', indexView.as_view(), name='index'),
    path('<int:pk>/', detailView.as_view(), name='detail'),
    path('<int:pk>/results/', resultsView.as_view(), name='results'),
    path('<int:pk>/vote/', vote, name='vote'),
    
]