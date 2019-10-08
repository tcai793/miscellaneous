def overlap_length(left, right):
    """Returns the length of the longest suffix of left that is a prefix of right
    
    Args:
        left: a string
        right: a string
    Returns:
        An integer length of the longest overlap (0 if there is no overlap)
    """
    ### BEGIN SOLUTION
    for length in range(min(len(left), len(right)), 0, -1):
        if left.endswith(right[:length]):
            return length
    else:
        return 0
    ### END SOLUTION

def merge_ordered_reads(reads):
    """Returns the shortest superstring resulting from
    merging a list of ordered reads.
    
    Args:
        reads: a list of strings
    Returns:
        A string that is a shortest superstring of the ordered input read strings.
    """

    ### BEGIN SOLUTION
    read_pieces = []
    prev_read = ""
    for read in reads:
        overlap_with_prev_read = overlap_length(prev_read, read)
        read_pieces.append(read[overlap_with_prev_read:])
        prev_read = read
    return ''.join(read_pieces)
    ### END SOLUTION