class Solution(object):
    def wordPatternMatch(self, pattern, str):
        def helper(pattern, string, forward={}, backward={}):
            if not pattern and string:
                return False

            if not pattern and not string:
                return True

            # abcde redblue
            # ^xxxx ^^^xxxx
            #   5       7
            # Try to match pattern `a` with at most 3 characters. 
            # That is 7 - 5 + 1, and the last + 1 is for Python range.
            for length in range(1, len(string) - len(pattern) + 1 + 1):
                p, s = pattern[0], string[:length]
                
                if p not in forward and s not in backward:
                    forward[p] = s
                    backward[s] = p

                    if helper(pattern[1:], string[length:], forward, backward):
                        return True

                    del forward[p]
                    del backward[s]
                elif p in forward and forward[p] == s :
                    if helper(pattern[1:], string[length:], forward, backward):
                        return True
                else:
                    # Invalid, but we want to do another attempt so do not return yet.
                    pass
            return False

        return helper(pattern, str)
