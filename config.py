import os

def get_upload_folder():
    return os.environ.get(
        'UPLOAD_FOLDER',
        os.path.join(os.getcwd(), 'static/uploads')
    )