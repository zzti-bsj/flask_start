import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    # g是什么？ g是一个特殊对象，独立于每一个请求，处理请求过程中存储可能多个函数都会使用的数据。把连接存储于其中，可以多次使用
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # row_factory 是什么？
        # 告诉连接返回类似于字典的行，这样可以通过列名称来操作 数据。
        g.db.row_factory = sqlite3.Row
    
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables"""
    init_db()
    click.echo("Initialized the database.")

def init_app(app):
    # 告诉 Flask 在返回响应后进行清理的时候调用此函数
    app.teardown_appcontext(close_db)
    # 添加一个新的 可以与 flask 一起工作的命令
    app.cli.add_command(init_db_command)
