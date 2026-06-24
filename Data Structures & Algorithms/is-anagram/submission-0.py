class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        t = t.lower()
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

        if len(sh) != len(th):
            return False
        else:
            for skey in sh:
                if skey not in th or sh[skey] != th[skey]:
                    return False
            return True