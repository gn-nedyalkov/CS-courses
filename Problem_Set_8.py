# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time


SUBJECT_FILENAME = "subject list.txt"
smaller_set='Smallset.txt'
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    inputFile = open(filename)
    d={}
    for line in inputFile:
        pair3=line.split(',')
        el1=pair3[0]
        el2=int(pair3[1])
        el3=int(pair3[2])
        d[el1]=el2,el3
    return d 



    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    # subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print (res)

def merge_sort(list1,subjects):
    if len(list1)==1:
        print(list1)
        return list1
    if len(list1)==2:
        if subjects[list1[1]][VALUE]<subjects[list1[0]][VALUE]: 
            temp=list1[0]
            list1[0]=list1[1]
            list1[1]=temp
        print(list1)
        return list1
    else: 
        k=len(list1)//2
        list_first=merge_sort(list1[0:k],subjects)
        list_second=merge_sort(list1[k:],subjects)
        sorted_list=list_first
        j=0
        # print('First list:', list_first)
        # print('Second list: ', list_second)
        # print(type(list_second))
        for i in range(len(list_second)):
            for k in range(len(sorted_list[j:])):
                if subjects[list_second[i]][VALUE]>=subjects[sorted_list[(len(sorted_list)-1)]][VALUE]:
              #  if list_second[i]>=sorted_list[(len(sorted_list)-1)]:
                      sorted_list.extend(list_second[i:])
                      return sorted_list
                if subjects[list_second[i]][VALUE]<=subjects[sorted_list[j]][VALUE]:
                # if list_second[i]<=sorted_list[j]: 
                    sorted_list=sorted_list+['']
                    temp=None
                    temp2=None
                    for p in range(len(sorted_list[j:])-1):
                        if temp==None:
                            temp=sorted_list[j+p+1]
                            sorted_list[j+p+1]=sorted_list[j+p]
                        else: 
                            temp2=temp
                            temp=sorted_list[j+p+1]
                            sorted_list[j+p+1]=temp2
                    sorted_list[j]=list_second[i]
                    # print('Sorted list: ',sorted_list)
                    break
                j=j+1
        return sorted_list
                    
            
            
        

def sort_by_value(subjects):
    list_of_keys=[]
    keys=subjects.keys()
    for key in keys:
        list_of_keys.append(key)
    new_list_keys=merge_sort(list_of_keys,subjects)        
    return new_list_keys
    return list_of_keys
    
    
    
def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork):
    
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    assert maxWork>=0 and type(maxWork)==int
    ordered_by_value=sort_by_value(subjects)
    j=len(ordered_by_value)
    greedy_list={}
    work_sum=0
    for i in range(j):
        if work_sum+subjects[ordered_by_value[j-1-i]][WORK]<=maxWork:
            greedy_list[ordered_by_value[j-1-i]]=subjects[ordered_by_value[j-1-i]]
            work_sum+=subjects[ordered_by_value[j-1-i]][WORK]
        if work_sum==maxWork:
            return greedy_list
    return greedy_list    
    
    # TODO...