# from flask import Flask, request, send_from_directory
# from flask_cors import CORS
# import smtplib
# import os
# from email.message import EmailMessage

# app = Flask(__name__)
# CORS(app)

# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# EMAIL_ADDRESS = 'kiksymyguy@gmail.com'
# EMAIL_PASSWORD = 'irat fmow onsk zrns'

# @app.route('/')
# def root():
#     return send_from_directory('.', 'index.html')

# @app.route('/submit', methods=['POST'])
# def submit_petition():
#     name = request.form['name']
#     details = request.form['details']
#     company = request.form['company']
#     files = request.files.getlist('attachments')

#     msg = EmailMessage()
#     msg['Subject'] = f'New Petition Against {company}'
#     msg['From'] = EMAIL_ADDRESS
#     msg['To'] = EMAIL_ADDRESS
#     msg.set_content(f"Petition by {name}\n\nCompany: {company}\n\nDetails:\n{details}")

#     for file in files:
#         file_data = file.read()
#         msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file.filename)

#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#         smtp.send_message(msg)

#     return {'status': 'success'}

# @app.route('/data/<path:path>')
# def send_data(path):
#     return send_from_directory('data', path)

# @app.route('/petitions/<path:path>')
# def send_petition(path):
#     return send_from_directory('petitions', path)

# # if __name__ == '__main__':
# #     app.run(debug=True)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, send_from_directory
from flask_cors import CORS
import smtplib
import os
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    raise ValueError("Email credentials are not set in environment variables.")

@app.route('/')
def root():
    return send_from_directory('.', 'index.html')

@app.route('/submit', methods=['POST'])
def submit_petition():
    name = request.form['name']
    details = request.form['details']
    company = request.form['company']
    files = request.files.getlist('attachments')

    msg = EmailMessage()
    msg['Subject'] = f'New Petition Against {company}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(f"Petition by {name}\n\nCompany: {company}\n\nDetails:\n{details}")

    for file in files:
        file_data = file.read()
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file.filename)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    return {'status': 'success'}

@app.route('/data/<path:path>')
def send_data(path):
    return send_from_directory('data', path)

@app.route('/petitions/<path:path>')
def send_petition(path):
    return send_from_directory('petitions', path)

if __name__ == '__main__':
    app.run(debug=True)
