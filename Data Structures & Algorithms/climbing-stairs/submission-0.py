class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n <= 2:
            return n
        
        # 'one_step_behind' represents ways(n-1), 'two_steps_behind' represents ways(n-2)
        two_steps_behind = 1
        one_step_behind = 2
        
        for _ in range(3, n + 1):
            current_ways = one_step_behind + two_steps_behind
            
            # Shift our pointers forward for the next iteration
            two_steps_behind = one_step_behind
            one_step_behind = current_ways
            
        return one_step_behind
