import plsql_util as putil
from itertools import islice
import os


def test_walk_pkg_gen():
    dir_test = 'test'
    location = os.path.join(os.path.abspath(__file__), dir_test)
    for item in islice(putil.walk_pkg_gen(location), 2):
        _, ext = os.path.splitext(item)
        assert ext != '.txt'
