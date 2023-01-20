#!/usr/bin/env python3
import tornado.web
import tornado.ioloop

port = 8888


class home(tornado.web.RequestHandler):
    def get(self):
        self.write("Enter Either Rel/Full")


class fullPath(tornado.web.RequestHandler):
    def get(self):
        self.render("styles.css")


class relPath(tornado.web.RequestHandler):
    def get(self):
        self.render("styles.css")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", home),
        (r"/full", fullPath),
        (r"/rel", relPath)
    ])

    app.listen(port)
    print(f"Running .CSS on {port}")
    tornado.ioloop.IOLoop.current().start()
