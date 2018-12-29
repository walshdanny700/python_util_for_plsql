from plsqlutil import plsql_util as putil
import pathlib
import pytest
import shutil


test_filenames = ['test_pkg.pks', 'test_pkg.pkb', 'exclude.txt']


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


def test_missing_slash_count(setup_missing_slash):
    assert len(list(putil.missing_slash_in_pkg(setup_missing_slash))) == 1


def test_missing_slash_spec(setup_missing_slash):
    for item in putil.missing_slash_in_pkg(setup_missing_slash):
        assert item.suffix == '.pks'


def test_walk_pkg_gen(setup_test_files):
    for pathObject in putil.walk_pkg_gen(setup_test_files):
        assert pathObject.suffix != '.txt'


def test_walk_pkg_gen_size(setup_test_files):
    assert len(list(putil.walk_pkg_gen(setup_test_files))) == 2


def test_walk_pkg_gen_ext(setup_test_files):
    for pathObject in putil.walk_pkg_gen(setup_test_files):
        assert pathObject.suffix in ['.pks', '.pkb']


def test_walk_pkg_gen_file_name(setup_test_files):
    for pathObject in putil.walk_pkg_gen(setup_test_files):
        assert pathObject.stem == 'test_pkg'


def test_walk_root_gen(setup_test_files):
    for pathObject in putil.walk_pkg_gen(setup_test_files):
        assert pathObject.parent == setup_test_files
