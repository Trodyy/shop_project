from django import template
import humanize
register = template.Library()

@register.simple_tag(name='super_discount')
def super_discount(price , discount) :
    new_price = price - ((price*discount)/100)
    return humanize.intcomma(int(new_price))