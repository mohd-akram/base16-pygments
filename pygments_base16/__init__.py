from os import path
from glob import glob
from string import capwords
from importlib import import_module


for filename in glob(path.join(path.dirname(__file__), 'base16-*.py')):
    module_name = path.splitext(path.basename(filename))[0]
    class_name = '{}Style'.format(capwords(module_name, '-').replace('-', ''))
    module = import_module('.{}'.format(module_name), __name__)
    globals()[class_name] = getattr(module, class_name)
