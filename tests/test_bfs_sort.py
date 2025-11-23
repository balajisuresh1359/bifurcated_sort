import random
import pytest
from bifurcated_sort import bfc_sort

# ============ BASIC TESTS ============

def test_basic_sorting():
    arr = [3, 1, 2]
    bfc_sort(arr)
    assert arr == [1, 2, 3]

def test_duplicates():
    arr = [4, 4, 2, 1]
    bfc_sort(arr)
    assert arr == [1, 2, 4, 4]

def test_already_sorted():
    arr = [1, 2, 3, 4]
    bfc_sort(arr)
    assert arr == [1, 2, 3, 4]

def test_reverse_sorted():
    arr = [5, 4, 3, 2, 1]
    bfc_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_single():
    arr = [10]
    bfc_sort(arr)
    assert arr == [10]

def test_empty():
    arr = []
    bfc_sort(arr)
    assert arr == []

def test_two_elements():
    arr = [2, 1]
    bfc_sort(arr)
    assert arr == [1, 2]

def test_two_elements_sorted():
    arr = [1, 2]
    bfc_sort(arr)
    assert arr == [1, 2]

# ============ DUPLICATE TESTS ============

def test_all_duplicates():
    arr = [5, 5, 5, 5, 5]
    bfc_sort(arr)
    assert arr == [5, 5, 5, 5, 5]

def test_many_duplicates():
    arr = [3, 1, 2, 3, 1, 2, 3, 1, 2]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_duplicates_at_extremes():
    arr = [1, 5, 1, 3, 5, 2, 1, 5]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

# ============ NEGATIVE NUMBER TESTS ============

def test_negative_numbers():
    arr = [-3, -1, -7, 2, 5]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_all_negative():
    arr = [-5, -10, -1, -3]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_negative_duplicates():
    arr = [-2, -2, -1, -5, -1]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_negative_and_positive():
    arr = [-10, 5, -3, 8, 0, -1, 3]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_zero_included():
    arr = [0, -1, 1, -2, 2]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_multiple_zeros():
    arr = [0, 5, 0, -3, 0, 2]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

# ============ FLOAT TESTS ============

def test_float_numbers():
    arr = [3.2, 1.5, 2.8]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_float_and_int_mix():
    arr = [4.5, 2, 3.1, 1]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_float_precision():
    arr = [1.1, 1.11, 1.111, 1.0, 1.01]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_negative_floats():
    arr = [-3.5, -1.2, -5.8, -2.0]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

# ============ EDGE CASES ============

def test_min_max_at_ends():
    """Min and max are already at start/end"""
    arr = [1, 5, 3, 4, 2, 10]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_min_max_at_beginning():
    """Min and max both at beginning"""
    arr = [1, 10, 5, 3, 7, 2]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_min_max_adjacent():
    """Min and max are next to each other"""
    arr = [5, 1, 10, 3, 7]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_alternating_high_low():
    """Alternating between high and low values"""
    arr = [1, 100, 2, 99, 3, 98, 4, 97]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_sawtooth_pattern():
    """Sawtooth ascending-descending pattern"""
    arr = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_mountain_pattern():
    """Mountain: low to high to low"""
    arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_valley_pattern():
    """Valley: high to low to high"""
    arr = [5, 4, 3, 2, 1, 2, 3, 4, 5]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

# ============ SIZE TESTS ============

def test_small_array():
    arr = [3, 1, 4, 1, 5]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_medium_array():
    arr = list(range(100, 0, -1))
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_large_random():
    arr = [random.randint(-100000, 100000) for _ in range(5000)]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_very_large_array():
    """Test with 50,000 elements"""
    arr = [random.randint(-10000, 10000) for _ in range(50000)]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

# ============ PENDING PARAMETER TESTS ============

def test_pending_parameter_variations():
    """Test different pending_item_percentage values"""
    arr = [15, 3, 8, 1, 12, 6, 20, 4, 18, 2, 14, 10]
    for p in [0.1, 0.2, 0.3, 0.4, 0.5, 0.55, 0.6, 0.7, 0.8, 0.9]:
        arr_copy = arr.copy()
        bfc_sort(arr_copy, pending_item_percentage=p)
        assert arr_copy == sorted(arr), f"Failed with pending_item_percentage={p}"

