#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Basic todo list using webpy 0.3 
"""

import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

import web
import model

### Url mappings

urls = (
    "", "Index",
    "/del/(\d+)", "Delete"
)

### Templates
render = web.template.render('todolist/templates', base='base')


class Index:
    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull,
            description='i need to:'),
        web.form.Button('Add todo'),
    )

    def GET(self):
        """ Show page
        """
        todos = model.get_todos()
        form = self.form()
        return render.index(todos, form)

    def POST(self):
        """ Add new entry
        """
        form = self.form()
        if not form.validates():
            todos = model.get_todos()
            return render.index(todos, form)
        model.new_todo(form.d.title)
        raise web.seeother('/')

class Delete:
    
    def GET(self, id):
        id = int(id)
        model.del_todo(id)
        raise web.seeother('/')
        
    
   #def POST(self, id):
   #    """ Delete based on ID
   #    """
   #    id = int(id)
   #    model.del_todo(id)
   #    raise web.seeother('/')

# app = web.application(urls, globals())
app = web.application(urls, locals())


if __name__ == '__main__':
    app.run()
