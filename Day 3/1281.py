class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        sum_digits = 0
        product_digits = 1

        while temp>0:
            element = temp % 10
            sum_digits += element 
            product_digits *= element 
            temp //= 10

        return product_digits - sum_digits

        
