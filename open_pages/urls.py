from django.urls import path
from open_pages import views

urlpatterns = [
    path("",views.ListPageAPIView.as_view(),name="page_list"),
]