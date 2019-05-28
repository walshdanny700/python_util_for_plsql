
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


def walk_pkg_body(pathObject):
    '''
        Description: Yields pathobject that has file extension of pkb
    '''
    package_body = '*.pkb'

    for f in pathObject.rglob(package_body):
        yield f


def commits_in_package(pathObject):
    '''
       Description: The commit of transactions should be in the service layer.
                            Any commits in the DB code makes it harder to test.
   '''

    COMMIT_STRING = 'commit;'

    for package_body_file in walk_pkg_body(pathObject):
        if COMMIT_STRING in package_body_file.read_text().lower():
            yield package_body_file
