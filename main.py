# def run_tests(tested_function, test_cases):
# for test in test_cases:
# try:
# output = tested_function(test['input'])
# input_str = str(test['input'])[:100]
# assert test['expected'] == output
# print(f"Test passed for expected {test['expected']} for input {input_str} outputted {output} #instead")
# except AssertionError:
# print(f"Test failed for expected {test['expected']} for input {input_str} outputted {output} instead")

# long_test_case = []
# for i in range(1, 10001):
#    long_test_case.append(i)

# long_test_case_2 = []
# for i in range(10000, 0, -1):
#     long_test_case_2.append(i)


# test_cases = [
#    {'input': [1000], 'expected': 0},
#    {'input': long_test_case, 'expected': 9999},
#    {'input': long_test_case_2, 'expected': 0},
#    {'input': [5, 1, 7], 'expected': 6},
# ]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_pointer = 0
        right_pointer = 1
        max_profit = 0
        while right_pointer < len(prices):
            current_profit = prices[right_pointer] - prices[left_pointer]
            if prices[left_pointer] < prices[right_pointer]:
                max_profit = max(current_profit, max_profit)
            else:
                left_pointer = right_pointer
            right_pointer += 1

        return max_profit

# run_tests(Solution().maxProfit, test_cases)