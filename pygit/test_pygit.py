from pygit.views import _create_md5_folder
from flask import Flask, request
import os
import shutil


app = Flask(__name__)
storage_path = os.getcwd() + '/test_storage'
os.makedirs(storage_path)


def test_save_repository():
    files = {
        'file': open('test.txt', 'wb+')
    }
    path = _create_md5_folder('test_storage')
    with app.test_client() as c:
        c.post('/repository', data=files)
        for file in request.files.values():
            file.save('{0}/{1}'.format(path, file.filename))
    assert len(os.listdir(path)) == 1


def test_clean():
    """ Remove folder/file created for testing. """
    shutil.rmtree(storage_path)
    os.remove('test.txt')
