#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


""" Basic blog using webpy 0.3 """
import web
import model

### Url mappings

urls = (
    '', 'Index',
    '/page/([1-9]\d*)', 'Index',
    '/view/(\d+)', 'View',
    '/new', 'New',
    '/delete/(\d+)', 'Delete',
    '/edit/(\d+)', 'Edit',
)


### Templates
t_globals = {
    'datestr': web.datestr,
    'homepath': '/blog',
}
render = web.template.render('blog/templates', base='base', globals=t_globals)


class Index:

    def GET(self, page=1):
        """ Show page """
        # posts = model.get_posts()
        # return render.index(posts)
        # params = web.input()
        # page = params.page if hasattr(params, 'page') else 1
        page = int(page) # if page else 1
        perpage = 2
        posts, pages = model.get_posts_pages(page, perpage)
        if page > pages:
            raise web.seeother('/')
        else:
            return render.index(posts=posts, pages=pages)

class View:

    def GET(self, id):
        """ View single post """
        post = model.get_post(int(id))
        return render.view(post)


class New:

    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull, 
            size=30,
            description="Post title:"),
        web.form.Textarea('content', web.form.notnull, 
            rows=30, cols=80,
            description="Post content:"),
        web.form.Button('Post entry'),
    )

    def GET(self):
        form = self.form()
        return render.new(form)

    def POST(self):
        form = self.form()
        if not form.validates():
            return render.new(form)
        model.new_post(form.d.title, form.d.content)
        raise web.seeother('/')


class Delete:

    def POST(self, id):
        model.del_post(int(id))
        raise web.seeother('/')


class Edit:

    def GET(self, id):
        post = model.get_post(int(id))
        form = New.form()
        form.fill(post)
        return render.edit(post, form)


    def POST(self, id):
        form = New.form()
        post = model.get_post(int(id))
        if not form.validates():
            return render.edit(post, form)
        model.update_post(int(id), form.d.title, form.d.content)
        raise web.seeother('/')


app = web.application(urls, locals())

if __name__ == '__main__':
    app.run()

