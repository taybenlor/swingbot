from bottle import route, run, template

import query

context = None

@route('/')
def index():
    global context
    greeting = 'Hello! I can record the BPM of a song or play a song at a given BPM.'
    response, context = query.query()
    return template('<strong>{{greeting}}</strong><p>{{response}}</p>', greeting=greeting, response=response)

@route('/<command>')
def command(command):
    global context
    response, context = query.query(command, context)
    return template('<p>{{response}}</p>', response=response)

run(host='0.0.0.0', port=8080)
