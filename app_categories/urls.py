from django.urls import path


from .import views


urlpatterns = [
    path("list/", views.CategoryListView.as_view(), name="ViewList"),
    path("create/", views.CategoryCreateView.as_view(), name="Create"),
    path("detail/<int:id>/", views.CategoryDetailView.as_view(), name="Detail"),
]