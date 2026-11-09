class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                j = stack.pop()
                left = stack[-1] if stack else - 1
                width = i - left - 1
                area = max(area, heights[j] * width)
            stack.append(i)
            
        while stack:
            j = stack.pop()
            left = stack[-1] if stack else - 1
            width = len(heights) - left - 1
            area = max(area, heights[j] * width)
        
        return area