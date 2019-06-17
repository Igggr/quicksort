import pytest

from merge_sort import merge_sort
from quicksort_pivot import quick_sort

def test_merge_sort(random_list):
    assert merge_sort(random_list) == sorted(random_list)
      
      
def test_quick_sort(random_list):
    quick_sort(random_list)
    assert random_list == sorted(random_list)
