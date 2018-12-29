
def walk_pkg_gen(pathObject):
    '''
      Description: Yields pathobject that has only file extension of pks or pkb
    '''

    glob_spec_or_body = '*.pk[sb]'

    for f in pathObject.rglob(glob_spec_or_body):
        yield f
