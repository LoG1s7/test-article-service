from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    SUBSCRIBER = "subscriber"
    AUTHOR = "author"

    ROLE_CHOICES = (
        (SUBSCRIBER, "Subscriber"),
        (AUTHOR, "Author"),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default=SUBSCRIBER
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    @property
    def is_author(self):
        return self.role == self.AUTHOR

    @property
    def is_subscriber(self):
        return self.role == self.SUBSCRIBER

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
