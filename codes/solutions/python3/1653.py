class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_cnt=0
        dp=[0]*(len(s)+1)
        for i in range(len(s)):
            if s[i]=='a':
                dp[i+1]=min(dp[i]+1,b_cnt)
            else:
                dp[i+1]=dp[i]
                b_cnt+=1
        return dp[-1]