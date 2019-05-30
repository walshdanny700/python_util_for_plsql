from sqlLinter import sqlLinter as lint
import pathlib
import pytest
import shutil


test_filenames = ['test_pkg.pks',
                  'test_pkg.pkb',
                  'exclude.txt',
                  'package_body_b.pkb']


@pytest.fixture()
def setup_test_files(tmpdir):
    dir_test = tmpdir / "dir_test"
    dir_test.mkdir()
    for name in test_filenames:
        file_name = dir_test / name
        file_name.write(str("content"))
    yield pathlib.Path(dir_test)
    shutil.rmtree(str(dir_test))


@pytest.fixture()
def setup_missing_slash(tmpdir):
    dir_test = tmpdir / "dir_test"
    dir_test.mkdir()
    spec = dir_test / test_filenames[0]
    spec.write(str("content"))
    body = dir_test / test_filenames[1]
    body.write(str("content \n /"))
    yield pathlib.Path(dir_test)
    shutil.rmtree(str(dir_test))


@pytest.fixture()
def setup_package_with_commit(tmpdir):
    dir_test = tmpdir / "dir_test"
    dir_test.mkdir()
    spec = dir_test / test_filenames[0]
    spec.write(str("content"))
    body = dir_test / test_filenames[1]
    body.write(str("commit; \n /"))
    body_b = dir_test / test_filenames[3]
    body_b.write(str("content \n /"))
    yield pathlib.Path(dir_test)
    shutil.rmtree(str(dir_test))


def test_missing_slash_count(setup_missing_slash):
    assert len(list(lint.missing_slash_in_pkg(setup_missing_slash))) == 1


def test_missing_slash_spec(setup_missing_slash):
    for item in lint.missing_slash_in_pkg(setup_missing_slash):
        assert item.suffix == '.pks'


def test_walk_pkg_gen(setup_test_files):
    for pathObject in lint.walk_pkg_gen(setup_test_files):
        assert pathObject.suffix != '.txt'


def test_walk_pkg_gen_size(setup_test_files):
    assert len(list(lint.walk_pkg_gen(setup_test_files))) == 3


def test_walk_pkg_gen_ext(setup_test_files):
    for pathObject in lint.walk_pkg_gen(setup_test_files):
        assert pathObject.suffix in ['.pks', '.pkb']


def test_walk_pkg_gen_file_name(setup_test_files):
    for pathObject in lint.walk_pkg_gen(setup_test_files):
        assert pathObject.stem in ['test_pkg', 'package_body_b']


def test_walk_root_gen(setup_test_files):
    for pathObject in lint.walk_pkg_gen(setup_test_files):
        assert pathObject.parent == setup_test_files


def test_walk_pkg_body(setup_test_files):
    '''
       Description: GIVEN walk_pkg_body WHEN it returns a pathObject
                            THEN the suffix is not .txt or .pks
    '''

    for pathObject in lint.walk_pkg_body(setup_test_files):
        assert pathObject.suffix not in ['.txt', '.pks']


def test_walk_pkg_body_happy_path(setup_test_files):
    '''
         Description: GIVEN walk_pkg_body WHEN it returns a pathObject
                              THEN the suffix is .pkb
    '''

    for pathObject in lint.walk_pkg_body(setup_test_files):
        assert pathObject.suffix == '.pkb'


def test_commits_in_package_happy_path(setup_package_with_commit):
    '''
       Description: GIVEN a package body
                            WHEN package body has a commit
                            THEN yield the package file object
    '''

    for pathObject in lint.commits_in_package(setup_package_with_commit):
        assert pathObject.stem == 'test_pkg'


def test_commits_in_package_path_b(setup_package_with_commit):
    '''
       Description: GIVEN a package body
                            WHEN package body has a commit
                            THEN dont yield files that do not contain commit
    '''

    for pathObject in lint.commits_in_package(setup_package_with_commit):
        assert pathObject.stem not in ['package_body_b',  'exclude']
        assert pathObject.suffix not in ['.txt', '.pks']


def test_commits_in_package_expected_suffix(setup_package_with_commit):
    '''
       Description: GIVEN a package body
                            WHEN package body has a commit
                            THEN suffix is pkb
    '''

    for pathObject in lint.commits_in_package(setup_package_with_commit):
        assert pathObject.suffix == '.pkb'
