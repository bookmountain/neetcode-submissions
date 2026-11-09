class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        m = {}
        for i in range(len(position)):
            m[position[i]] = speed[i]

        m_sorted = dict(sorted(m.items(), reverse=True))
        stack = []

        for p, s in m_sorted.items():
            t = (target - p) / s
            if stack and t <= stack[-1]:
                # same fleet
                continue
            else:
                stack.append(t)

        return len(stack)
        