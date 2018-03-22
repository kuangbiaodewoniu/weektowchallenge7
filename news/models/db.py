# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: db.py
@time: 2018/03/21 
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@192.168.100.78:3306/51fanli_django'
db = SQLAlchemy(app)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


# 文章表
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category', backref=db.backref('file', lazy='dynamic'))

    def __init__(self, title,created_time,category, content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content

    def __repr__(self):
        return '<File %r>' % self.title


def get_file_data():
    data = {}
    for id, title in db.session.query(File.id, File.title):
        data[id] = title
    return data


def get_data_byid(id):
    result = {}
    data = db.session.query(File.id, File.title, File.created_time, File.content).filter_by(id=id)
    for id, title,created_time,content in data:
        result = {'id': id, 'title':title, 'created_time':created_time, 'content':content}
        return result


if __name__ == '__main__':
    result = get_data_byid(1)
    print(result)




