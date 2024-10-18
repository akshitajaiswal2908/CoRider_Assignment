from flask import Flask
from app import create_app
from app.routes import user_blueprint
# Create the Flask app
app = create_app()

app.register_blueprint(user_blueprint, url_prefix='')

if __name__ == '__main__':
    # Run the app in debug mode for easier error tracking
    app.run(debug=True, host='127.0.0.1', port=5000)
