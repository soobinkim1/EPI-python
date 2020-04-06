def merge_ranges(meetings):
    if len(meetings) == 0:
        return meetings
    # input is an array of tuples
    # sort arrays, so that each meeting that starts earlier will be the first one
    # create a queue of "merged" arrays, since need to see if last element in "merged" needs to be updated based on subsequent elements
    # for the last element in merged array, if last is greater, update
    merged = [meetings[0]]
    meetings = sorted(meetings, key = lambda x : x[0])
    
    for cur_start, cur_end in meetings:
        last_start, last_end = merged[-1]
        if last_end >= cur_start:
            merged[-1] = (last_start, max(last_end, cur_end))
        else:
            merged.append((cur_start, cur_end))
    return merged

# print(merge_ranges([(1, 10), (2, 6), (3, 10), (7, 9), [11,13]]))