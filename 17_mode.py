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

    num_dict = {}

    for num in nums:
        num_dict[num] = num_dict.get(num, 0) + 1

    max_num = 0
    max_count = 0

    for (num, count) in num_dict.items():
        if count > max_count:
            max_count = count
            max_num = num
    
    return max_num
        
       