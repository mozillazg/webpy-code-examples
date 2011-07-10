import web
import view, config
from view import render

urls = (
    '', 'index'
)

class index:
    def GET(self):
        return render.base(view.listing())
        
app = web.application(urls, locals())
app.internalerror = web.debugerror

if __name__ == "__main__":
    app.run()

