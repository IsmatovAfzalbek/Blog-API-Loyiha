from django.urls import path


from .import views


urlpatterns = [
    path("sign-up/", views.SignUpView.as_view(), name="sign_up"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("profile/", views.ProfileView.as_view(), name="profile_view"),
    path("profile-update/<int:id>/", views.ProfileUpdateView.as_view(), name="profile_update"),
    path("logout/", views.LogoutView.as_view(), name="user_logout"),
]