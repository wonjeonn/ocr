import os
from flask import Flask
from app.routes import main_bp

app = Flask(__name__)
app.register_blueprint(main_bp)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['STATIC_FOLDER'] = 'static'

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
