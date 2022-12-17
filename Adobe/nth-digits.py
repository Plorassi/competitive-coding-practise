class Solution:
    def findNthDigit(self, n: int) -> int:
        n -= 1 # zero indexing
        for group in range(1,11):
            # get first number in each group
            first_element_in_group = 10**(group-1)
            
            # store number of elements in group
            num_elements_in_group = 9*first_element_in_group
            
            # get number of digits in group
            num_digits_in_group = num_elements_in_group*group
            
            # if we are in this current nth digit group
            if n < num_digits_in_group:
                # find the element in this group
                element = first_element_in_group + n // group
                # get the digit from this element
                digit = str(element)[n % group]
                return digit
            
            # decrement by the number of digits to go to another group
            n -= num_digits_in_group
