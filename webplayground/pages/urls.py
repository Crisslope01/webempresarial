from django.urls import path
from .views import PageListView, PageDetailView, PagesCreateView, PagesUpdate



pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PagesCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PagesUpdate.as_view(), name='update'),
], 'pages')



