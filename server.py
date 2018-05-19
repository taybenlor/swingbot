from bottle import route, run, template, request, post

import query

context = None

@route('/')
def index():
    global context
    response, context = query.query()
    return template('''
        <p><strong>Hello! I can record the BPM of a song or play a song at a given BPM.</strong></p>
        <p>{{response}}</p>
        <form action="/command" method="post">
            <label>
                <input style="width: 200px" type="text" name="command">
            </label>
            <input type="submit">
        </form>
    ''', response=response)

@post('/command')
def command():
    global context
    command = request.forms.get('command')
    response, context = query.query(command, context)
    return template('''
        <p>{{response}}</p>
        <form action="/command" method="post">
            <label>
                <input style="width: 200px" type="text" name="command">
            </label>
            <input type="submit">
        </form>
    ''', response=response)

run(host='0.0.0.0', port=8080)
