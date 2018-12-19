from python_util_for_plsql import plsql_util as putil
import os
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
    yield dir_test
    shutil.rmtree(dir_test, ignore_errors=True)


def test_walk_pkg_gen(setup_test_files):
    for _, cur_file in putil.walk_pkg_gen(setup_test_files):
        _, ext = os.path.splitext(cur_file)
        assert ext != '.txt'


def test_walk_pkg_gen_size(setup_test_files):
    assert len(list(putil.walk_pkg_gen(setup_test_files))) == 2


def test_walk_pkg_gen_ext(setup_test_files):
    for _, cur_file in putil.walk_pkg_gen(setup_test_files):
        _, ext = os.path.splitext(cur_file)
        assert ext in ['.pks', '.pkb']


def test_walk_pkg_gen_file_name(setup_test_files):
    for _, cur_file in putil.walk_pkg_gen(setup_test_files):
        name, _ = os.path.splitext(cur_file)
        assert name == 'test_pkg'


def test_walk_root_gen(setup_test_files):
    for root, _ in putil.walk_pkg_gen(setup_test_files):
        assert root == str(setup_test_files)
