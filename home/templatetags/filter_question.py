from django import template

register = template.Library()


@register.filter
def filter_question(choices, question_id):
    return choices.filter(question_id=question_id)