def test_pending_parameter_minimum():
    """Test with very small percentage"""
    arr = [5, 1, 4, 2, 3]
    bfc_sort(arr, pending_item_percentage=0.01)
    assert arr == [1, 2, 3, 4, 5]

def test_pending_parameter_maximum():
    """Test with very large percentage"""
    arr = [5, 1, 4, 2, 3]
    bfc_sort(arr, pending_item_percentage=0.99)
    assert arr == [1, 2, 3, 4, 5]

def test_pending_on_large_array():
    """Test pending parameter on larger arrays"""
    for p in [0.3, 0.5, 0.7]:
        arr = [random.randint(0, 1000) for _ in range(1000)]
        expected = sorted(arr)
        bfc_sort(arr, pending_item_percentage=p)
        assert arr == expected

# ============ RANDOM STRESS TESTS ============

def test_multiple_random_runs():
    """Run 50 random tests"""
    for _ in range(50):
        arr = [random.randint(-1000, 1000) for _ in range(200)]
        expected = sorted(arr)
        bfc_sort(arr)
        assert arr == expected

def test_extreme_stress():
    """Stress test with 20,000 elements"""
    arr = [random.randint(-10**9, 10**9) for _ in range(20000)]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_random_lengths():
    """Test various random array lengths"""
    for length in [5, 10, 50, 100, 500, 1000, 5000]:
        arr = [random.randint(-1000, 1000) for _ in range(length)]
        expected = sorted(arr)
        bfc_sort(arr)
        assert arr == expected

def test_worst_case_pending():
    """Generate input that maximizes pending items"""
    # Middle values that don't fit either end
    arr = list(range(50, 150)) + [1] + [200]
    random.shuffle(arr)
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

# ============ SPECIAL VALUE TESTS ============

def test_large_numbers():
    """Test with very large integers"""
    arr = [10**15, 10**14, 10**16, 10**13]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_small_numbers():
    """Test with very small integers"""
    arr = [-10**15, -10**14, -10**16, -10**13]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_sparse_range():
    """Large gaps between numbers"""
    arr = [1, 1000, 2, 999, 3, 998]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_tight_range():
    """Small range with many duplicates"""
    arr = [random.randint(0, 5) for _ in range(100)]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

# ============ TUPLE/COMPARABLE TESTS ============

def test_tuple_sorting():
    """Test sorting tuples (by first element)"""
    arr = [(3, 'a'), (1, 'b'), (2, 'c')]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_tuple_with_duplicates():
    """Test tuples with duplicate first elements"""
    arr = [(3, 'a'), (3, 'b'), (1, 'c'), (2, 'd'), (3, 'e')]
    bfc_sort(arr)
    # Check first elements are sorted
    assert [x[0] for x in arr] == [1, 2, 3, 3, 3]

# ============ PROPERTY TESTS ============

def test_output_length_unchanged():
    """Ensure output has same length as input"""
    arr = [random.randint(0, 100) for _ in range(100)]
    original_len = len(arr)
    bfc_sort(arr)
    assert len(arr) == original_len

def test_output_contains_same_elements():
    """Ensure output contains same elements (counting duplicates)"""
    arr = [random.randint(0, 50) for _ in range(100)]
    from collections import Counter
    original_counts = Counter(arr)
    bfc_sort(arr)
    sorted_counts = Counter(arr)
    assert original_counts == sorted_counts

def test_idempotent():
    """Sorting twice gives same result"""
    arr = [random.randint(0, 100) for _ in range(50)]
    bfc_sort(arr)
    first_result = arr.copy()
    bfc_sort(arr)
    assert arr == first_result

# ============ COMPARISON TESTS ============

def test_matches_builtin_sort():
    """Compare with Python's built-in sort on 100 random arrays"""
    for _ in range(100):
        arr = [random.randint(-1000, 1000) for _ in range(random.randint(10, 200))]
        expected = sorted(arr)
        bfc_sort(arr)
        assert arr == expected

