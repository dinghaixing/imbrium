# 中文等utf8 url转换为标准url
from urllib import parse
url = parse.quote(chinese_url, safe='!@#$%^&*()_+|~-=`<>?:"}{[];,./\\')

