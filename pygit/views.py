from flask import render_template_string, request
from pygit import app
import hashlib
import time
import os


@app.route('/repository', methods=['POST'])
def save_repository():
    path = _create_md5_folder('storage')
    for file in request.files.values():
        file.save('{0}/{1}'.format(path, file.filename))
    return render_template_string('')


def _create_md5_folder(storage):
    """ Create hash by current time. Then use it for naming new folder. """
    current_dir = os.getcwd()
    md5 = hashlib.md5()
    md5.update(str(time.time()).encode('utf-8'))
    path = '{0}/{1}/{2}'.format(current_dir, storage, md5.hexdigest())
    os.makedirs(path)
    return path
