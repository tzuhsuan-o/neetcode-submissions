class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            sh = {}
            th = {}
            for schar in s:
                if schar in sh:
                    sh[schar] += 1
                else:
                    sh[schar] = 1

            for tchar in t:
                if tchar in th:
                    th[tchar] += 1
                else:
                    th[tchar] = 1

            if sh != th:
                return False
            else:
                return True