from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import uvicorn

class HttpServer:
	def __init__(self, host="127.0.0.1", port=8000):
		self.host = host
		self.port = port
		self.app = FastAPI()
		self.static_dir = os.path.join(os.path.dirname(__file__), 'static')

		self.app.mount("/static", StaticFiles(directory=self.static_dir), name="static")

		@self.app.get("/", response_class=HTMLResponse)
		async def home():
			with open(os.path.join(self.static_dir, 'index.html'), 'r') as file:
				content = file.read()
			return HTMLResponse(content=content)

		@self.app.get("/page1", response_class=HTMLResponse)
		async def page1():
			with open(os.path.join(self.static_dir, 'page1.html'), 'r') as file:
				content = file.read()
			return HTMLResponse(content=content)

	def start(self):
		uvicorn.run(self.app, host=self.host, port=self.port)

server = HttpServer()
