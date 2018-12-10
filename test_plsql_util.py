import plsql_util as putil
import os
import pytest


cur_dir = os.path.dirname(os.path.realpath(__file__))
dir_test = 'test'
location = os.path.join(cur_dir, dir_test)
test_filenames = ['test_pkg.pks', 'test_pkg.pkb', 'exclude.txt']


@pytest.fixture
def setup_test_files():
    os.makedirs(location)
    for name in test_filenames:
        with open(os.path.join(location, name), 'w+'):
            pass
    yield
    for name in test_filenames:
        os.remove(os.path.join(location, name))
    os.rmdir(location)


def test_walk_pkg_gen(setup_test_files):
    for _, cur_file in putil.walk_pkg_gen(location):
        _, ext = os.path.splitext(cur_file)
        assert ext != '.txt'


def test_walk_pkg_gen_size(setup_test_files):
    assert len(list(putil.walk_pkg_gen(location))) == 2


def test_walk_pkg_gen_ext(setup_test_files):
    for _, cur_file in putil.walk_pkg_gen(location):
        _, ext = os.path.splitext(cur_file)
        assert ext in ['.pks', '.pkb']


def test_walk_pkg_gen_file_name(setup_test_files):
    for _, cur_file in putil.walk_pkg_gen(location):
        name, _ = os.path.splitext(cur_file)
        assert name == 'test_pkg'


def test_walk_root_gen(setup_test_files):
    for root, _ in putil.walk_pkg_gen(location):
        assert root == location
