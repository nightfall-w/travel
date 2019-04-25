# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Scheme(models.Model):
    """
    套餐类
    """
    name = models.CharField(max_length=200, verbose_name="套餐名")
    coordinate = models.CharField(max_length=50, verbose_name="坐标")
    originating = models.CharField(max_length=20, verbose_name="始发地")
    end_locale = models.CharField(max_length=20, verbose_name="目的地")
    through_time = models.IntegerField(verbose_name="历时天数")
    day = models.IntegerField(verbose_name="白天数")
    night = models.IntegerField(verbose_name="晚上数")
    introduce = models.TextField(verbose_name="套餐介绍")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    favorites = models.ManyToManyField(User, verbose_name="被喜欢", blank=True)
    is_delete = models.BooleanField(choices=((1, 'delete'), (0, 'exist')), default=0, verbose_name="被删除")
    groggery = models.ManyToManyField("Groggery", verbose_name="酒店", blank=True)
    score = models.ManyToManyField("Score", verbose_name="评分", blank=True)
    scenic = models.ManyToManyField('Scenic',verbose_name='相册',blank=True)

    class Meta:
        db_table = 'scheme'
        verbose_name = verbose_name_plural = '旅游项目'

    def __str__(self):
        return self.name


class Scenic(models.Model):
    """
    相册类
    """
    name = models.CharField(max_length=40, verbose_name="照片名")
    image = models.ImageField(upload_to='images/scenic', verbose_name='景点照片')

    class Meta:
        db_table = 'scenic'
        verbose_name = verbose_name_plural = '相册'

    def __str__(self):
        return self.name


class Ticket(models.Model):
    """
    票务类
    """
    scheme = models.ForeignKey(Scheme, verbose_name="套餐对象")
    start_date = models.DateField(verbose_name="出发时间")
    end_date = models.DateField(verbose_name="返程时间")
    surplus = models.IntegerField(verbose_name="剩余票数")
    unit_price = models.IntegerField(verbose_name="当天票价")

    class Meta:
        db_table = 'ticket'
        verbose_name = verbose_name_plural = '票务'

    def __str__(self):
        return self.scheme.name


class Score(models.Model):
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
    score_number = models.IntegerField(choices=SCORE_CHOICES, verbose_name="分数")
    user = models.ManyToManyField(User, verbose_name="评分者")
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1, verbose_name="评分类别")

    class Meta:
        db_table = 'score'
        verbose_name = verbose_name_plural = '评价'

    def __str__(self):
        return str(self.score_number)


class Review(models.Model):
    """
    评论类
    """
    scheme = models.ForeignKey(Scheme, related_name="review_scheme", verbose_name="被评论套餐")
    content = models.TextField(verbose_name="评论内容")
    create = models.DateTimeField(auto_now_add=True, verbose_name="评论发表时间")
    user = models.ForeignKey(User, related_name="review_user", verbose_name="评论者")
    assist = models.BigIntegerField(verbose_name="赞同数")
    oppose = models.BigIntegerField(verbose_name="反对数")

    class Meta:
        db_table = 'review'
        verbose_name = verbose_name_plural = '用户评论'

    def __str__(self):
        return self.scheme.name


class Journey(models.Model):
    """
    行程类
    """
    cafe = models.ForeignKey("Groggery", related_name="journey_groggery", verbose_name="入住酒店")
    time = models.TimeField(verbose_name="行程时间")
    day = models.IntegerField(verbose_name="第几天")
    visit_address = models.CharField(max_length=20, verbose_name="游访地点")
    content = models.TextField("游玩内容")
    scheme = models.ForeignKey(Scheme, verbose_name="所属套餐")

    class Meta:
        db_table = 'journey'
        verbose_name = verbose_name_plural = '行程'

    def __str__(self):
        return self.scheme.name


class Groggery(models.Model):
    """
    酒店类
    """
    name = models.CharField(max_length=30, verbose_name="酒店名")
    image = models.ImageField(upload_to='images/groggery', verbose_name='酒店图片')

    class Meta:
        db_table = 'groggery'
        verbose_name = verbose_name_plural = '酒店'

    def __str__(self):
        return self.name
