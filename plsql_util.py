import os


def walk_pkg_gen(root_dir):
    '''
      Description: Yields only file extension of pks and pkb
    '''
    ext_spec = '.pks'
    ext_body = '.pkb'
    for root, _, anyfile in os.walk(root_dir):
        extension = os.path.splitext(anyfile)
        if extension in (ext_spec, ext_body):
            yield root, anyfile
