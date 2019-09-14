# -*- coding:utf-8 -*
import mongoengine


class User(mongoengine.Document):
    uid = mongoengine.IntField(required=True)
    username = mongoengine.StringField(required=True)
    favorites = mongoengine.ListField()


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


class VisitAddress(mongoengine.EmbeddedDocument):
    """
    景点坐标
    """
    name = mongoengine.StringField(verbose_name="景点名", max_length=60)
    coordinate = mongoengine.StringField(verbose_name="坐标", max_length=60)

    class Meta:
        db_table = 'visit_address'
        verbose_name = verbose_name_plural = '景点坐标'


class Journey(mongoengine.EmbeddedDocument):
    """
    行程类
    """
    hotel = mongoengine.StringField(verbose_name="入住酒店", max_length=600, null=True)
    time = mongoengine.StringField(verbose_name="行程时间", null=True)
    day = mongoengine.IntField(verbose_name="第几天")
    visit_address = mongoengine.StringField(max_length=300, verbose_name="游访地点")
    content = mongoengine.StringField(verbose_name="游玩内容", max_length=600)

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
    _id = mongoengine.ObjectIdField(verbose_name='id')
    title = mongoengine.StringField(max_length=200, verbose_name="套餐名")
    departure = mongoengine.StringField(max_length=20, verbose_name="始发地")
    subhead = mongoengine.StringField(max_length=200, verbose_name="子标题")
    destination = mongoengine.StringField(max_length=20, verbose_name="目的地")
    day = mongoengine.IntField(verbose_name="白天数")
    night = mongoengine.IntField(verbose_name="晚上数")
    intro = mongoengine.StringField(verbose_name="套餐介绍")
    include = mongoengine.StringField(verbose_name='包含内容')
    favorites = mongoengine.ListField(mongoengine.ReferenceField(User), verbose_name="被喜欢", blank=True)
    is_delete = mongoengine.BooleanField(choices=((True, 'delete'), (False, 'exist')), default=False,
                                         verbose_name="被删除")
    ticket_month = mongoengine.ListField(mongoengine.StringField(), verbose_name="票务月份")
    scenic_images = mongoengine.ListField(mongoengine.StringField(), verbose_name="景点照片")
    scores = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Score), verbose_name='所有评分')
    review = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Review), verbose_name='用户评论')
    journeys = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Journey), verbose_name='行程安排')
    tickets = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Ticket), verbose_name='票务')
    price = mongoengine.IntField(verbose_name='最低价')
    avg_score = mongoengine.FloatField(verbose_name='平均评分')

    class Meta:
        db_table = 'scheme'
        verbose_name = verbose_name_plural = '旅游项目'
