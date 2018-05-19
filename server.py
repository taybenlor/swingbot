from bottle import route, run, template, request, post, view, static_file

import query

import google_assistant

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

@route('/google-assistant', method='ANY')
def g_assistant():
    global context
    if request.json:
        command = '. '.join('. '.join(raw_input['query'] for raw_input in input['rawInputs']) for input in request.json['inputs'])
    else:
        command = None
    response, context = query.query(command, context)
    return google_assistant.say(response)

run(host='0.0.0.0', port=8080, server='paste')