# ============ ERROR HANDLING TESTS ============

def test_non_comparable_raises_error():
    """Test that non-comparable types raise appropriate error"""
    arr = [1, "string", 3]
    with pytest.raises(TypeError):
        bfc_sort(arr)

def test_none_in_list():
    """Test behavior with None values"""
    arr = [3, None, 1, 2]
    with pytest.raises(TypeError):
        bfc_sort(arr)

# ============ PERFORMANCE MARKERS ============

@pytest.mark.slow
def test_performance_50k():
    """Performance test with 50,000 elements (marked as slow)"""
    arr = [random.randint(-100000, 100000) for _ in range(50000)]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

@pytest.mark.slow
def test_performance_100k():
    """Performance test with 100,000 elements (marked as slow)"""
    arr = [random.randint(-100000, 100000) for _ in range(100000)]
    expected = sorted(arr)
    bfc_sort(arr)
    assert arr == expected

def test_pending_percentage_default():
    """Test with default pending percentage (0.55)"""
    arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    bfc_sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_pending_percentage_low():
    """Test with low pending percentage (0.1)"""
    arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    bfc_sort(arr, pending_item_percentage=0.1)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_pending_percentage_high():
    """Test with high pending percentage (0.9)"""
    arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    bfc_sort(arr, pending_item_percentage=0.9)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_pending_percentage_variations():
    """Test multiple pending percentages"""
    arr = [15, 3, 8, 1, 12, 6, 20, 4, 18, 2, 14, 10]
    for p in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
        test_arr = arr.copy()
        bfc_sort(test_arr, pending_item_percentage=p)
        assert test_arr == sorted(arr), f"Failed with pending_item_percentage={p}"

def test_pending_percentage_minimum():
    """Test with minimum valid percentage"""
    arr = [5, 2, 8, 1, 9]
    bfc_sort(arr, pending_item_percentage=0.01)
    assert arr == [1, 2, 5, 8, 9]

def test_pending_percentage_maximum():
    """Test with maximum percentage (1.0)"""
    arr = [5, 2, 8, 1, 9]
    bfc_sort(arr, pending_item_percentage=1.0)
    assert arr == [1, 2, 5, 8, 9]

def test_pending_percentage_invalid_zero():
    """Test that 0 percentage raises error"""
    arr = [5, 2, 8]
    with pytest.raises(ValueError, match="must be between 0 and 1"):
        bfc_sort(arr, pending_item_percentage=0)

def test_pending_percentage_invalid_negative():
    """Test that negative percentage raises error"""
    arr = [5, 2, 8]
    with pytest.raises(ValueError, match="must be between 0 and 1"):
        bfc_sort(arr, pending_item_percentage=-0.1)

def test_pending_percentage_invalid_over_one():
    """Test that percentage > 1 raises error"""
    arr = [5, 2, 8]
    with pytest.raises(ValueError, match="must be between 0 and 1"):
        bfc_sort(arr, pending_item_percentage=1.5)

def test_pending_percentage_large_array():
    """Test pending percentage on large array"""
    arr = [random.randint(0, 1000) for _ in range(1000)]
    expected = sorted(arr)
    for p in [0.2, 0.5, 0.8]:
        test_arr = arr.copy()
        bfc_sort(test_arr, pending_item_percentage=p)
        assert test_arr == expected

# ============ INPLACE TESTS ============

def test_inplace_true():
    """Test inplace=True modifies original array"""
    arr = [5, 2, 8, 1, 9]
    bfc_sort(arr, inplace=True)
    assert arr == [1, 2, 5, 8, 9] 

def test_inplace_false():
    """Test inplace=False returns new array"""
    arr = [5, 2, 8, 1, 9]
    result = bfc_sort(arr, inplace=False)
    assert arr == [5, 2, 8, 1, 9]  # Original unchanged
    assert result == [1, 2, 5, 8, 9]  # Returns sorted copy

def test_inplace_default():
    """Test default inplace behavior (should be True)"""
    arr = [5, 2, 8, 1, 9]
    bfc_sort(arr)
    assert arr == [1, 2, 5, 8, 9]  # Original modified by default

