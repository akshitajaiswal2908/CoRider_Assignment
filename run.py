from flask import Flask
from app import create_app
from app.routes import user_blueprint

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
