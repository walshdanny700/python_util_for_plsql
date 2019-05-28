
def walk_pkg_gen(pathObject):
    '''
      Description: Yields pathobject that has only file extension of pks or pkb
    '''
    glob_spec_or_body = '*.pk[sb]'

    for f in pathObject.rglob(glob_spec_or_body):
        yield f


def missing_slash_in_pkg(pathObject):
    '''
      Description: Yields pathobject of package files that are missing
        the required slash at end of file for the given directory passed in
    '''

    for pkgFile in walk_pkg_gen(pathObject):
        if pkgFile.read_text().rstrip()[-1] != '/':
            yield pkgFile
