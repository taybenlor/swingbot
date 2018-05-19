from bottle import route, run, template, request, post, view, static_file

import query

context = None

@route('/')
@view('index')
def index():
    global context
    response, context = query.query()
    return template('index', response=response)

@post('/command')
def command():
    global context
    command = request.forms.get('command')
    response, context = query.query(command, context)
    frontend = context and context.get('frontend')
    return { 'message': response, 'frontend': frontend }

@route('/music/<filename>')
def music_static(filename):
    return static_file(filename, root='music/')

run(host='0.0.0.0', port=8080, server='paste')
