import pytest
from py_algo_practice.two_pointer.detect_cycle_linked_list import *


def test_returnsTrueIfCycleExists():
    cycleExists = detectCycle(noCycleList)
    noCycleList = ListNode(1)
    assert cycleExists == False


