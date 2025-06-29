from flask import Flask, request, session, jsonify, make_response

app = Flask(__name__)
app.json.compact = False
app.secret_key = b'?w\x85Z\x08Q\xbdO\xb8\xa9\xb65Kj\xa9_'  # Used to sign session cookies

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome! Try visiting /sessions/hello to see cookie and session data."
    })

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):
    # Set session values only if they don't already exist
    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

    # Prepare response with session and cookie info
    response = make_response(jsonify({
        'session': {
            'session_key': key,
            'session_value': session.get(key),
            'session_accessed': session.accessed,
        },
        'cookies': [
            {cookie: request.cookies[cookie]} for cookie in request.cookies
        ],
    }), 200)



    response.set_cookie('mouse', 'Cookie')

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
