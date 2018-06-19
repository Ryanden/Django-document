from django.db import models


__all__ = (
    'TwitterUser',
    'Relation'
)


class TwitterUser(models.Model):
    """
    User 간의 관계는 2종류로 나뉨
        follow
        block

    관계를 나타내는 Relation 클래스 사용 ( 중개 모델)

    """
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
    )

    def __str__(self):
        return self.name

    @property
    def following_relations(self):
        return self.relations_by_from_user.filter(relation_type='f')
        # return Relation.objects.filter(from_user=self, relation_type='f')

    @property
    def block_relations(self):
        return self.relations_by_from_user.filter(relation_type='b')
        # return Relation.objects.filter(from_user=self, relation_type='b')

    @property
    def follower_relations(self):
        # 나를 follow 하고 있는 Relation 들을 리턴
        return self.relations_by_to_user.filter(relation_type='f')


class Relation(models.Model):
    """

    TwitterUser 간의 MTM 관계를 정의
        from_user
        to_user
        follow 인지, block 인지를 판단

    """
    CHOICES_RELATION_TYPE = {
        ('f', 'Follow'),
        ('b', 'Block'),
    }

    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_from_user'
    )

    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_to_user'
    )

    relation_type = models.CharField(
        max_length=1,
        choices=CHOICES_RELATION_TYPE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # get_foo_display foo 함수를 적용
        return 'from({}), to({}), {}'.format(
            self.from_user.name,
            self.to_user.name,
            # RELATION TYPE 의 오른쪽 메시지를 출력
            self.get_relation_type_display()
        )
