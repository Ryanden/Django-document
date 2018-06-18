from django.db import models


__all__ = (
    'InstagramUser',
)


class InstagramUser(models.Model):
    name = models.CharField(max_length=50)

    # 내가 follow 하고 있는 사람들의 목록

    following = models.ManyToManyField(
        'self',
        related_name='followers',
        symmetrical=False,
    )

    def __str__(self):
        return self.name

