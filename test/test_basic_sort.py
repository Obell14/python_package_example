# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================
import pytest
import numpy as np
from basic_sort_3977.int_sort import bubble, quick, insertion


def is_sorted(int_list):
    """
    Testing oracle.
    """
    return int_list == sorted(int_list)


@pytest.fixture
def int_lists():
    '''
    List of lists to run as pytest fixtures, testing the sorting algorithms we 
    designed
    '''
    return [
        # Sorted list
        [1, 2, 3],
        # Reversed list
        [3, 2, 1],
        # List with duplicate elements
        [1, 1, 1, 1, 1],
        # List with a mix of positive and negative numbers
        [-5, 2, -8, 9, 0],
        # List with only one element
        [42],
        # Empty list
        [],

        # # TODO: THIS EXAMPLE FAILS BUT SHOULDN'T
        # # Random list generated using NumPy
        # list(np.random.randint(low=-10, high=200, size=5)),

        # # TODO: BELOW, WRITE TEST INPUTS THAT SHOULD FAIL, AND ENSURE THEY DO FAIL
        # # String input
        # "hi I am a string!",
        # # Single char input
        # "q",
        # # Empty string input
        # "",
        # # Decimal input
        # [0.2, 5.4234156, 0.000000001, -99.9],
        # # Mixed input
        # [6, 2, "oop", 74],
        # # 2D lists
        # [[8,5,2],[82,3]],
        # # 2D empty lists
        # [[]],
        # [[],[]]

    ]

'''
For each sorting algorithm we will test all of the pytest fixtures
'''
# Test the bubble sort algorithm
def test_bubble(int_lists):
    for example in int_lists:
        sorted_list = bubble(example.copy())
        assert is_sorted(sorted_list)


# Test the quick sort algorithm
def test_quick(int_lists):
    for example in int_lists:
        sorted_list = quick(example.copy())
        assert is_sorted(sorted_list)


# Test the insertion sort algorithm
def test_insertion(int_lists):
    for example in int_lists:
        sorted_list = insertion(example.copy())
        assert is_sorted(sorted_list)
