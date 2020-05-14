def lengthOfLongestSubstringKDistinct(self, s, k) :
        if k == 0 or len(s) == 0:
            return 0
        # track which index needs to be cut in order to remove one item from the substring
        ht = {}
        start, end = 0, 0
        max_len = 0
        while end < len(s):
            ht[s[end]] = end # add location of character to ht
            end += 1
            if len(ht) == k + 1:
                delete_index = min(ht.values())
                del ht[s[delete_index]]
                start = delete_index + 1 # discard the last alphabet
            max_len = max(max_len, end-start)
        return max_len