from flask import request
from flask_paginate import Pagination


def paging(content, number):
    page = request.args.get('page', 1, type=int)
    if page > len(content) or page < 1:
        page = 1
    start = (page - 1) * number
    end = start + number
    slices = slice(start, end)
    sli_content = content[slices]
    if len(content) == 0:
        content = ['', ]
    current_page = Pagination(content, page=page, per_page=number, total=len(content), items=content[page - 1])
    total_page = current_page.total
    context = {
        'content': content,
        'total_page': total_page,
        'sli_content': sli_content,
        'current_page': current_page,
    }
    return context
