class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
            
        curr_row = 0
        curr_idx = 0
        total_sentences_ct = 0
        memo = {} # {word_idx: [completed_sentences_ct, next_start_word_idx]}
        
        while curr_row < rows:
            start_word_idx = curr_idx 
            if start_word_idx in memo:
                completed_sentences_ct, curr_idx = memo[start_word_idx]
                total_sentences_ct += completed_sentences_ct
            else:
                complete_sentences_ct = 0
                curr_col = 0

                while curr_col < cols:
                    curr_word_len = len(sentence[curr_idx])
                    if cols < curr_word_len:
                        return 0
                    if cols - curr_col < curr_word_len:
                        break
                    curr_col += (curr_word_len + 1)
                    if curr_idx == len(sentence) - 1:
                        complete_sentences_ct += 1
                    curr_idx = (curr_idx + 1) % len(sentence)
                memo[start_word_idx] = [complete_sentences_ct, curr_idx]
                total_sentences_ct += complete_sentences_ct
            curr_row += 1
        return total_sentences_ct
