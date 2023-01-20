#!/usr/bin/env python3
import tornado.web
import tornado.ioloop

port = 8080

class basicRequestHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello world!")

class staticRequestHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("C:/Users/user/Desktop/html/Project 1/index.html")



if __name__ == "__main__":
	app = tornado.web.Application([
		(r"/", basicRequestHandler),
		(r"/site", staticRequestHandler)
	])

	app.listen(port)
	print(f"Listening on {port}")
	tornado.ioloop.IOLoop.current().start()



