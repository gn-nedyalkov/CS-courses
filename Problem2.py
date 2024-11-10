#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    # TODO: Your code here.
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    amount=[]
    amount.append(salary*save*0.01)
    for i in range(len(growthRates)-1):
        amount.append(amount[i]*(1+growthRates[i+1]*0.01)+salary*save*0.01)
        
    return amount





def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print (savingsRecord)
    
    salary2      = 10000
    save2        = 10
    growthRates2 = [2, 1, 1, 10, 10]
    savingsRecord2 = nestEggVariable(salary2, save2, growthRates2)
    print (savingsRecord2)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

#