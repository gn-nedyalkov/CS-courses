#
# Problem 4
#
def nestEggVariable(salary, save, growthRates):
 
    amount=[]
    amount.append(salary*save*0.01)
    for i in range(len(growthRates)-1):
        amount.append(amount[i]*(1+growthRates[i+1]*0.01)+salary*save*0.01)
        
    return amount

def postRetirement(savings, growthRates, expenses):
    
    amount=[]
    amount.append(savings*(1+growthRates[0]*0.01)-expenses)
    for i in range(len(growthRates)-1):
        amount.append(amount[i]*(1+growthRates[i+1]*0.01)-expenses)
        
    return amount

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    index_of_ending_year=len(preRetireGrowthRates)-1
    ending_savings=nestEggVariable(salary,save,preRetireGrowthRates)[index_of_ending_year]
    high_value=ending_savings
    low_value=0
    expenses=(high_value+low_value)/2 #trial expenses
    while True:
        t=len(postRetireGrowthRates)-1
        k=postRetirement(ending_savings,postRetireGrowthRates,expenses)[t]
        ending_amount=k
        if abs(ending_amount)<=0.01:
            break
        elif ending_amount>0:
            low_value=expenses
            expenses=(high_value+low_value)/2
        elif ending_amount<0:
            high_value=expenses
            expenses=(high_value+low_value)/2
            
    return expenses
 



def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print (expenses)
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.
    salary                = 10000
    save                  = 15
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print (expenses)