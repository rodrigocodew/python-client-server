from jinja2 import Environment, FileSystemLoader
from wsgiref.simple_server import make_server

def application(env, start_response):
    headers = [('Content-type', 'text/html')]
    start_response('200 OK', headers)
    
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')

    html = template.render(
        {
            'title': 'Servidor Python',
            'name': 'Rodrigo Luna'
        }
    )

    return [bytes(html, 'utf-8')]

server = make_server('localhost', 8080, application)
server.serve_forever()