#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

db = web.database(dbn='postgres', db='todo', user='postgres', pw='py')

def get_todos():
    return db.select('todo', order='id')

def new_todo(text):
    db.insert('todo', title=text)

def del_todo(id):
    db.delete('todo', where="id=$id", vars=locals())
