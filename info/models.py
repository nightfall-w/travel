# -*- coding:utf-8 -*
import mongoengine


class User(mongoengine.Document):
    uid = mongoengine.IntField(required=True)
    username = mongoengine.StringField(required=True)


class Review(mongoengine.EmbeddedDocument):
    """
    评论类
    """
    content = mongoengine.StringField(verbose_name="评论内容")
    create = mongoengine.DateTimeField(verbose_name="评论发表时间")
    user = mongoengine.ReferenceField(User, related_name="review_user", verbose_name="评论者")

    class Meta:
        db_table = 'review'
        verbose_name = verbose_name_plural = '用户评论'


class Scenic(mongoengine.EmbeddedDocument):
    """
    相册类
    """
    name = mongoengine.StringField(max_length=40, verbose_name="照片名")
    path = mongoengine.StringField(verbose_name='景点照片')

    class Meta:
        db_table = 'scenic'
        verbose_name = verbose_name_plural = '相册'


class Score(mongoengine.EmbeddedDocument):
    """
    评分类
    """
    SCORE_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]

    CATEGORY_CHOICES = [
        (1, '清洁度'),
        (2, '服务'),
        (3, '舒适'),
        (4, '条件'),
    ]
    score_number = mongoengine.IntField(choices=SCORE_CHOICES, verbose_name="分数", default=4)
    user = mongoengine.ReferenceField(User, verbose_name="评分者")
    category = mongoengine.IntField(choices=CATEGORY_CHOICES, default=1, verbose_name="评分类别")

    class Meta:
        db_table = 'score'
        verbose_name = verbose_name_plural = '评价'


class Journey(mongoengine.EmbeddedDocument):
    """
    行程类
    """
    hotel = mongoengine.StringField(verbose_name="入住酒店", max_length=600, null=True)
    time = mongoengine.StringField(verbose_name="行程时间", null=True)
    day = mongoengine.IntField(verbose_name="第几天")
    visit_address = mongoengine.StringField(max_length=300, verbose_name="游访地点")
    content = mongoengine.StringField()
    scenics = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Scenic))

    class Meta:
        db_table = 'journey'
        verbose_name = verbose_name_plural = '行程'


class Ticket(mongoengine.EmbeddedDocument):
    """
    票务类
    """
    start_date = mongoengine.DateField(verbose_name="出发时间")
    end_date = mongoengine.DateField(verbose_name="返程时间")
    surplus = mongoengine.IntField(verbose_name="剩余票数")
    unit_price = mongoengine.IntField(verbose_name="当天票价")

    class Meta:
        db_table = 'ticket'
        verbose_name = verbose_name_plural = '票务'


class Scheme(mongoengine.Document):
    """
    套餐类
    """
    name = mongoengine.StringField(max_length=200, verbose_name="套餐名")
    coordinate = mongoengine.StringField(max_length=50, verbose_name="坐标", null=True)
    originating = mongoengine.StringField(max_length=20, verbose_name="始发地")
    end_locale = mongoengine.StringField(max_length=20, verbose_name="目的地")
    day = mongoengine.IntField(verbose_name="白天数")
    night = mongoengine.IntField(verbose_name="晚上数")
    introduce = mongoengine.StringField(verbose_name="套餐介绍")
    feature = mongoengine.StringField(verbose_name='特色')
    contains_content = mongoengine.StringField(verbose_name='包含内容')
    create_date = mongoengine.DateTimeField(verbose_name="创建时间")
    favorites = mongoengine.ListField(mongoengine.ReferenceField(User), verbose_name="被喜欢", blank=True)
    is_delete = mongoengine.BooleanField(choices=((True, 'delete'), (False, 'exist')), default=False,
                                         verbose_name="被删除")
    score = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Score), verbose_name='所有评分')
    review = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Review), verbose_name='用户评论')
    review_number = mongoengine.IntField(verbose_name='评论数')
    journeys = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Journey), verbose_name='行程安排')
    tickets = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Ticket), verbose_name='票务')
    min_price = mongoengine.IntField(verbose_name='最低价')
    avg_score = mongoengine.FloatField(verbose_name='平均评分')
    first_photo = mongoengine.StringField(verbose_name='缩略图')

    # min_price = mongoengine.IntField('最低价')
    class Meta:
        db_table = 'scheme'
        verbose_name = verbose_name_plural = '旅游项目'
