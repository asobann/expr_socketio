from datetime import datetime
from flask import Flask, render_template
from flask_socketio import SocketIO

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @socketio.on('connection established')
    def handle_connection_established(message):
        print(f'connection established: message={message}')

    @socketio.on('get time')
    def handle_get_time():
        return datetime.now().ctime()

    return socketio, app


socketio, app = create_app()


if __name__ == '__main__':
    socketio.run(app)

