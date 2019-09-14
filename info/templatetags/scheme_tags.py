from django import template

register = template.Library()


@register.filter(name='scheme_id')  # 过滤器在模板中使用时的name
def scheme_id(value):
    '''返回mongo的_id属性'''
    return value._id
