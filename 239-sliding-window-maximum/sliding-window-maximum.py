class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque() #index value {it stores the values in decreasing}
        l=0
        r=0
        output=[]
        while r < len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            #remove the left value to maintain the window size
            if l>q[0]:
                q.popleft()
            if (r+1>=k):
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output
            

            


        