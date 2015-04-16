import sys
import os

import pybossa

# import utilities from pybossa/test
sys.path.append(os.path.abspath("./pybossa/test"))
import helper
import default
import factories


class TestSched(helper.sched.Helper):

    @default.with_context
    def test_get_task(self):
        pass