def test_inplace_false_multiple_arrays():
    """Test inplace=False on multiple arrays"""
    arr1 = [5, 2, 8]
    arr2 = [9, 1, 4]
    
    result1 = bfc_sort(arr1, inplace=False)
    result2 = bfc_sort(arr2, inplace=False)
    
    # Originals unchanged
    assert arr1 == [5, 2, 8]
    assert arr2 == [9, 1, 4]
    
    # Results sorted
    assert result1 == [2, 5, 8]
    assert result2 == [1, 4, 9]

def test_inplace_false_returns_different_reference():
    """Test that inplace=False returns different array object"""
    arr = [5, 2, 8, 1, 9]
    result = bfc_sort(arr, inplace=False)
    assert result is not arr  # Different object reference

def test_inplace_with_reverse():
    """Test inplace with reverse parameter"""
    arr = [5, 2, 8, 1, 9]
    bfc_sort(arr, inplace=True, reverse=True)
    assert arr == [9, 8, 5, 2, 1]

def test_not_inplace_with_reverse():
    """Test inplace=False with reverse parameter"""
    arr = [5, 2, 8, 1, 9]
    result = bfc_sort(arr, inplace=False, reverse=True)
    assert arr == [5, 2, 8, 1, 9]  # Original unchanged
    assert result == [9, 8, 5, 2, 1]

def test_inplace_empty_array():
    """Test inplace with empty array"""
    arr = []
    result = bfc_sort(arr, inplace=False)
    assert arr == []
    assert result == []

def test_inplace_single_element():
    """Test inplace with single element"""
    arr = [5]
    result = bfc_sort(arr, inplace=False)
    assert arr == [5]
    assert result == [5]

# ============ REVERSE TESTS ============

def test_reverse_false_default():
    """Test default reverse=False behavior"""
    arr = [5, 2, 8, 1, 9]
    bfc_sort(arr)
    assert arr == [1, 2, 5, 8, 9]

def test_reverse_true():
    """Test reverse=True sorts in descending order"""
    arr = [5, 2, 8, 1, 9]
    bfc_sort(arr, reverse=True)
    assert arr == [9, 8, 5, 2, 1]

def test_reverse_ascending_then_descending():
    """Test sorting same array ascending then descending"""
    arr = [5, 2, 8, 1, 9]
    
    # Ascending
    bfc_sort(arr, reverse=False)
    assert arr == [1, 2, 5, 8, 9]
    
    # Descending
    bfc_sort(arr, reverse=True)
    assert arr == [9, 8, 5, 2, 1]

def test_reverse_with_duplicates():
    """Test reverse with duplicate values"""
    arr = [5, 2, 8, 2, 5, 1, 8]
    bfc_sort(arr, reverse=True)
    assert arr == [8, 8, 5, 5, 2, 2, 1]

def test_reverse_with_negatives():
    """Test reverse with negative numbers"""
    arr = [-5, 2, -8, 1, -3]
    bfc_sort(arr, reverse=True)
    assert arr == [2, 1, -3, -5, -8]

def test_reverse_already_sorted():
    """Test reverse on already sorted array"""
    arr = [1, 2, 3, 4, 5]
    bfc_sort(arr, reverse=True)
    assert arr == [5, 4, 3, 2, 1]

def test_reverse_already_reverse_sorted():
    """Test reverse on already reverse sorted array"""
    arr = [5, 4, 3, 2, 1]
    bfc_sort(arr, reverse=True)
    assert arr == [5, 4, 3, 2, 1]

def test_reverse_with_floats():
    """Test reverse with float values"""
    arr = [5.5, 2.2, 8.8, 1.1, 9.9]
    bfc_sort(arr, reverse=True)
    assert arr == [9.9, 8.8, 5.5, 2.2, 1.1]

def test_reverse_large_array():
    """Test reverse on large array"""
    arr = [random.randint(0, 1000) for _ in range(1000)]
    expected = sorted(arr, reverse=True)
    bfc_sort(arr, reverse=True)
    assert arr == expected

