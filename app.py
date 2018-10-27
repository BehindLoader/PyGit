from pygit import app
import os


if not os.path.isdir('storage'):
    current_dir = os.getcwd()
    os.makedirs('{0}/storage'.format(current_dir))
