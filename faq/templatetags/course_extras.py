from django import template
from django.utils.safestring import mark_safe

import markdown2

from courses.models import Question


register = template.Library() 

@register.simple_tag
def newest_question():
    '''Gets the most recent course that was added to the library'''
    return Question.objects.latest('created_at')


@register.inclusion_tag('faq/faq_nav.html')
def nav_faq_index(): 
    '''Returns dictionary of courses to display as navigation pane'''
    courses = Question.objects.all()[:5]
    return {'questions': questions}


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''Converts markdown text to HTML'''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)