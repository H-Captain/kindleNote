from flask import render_template, redirect, url_for

from . import main
from .. import db
from .. import modles

# @app.route('/')
# def showMark():
#     # todo: ������ݿ��б�ĵ���
#     db = get_db()
#     cur = db.execute('select id,name,content from book order by id')
#     entries = cur.fetchall()
#     return render_template('showMark.html', items=entries)

@main.route('/')
def index():
    return render_template('showMark.html')