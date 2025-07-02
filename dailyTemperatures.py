class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        n = len(temperatures)
        answer = [0] * n
        stack = []  # Store indices

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day
            stack.append(i)

        print(answer)
        return answer


temp1 = [73, 74, 75, 71, 69, 72, 76, 73]
Solution().dailyTemperatures(temp1)

temp2 = [30, 40, 50, 60]
Solution().dailyTemperatures(temp2)

temp3 = [30, 60, 90]
Solution().dailyTemperatures(temp3)
