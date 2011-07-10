#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import todolist.todo
import blog.blog
import skeleton.code
import wiki.wiki

urls = (
    "/(.*)/", "Redirect",
    "/todo", todolist.todo.app,
    '/blog', blog.blog.app,
    '/skeleton', skeleton.code.app,
    '/wiki', wiki.wiki.app,
    "/.*", "Index"
)
render = web.template.render('templates', base='base')


class Redirect:
    def GET(self, path):
        web.seeother('/' + path)


class Index:
    def GET(self):
        pages = {
                "todo": '/todo',
                'blog': '/blog',
                'skeleton': '/skeleton',
                'wiki': '/wiki'
                }
        return render.index(pages)

app = web.application(urls, locals())

if __name__ == "__main__":
    app.run()
