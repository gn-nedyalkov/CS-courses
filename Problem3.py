# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    amount=[]
    amount.append(savings*(1+growthRates[0]*0.01)-expenses)
    for i in range(len(growthRates)-1):
        amount.append(amount[i]*(1+growthRates[i+1]*0.01)-expenses)
        
    return amount
   

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print (savingsRecord)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.
    savings   = 100000
    growthRates = [10, 52, 0.2, -5, 1]
    expenses    = 10000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print (savingsRecord)
