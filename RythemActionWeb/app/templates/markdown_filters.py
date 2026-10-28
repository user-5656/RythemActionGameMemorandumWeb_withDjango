# blog/templatetags/markdown_filters.py
import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def render_markdown(text):
  # markdown文字列をHTMLに変換し、安全なHTMLとしてマークする
  html = markdown.markdown(text, extensions=['extra', 'codehilite'])
  return mark_safe(html)