def test_reverse_empty_array():
    """Test reverse with empty array"""
    arr = []
    bfc_sort(arr, reverse=True)
    assert arr == []

def test_reverse_single_element():
    """Test reverse with single element"""
    arr = [5]
    bfc_sort(arr, reverse=True)
    assert arr == [5]

def test_reverse_two_elements():
    """Test reverse with two elements"""
    arr = [5, 2]
    bfc_sort(arr, reverse=True)
    assert arr == [5, 2]

# ============ COMBINED PARAMETER TESTS ============

def test_all_parameters_combined():
    """Test all parameters together"""
    arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    result = bfc_sort(
        arr,
        pending_item_percentage=0.4,
        inplace=False,
        reverse=True,
    )
    assert arr == [5, 2, 8, 1, 9, 3, 7, 4, 6]  # Original unchanged
    assert result == [9, 8, 7, 6, 5, 4, 3, 2, 1]

def test_pending_percentage_with_reverse():
    """Test pending_item_percentage with reverse"""
    arr = [15, 3, 8, 1, 12, 6, 20, 4, 18, 2, 14, 10]
    for p in [0.2, 0.5, 0.8]:
        test_arr = arr.copy()
        bfc_sort(test_arr, pending_item_percentage=p, reverse=True)
        assert test_arr == sorted(arr, reverse=True)

def test_all_parameters_large_array():
    """Test all parameters on large array"""
    arr = [random.randint(-1000, 1000) for _ in range(500)]
    result = bfc_sort(
        arr,
        pending_item_percentage=0.3,
        inplace=False,
        reverse=True,
    )
    assert arr != result  # Original unchanged
    assert result == sorted(arr, reverse=True)

def test_multiple_combinations():
    """Test multiple parameter combinations"""
    arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    
    combinations = [
        {'pending_item_percentage': 0.3, 'reverse': False},
        {'pending_item_percentage': 0.7, 'reverse': True},
        {'reverse': True, 'inplace': False},
    ]
    
    for params in combinations:
        test_arr = arr.copy()
        result = bfc_sort(test_arr, **params)
        
        # Check result is sorted correctly
        if params.get('reverse', False):
            expected = sorted(arr, reverse=True)
        else:
            expected = sorted(arr)
        
        if params.get('inplace', True):
            assert test_arr == expected
        else:
            assert result == expected
            assert test_arr == arr 

# ============ EDGE CASE TESTS ============

def test_parameters_with_empty_array():
    """Test all parameters with empty array"""
    arr = []
    result = bfc_sort(
        arr,
        pending_item_percentage=0.5,
        inplace=False,
        reverse=True,
    )
    assert arr == []
    assert result == []

def test_parameters_with_single_element():
    """Test all parameters with single element"""
    arr = [5]
    result = bfc_sort(
        arr,
        pending_item_percentage=0.5,
        inplace=False,
        reverse=True,
    )
    assert arr == [5]
    assert result == [5]

def test_parameters_with_all_duplicates():
    """Test parameters with all duplicate values"""
    arr = [5, 5, 5, 5, 5]
    bfc_sort(arr, reverse=True, inplace=True)
    assert arr == [5, 5, 5, 5, 5]

# ============ ARRAY VALIDATION TESTS ============

def test_array_not_list():
    """Array must be a list"""
    with pytest.raises(TypeError, match="array must be a list"):
        bfc_sort((5, 2, 8))  # Tuple

def test_array_not_list_string():
    """String should raise TypeError"""
    with pytest.raises(TypeError, match="array must be a list"):
        bfc_sort("hello")

def test_array_valid_ints():
    """Valid integer array should work"""
    arr = [5, 2, 8, 1, 9]
    bfc_sort(arr)
    assert arr == [1, 2, 5, 8, 9]

def test_array_valid_floats():
    """Valid float array should work"""
    arr = [5.5, 2.2, 8.8, 1.1]
    bfc_sort(arr)
    assert arr == [1.1, 2.2, 5.5, 8.8]

