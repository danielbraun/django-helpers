import re


def remove_html_tags(string):
    return re.sub('<[^>]*>', '', string)
