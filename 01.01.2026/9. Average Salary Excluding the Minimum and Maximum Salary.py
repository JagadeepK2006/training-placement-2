class Solution(object):
    def average(self, salary):
       
        salary.sort() 
        avg =  sum(salary) 
        avg=avg-salary[0] - salary[-1]
        avg=avg/(len(salary)-2.0) 
        return avg
        