def test_array_mixed_int_float():
    """Mixed int and float should work"""
    arr = [5, 2.5, 8, 1.5, 9]
    bfc_sort(arr)
    assert arr == [1.5, 2.5, 5, 8, 9]

# ============ PENDING_ITEM_PERCENTAGE VALIDATION ============

def test_pending_percentage_not_number():
    """pending_item_percentage must be a number"""
    with pytest.raises(TypeError, match="must be a number"):
        bfc_sort([1, 2, 3], pending_item_percentage="0.5")

def test_pending_percentage_zero():
    """pending_item_percentage cannot be 0"""
    with pytest.raises(ValueError, match="must be between 0 and 1"):
        bfc_sort([1, 2, 3], pending_item_percentage=0)

def test_pending_percentage_negative():
    """pending_item_percentage cannot be negative"""
    with pytest.raises(ValueError, match="must be between 0 and 1"):
        bfc_sort([1, 2, 3], pending_item_percentage=-0.5)

def test_pending_percentage_over_one():
    """pending_item_percentage cannot exceed 1"""
    with pytest.raises(ValueError, match="must be between 0 and 1"):
        bfc_sort([1, 2, 3], pending_item_percentage=1.5)

def test_pending_percentage_valid():
    """Valid pending_item_percentage should work"""
    arr = [5, 2, 8, 1, 9]
    bfc_sort(arr, pending_item_percentage=0.5)
    assert arr == [1, 2, 5, 8, 9]

# ============ INPLACE VALIDATION ============

def test_inplace_not_bool():
    """inplace must be boolean"""
    with pytest.raises(TypeError, match="inplace must be a boolean"):
        bfc_sort([1, 2, 3], inplace=1)

def test_inplace_string():
    """inplace cannot be string"""
    with pytest.raises(TypeError, match="inplace must be a boolean"):
        bfc_sort([1, 2, 3], inplace="True")

def test_inplace_none():
    """inplace cannot be None"""
    with pytest.raises(TypeError, match="inplace must be a boolean"):
        bfc_sort([1, 2, 3], inplace=None)

def test_inplace_valid_true():
    """Valid inplace=True should work"""
    arr = [5, 2, 8]
    bfc_sort(arr, inplace=True)
    assert arr == [2, 5, 8]

def test_inplace_valid_false():
    """Valid inplace=False should work"""
    arr = [5, 2, 8]
    result = bfc_sort(arr, inplace=False)
    assert arr == [5, 2, 8]
    assert result == [2, 5, 8]

# ============ REVERSE VALIDATION ============

def test_reverse_not_bool():
    """reverse must be boolean"""
    with pytest.raises(TypeError, match="reverse must be a boolean"):
        bfc_sort([1, 2, 3], reverse=1)

def test_reverse_string():
    """reverse cannot be string"""
    with pytest.raises(TypeError, match="reverse must be a boolean"):
        bfc_sort([1, 2, 3], reverse="True")

def test_reverse_none():
    """reverse cannot be None"""
    with pytest.raises(TypeError, match="reverse must be a boolean"):
        bfc_sort([1, 2, 3], reverse=None)

def test_reverse_valid_true():
    """Valid reverse=True should work"""
    arr = [5, 2, 8, 1]
    bfc_sort(arr, reverse=True)
    assert arr == [8, 5, 2, 1]

def test_reverse_valid_false():
    """Valid reverse=False should work"""
    arr = [5, 2, 8, 1]
    bfc_sort(arr, reverse=False)
    assert arr == [1, 2, 5, 8]

# ============ COMBINED VALIDATION ============

def test_multiple_invalid_parameters():
    """Multiple invalid parameters should raise first error"""
    with pytest.raises(TypeError):
        bfc_sort("not a list", pending_item_percentage=5, inplace="yes")

def test_all_valid_parameters():
    """All valid parameters should work"""
    arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    result = bfc_sort(
        arr,
        pending_item_percentage=0.4,
        inplace=False,
        reverse=True,
    )
    assert arr == [5, 2, 8, 1, 9, 3, 7, 4, 6]  # Original unchanged
    assert result == [9, 8, 7, 6, 5, 4, 3, 2, 1]