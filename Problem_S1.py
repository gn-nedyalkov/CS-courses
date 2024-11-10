def merge_sort(list1,subjects):
    if len(list1)==1:
        print(list1)
        return list1
    if len(list1)==2:
        if subjects[str(list1[1])][VALUE]<subjects[str(list1[0])][VALUE]: 
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
                if subjects[str(list_second[i])][VALUE]>=subjects[str(sorted_list[(len(sorted_list)-1)])][VALUE]:
              #  if list_second[i]>=sorted_list[(len(sorted_list)-1)]:
                     sorted_list.extend(list_second[i:])
                     return sorted_list
                if subjects[str(list_second[i])][VALUE]<=subjects[str(sorted_list[j])][VALUE]:
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
        list_of_keys.append(float(key))
    # new_list_keys=merge_sort(list_of_keys,subjects)        
    # return new_list_keys
    return list_of_keys
    
    