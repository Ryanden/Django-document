from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    # 관계가 대치적으로 형성됨.
    # A 가 B 를 friends 에 추가 -> B의 friend 에도 추가
    friends = models.ManyToManyField(
        'self',
    )

    def __str__(self):
        return self.name
