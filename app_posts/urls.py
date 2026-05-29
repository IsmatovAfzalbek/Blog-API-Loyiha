from django.urls import path


from .import views


urlpatterns = [ 
    path("post-list/", views.ListCreatedView.as_view(), name="post_list"),
    path("detail/<int:id>/", views.DetailUpdateDelete.as_view(), name="detail"),
]


