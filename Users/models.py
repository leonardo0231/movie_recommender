from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="user_profile/%Y%m%d/", blank=True, null=True)

    def __str__(self):
        return f"user: {self.user.username}"

