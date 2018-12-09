import plsql_util as putil
import os


cur_dir = os.path.dirname(os.path.realpath(__file__))
dir_test = 'test'
location = os.path.join(cur_dir, dir_test)


def test_walk_pkg_gen():
    for _, cur_file in putil.walk_pkg_gen(location):
        _, ext = os.path.splitext(cur_file)
        assert ext != '.txt'


def test_walk_pkg_gen_size():
    assert len(list(putil.walk_pkg_gen(location))) == 2


def test_walk_pkg_gen_ext():
    for _, cur_file in putil.walk_pkg_gen(location):
        _, ext = os.path.splitext(cur_file)
        assert ext in ['.pks', '.pkb']


def test_walk_pkg_gen_file_name():
    for _, cur_file in putil.walk_pkg_gen(location):
        name, _ = os.path.splitext(cur_file)
        assert name == 'test_pkg'


def test_walk_root_gen():
    for root, _ in putil.walk_pkg_gen(location):
        assert root == location
