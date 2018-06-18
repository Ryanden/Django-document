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

    def show_friends(self):
        # 이한영의 친구목록

        print(f'{self.name}의 친구목록')
        friend_list = ''

        for friend in self.friends.all():
            friend_list += f'- {friend.name}\n'
        print(len(self.friends.all()), '명')
        print(friend_list)
