import pytest
from py_algo_practice.two_pointer.detect_cycle_linked_list import *


def test_returnsTrueIfCycleExists():
    noCycleList = ListNode(1)
    cycleExists = detectCycle(noCycleList)
    assert cycleExists == False


