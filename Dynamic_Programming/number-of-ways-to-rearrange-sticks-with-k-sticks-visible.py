class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        
        dp = {}
        
        def dfs(n_arr, k_arr):
        
            if n_arr == k_arr:
                return 1
        
            if n_arr == 0 or k_arr == 0:
                return 0
            
            if (n_arr,k_arr) in dp:
                return dp[(n_arr,k_arr)]
            
            
            dp[(n_arr,k_arr)] = (dfs(n_arr-1,k_arr-1) + (n_arr-1)*dfs(n_arr-1,k_arr)) % (10**9+7)
            
            return dp[(n_arr,k_arr)]
        
        
        return dfs(n,k)
