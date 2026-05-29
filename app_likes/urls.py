from django.urls import path


from . import views


urlpatterns = [
    path( "likes/",views.CreateListView.as_view(),name="like_list_create"),
    path( "detail-like/<int:id>/",views.DetailDeleteView.as_view(),name="like_detail_delete"),
]