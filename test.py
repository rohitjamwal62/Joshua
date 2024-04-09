import json,requests,shutil,time,asyncio

try:
    from . import Innovation
    from . import Informatique
    from . import Research

except:
    import Innovation
    import Informatique
    import Research
from logger import error_log
import docx
import random
from docx.shared import Pt
from docx.shared import RGBColor
from flask import Flask, render_template, request, send_file, send_from_directory, after_this_request, logging, \
    current_app

from scholarly import scholarly
import random
from docx.shared import Pt
import docx.enum.text
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os, sys
import threading
import datetime

current_year = datetime.datetime.now().year
app = Flask(__name__)
generated_files = []
for filename in os.listdir('files'):
    file_path = os.path.join('files', filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print(f'Failed to delete {file_path}. Reason: {e}')

@app.route('/')
def index():
    return render_template('index.html')

threads = []
async def process_file(file, index, project_type):
    if file.filename != '':
        filename = f"sample_{index + 1}.docx"
        filenames_real = file.filename
        file.save(filename)
        await create_document(index + 1, project_type, filenames_real)


# @app.route('/thanks',methods=['POST'])
# def thanks():
#     return render_template('thanks.html', files=generated_files)


@app.route('/upload', methods=['POST'])
async def upload():
    # client_name = request.form.get('name')
    files = request.files.getlist('files[]')
    project_types = request.form.getlist('projectType[]')  # Get the list of project types
    # threads = []
    for index, file in enumerate(files):
        project_type = project_types[index] if index < len(project_types) else 'Default'
        await process_file(file, index, project_type)
    #     thread = threading.Thread(target=process_file, args=(file, index, project_type))
    #     threads.append(thread)
    #     thread.start()

    # for thread in threads:
    #     thread.join()
    print("ALL DONE ####################################")
    print(generated_files)
    return render_template('thanks.html')


@app.route('/thanks')
def thanks():
    # Assuming 'generated_files' is accessible here, otherwise you might need to adjust
    return render_template('thanks.html', files=generated_files)

@app.route('/view_log')
def view_log():
    try:
        error_log = open(os.path.join(os.getcwd(), 'logs', 'error_logs.txt'), 'r')
        error_log_str = error_log.read()
        return str(error_log_str)
    except Exception as e:
        return str(e)

async def create_document(index, project_type, filename_real):
    try:
        if project_type == "R&D":
            print("111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
            file = Research.create_document(index, filename_real)
            generated_files.append(file)
        elif project_type == "Informatique":
            print("2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222")
            file = Informatique.create_document(index, filename_real)
            generated_files.append(file)
        elif project_type == "Innovation":
            print("3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333")
            file = Innovation.create_document(index, filename_real)
            generated_files.append(file)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        error = str(exc_type) + ' ' + str(fname) + ' ' + str(exc_tb.tb_lineno)
        error_log(error)


@app.route('/download/<filename>')
def download_file(filename):
    directory = current_app.root_path  # Adjust based on your setup
    # file_path = os.path.join(directory, filename)
    file_path = f"files/{filename}"
    print(f"Attempting to send file from path: {file_path}")  # Debugging line
    current_app.logger.debug(f"Attempting to send file from path: {file_path}")

    # Security check to prevent directory traversal attacks
    if '..' in filename or filename.startswith('/'):
        return "Invalid filename", 400

    # Check if the file exists to prevent FileNotFoundError
    if not os.path.exists(file_path):
        return "File not found", 404

    # Attempt to delete the file after sending it
    @after_this_request
    def remove_file(response):
        try:
            os.remove(file_path)
            current_app.logger.info(f"Successfully removed {file_path}")
        except Exception as error:
            current_app.logger.error(f"Error removing file after download: {error}")
        return response

    # Stream the file content directly
    try:
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        current_app.logger.error(f"Error sending file: {e}")
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        error = str(exc_type) + ' ' + str(fname) + ' ' + str(exc_tb.tb_lineno)
        error_log(error)
        return "Error sending file", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)