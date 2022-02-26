# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i%15==0:
                res.append("FizzBuzz")
            elif i%3==0:
                res.append("Fizz")
            elif i%5==0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
 

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        
        # Python 3.7 dicts in all Python implementations must preserve insertion order.
        # In older python versions, it's safe to use collections.OrderedDict()
        div_dict = {3: "Fizz", 5: "Buzz"} 
        
        for num in range(1, n+1):
            ele = ""
            for k in div_dict:
                if num % k == 0:
                    ele += div_dict[k]
            if not ele:
                ele = str(num)
            res.append(ele)
                    
        return res

