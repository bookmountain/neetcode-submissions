class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        l = 0
        have, total = 0, len(need)
        best_len, best_left = float("inf"), 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            # scenario have += 1
            if s[r] in need and window[s[r]] == need[s[r]]:
                have += 1
            while have == total:
                if r - l + 1 < best_len:
                    best_len, best_l = r - l + 1, l
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        return "" if best_len == float("inf") else s[best_l:best_l + best_len]