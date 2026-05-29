from django.urls import path


from .import views


urlpatterns = [
    path("comments/", views.CommentListCreateView.as_view(), name="comment_list_create"),
    path("comments/<int:id>/", views.DetailUpdateDelete.as_view(), name="comment_detail_update_delete"),
]