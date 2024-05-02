from flask import Flask, render_template, url_for, request, send_from_directory
import os

def create_app(): 

    app = Flask(__name__)
    upload_folder = 'uploads'
    app.config['UPLOAD_FOLDER'] = upload_folder

    upload_folder = 'uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)


    from .views import data_view
    app.register_blueprint(data_view.databp)
    
    @app.route('/')
    def index():
        return "<h1>It's Time</h1>"

    @app.route('/user/<name>')
    def userinfo(name):
        return render_template('temp.html', name=name)
    
    @app.route('/upload_file', methods=['POST'])
    def upload_file():
        if 'file' not in request.files or 'image' not in request.files:
            return "NO FILE", 400
            
        file = request.files['file']
        image = request.files['image']

        if file.filename == '' or image.filename == '':
            return "NOT SELECTED", 400
            
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        image_filename = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)

        file.save(filename)
        image.save(image_filename)

    # 업로드된 이미지의 경로 생성
        uploaded_image_path = url_for('static', filename=f'uploads/{image.filename}')

        return render_template('save_data.html', uploaded_image_path=uploaded_image_path)


    @app.route('/download/<filename>', methods=['GET'])
    def download_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

    with app.test_request_context():
        print(url_for(endpoint='static', filename='css/style_1.css'))
        print(url_for(endpoint='static', filename='image/jellyfish.png'))

    return app
