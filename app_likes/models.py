from django.db import models

from app_accounts.models import CustomUser
from app_posts.models import Post


class Likes(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")

    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, verbose_name="Post")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")


    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likelar"

        unique_together = ['user', 'post']


    def __str__(self):
        return f"{self.user} - {self.post}"