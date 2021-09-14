from django.urls import path
from polls.views import DetailView, IndeXView, ResultView, vote

app_name ="polls"

urlpatterns = [
    path('', IndeXView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
]