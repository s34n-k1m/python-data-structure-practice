def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    num_freq = {}

    for num in nums:
    num_freq[num] =num_freq.get(num, 0) + 1

    max_num = 0
    max_count = 0
    
    def val_by_key(key):
        return num_freq[key]

    return max(nums, key=val_by_key)







 
       