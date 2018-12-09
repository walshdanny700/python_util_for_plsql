import plsql_util as putil
import os


def test_walk_pkg_gen():
    dir_test = 'test'
    location = os.path.join(os.path.abspath(__file__), dir_test)
    for _, cur_file in putil.walk_pkg_gen(location):
        _, ext = os.path.splitext(cur_file)
        assert ext != '.txt'


def test_walk_pkg_gen_ext():
    dir_test = 'test'
    location = os.path.join(os.path.abspath(__file__), dir_test)
    for _, cur_file in putil.walk_pkg_gen(location):
        _, ext = os.path.splitext(cur_file)
        assert ext in ['.pks', '.pkb']


def test_walk_root_gen():
    dir_test = 'test'
    location = os.path.join(os.path.abspath(__file__), dir_test)
    for root, _ in putil.walk_pkg_gen(location):
        assert root == location
