# Simple skeleton file for running tests on our project

from nose.tools import *
from sorting.tools import *
import random

def test_insertion_sort() :
    l =  [0, 2, 1, -2.3, 40, 100, 3, 5]
    insertion_sort(l)
    assert_equals(l, [-2.3, 1, 2, 0, 3, 5, 40, 100])
    nums = []
    for i in range(10) :
        nums.append(tNum(random.randint(1,20)))
    print nums
    insertion_sort(nums)
    assert_equals([i.num for i in sorted(nums)], [i.num for i in nums])

def test_tNum_class() :
    my_num = tNum(10)
    assert_equals(my_num, tNum(10))
    assert_equals(my_num < tNum(11), True)
    assert_equals(my_num == tNum(10), True)
    assert_equals(my_num == tNum(-10), False)

