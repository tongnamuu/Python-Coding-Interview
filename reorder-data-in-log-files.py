from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def cmp(x):
            return x.split()[1:], x.split()[0]
        word_list = []
        num_list = []
        for log in logs:
            a, *b = log.split()
            if b[0].isdigit():
                num_list.append(log)
            else:
                word_list.append(log)
        word_list.sort(key=cmp)
        word_list.extend(num_list)
        return word_list


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
solution = Solution()
answer = solution.reorderLogFiles(logs)
print(answer)

