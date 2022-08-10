import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('liang', __name__, url_prefix='/liang')

# views code
# -------------------

@bp.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        return '待处理！'
    if request.method == 'GET':
        result = {}
        result['title'] = '离校扫码凭证'
        result['name'] = '勾朝亮'
        result['number'] = '2010302019'
        result['major'] = ''
        result['info1'] = '当天出校进校申请\n离校不离邕'
        result['info2'] = '可以离校'
        result['remind'] = '温馨提醒：请于离校当天23:30前返校，超过时间将不能扫码返校。'
        result['time'] = '2022-7-31 17:30:50'

        result['yuelaiyuexingle'] = '疫情防控 人人有责 仿冒凭证 依法必究'
        return result