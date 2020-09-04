#local() and global(): tell you which items are local and global
# account_number_lists = [i for i in range(1,101)]
# print(account_number_lists)
def swap(values_list):
    li = list(values_list)
    li[0], li[-1] = li[-1], li[0]
    return li

values_list = input().split(',') # Program receives comma-separated values like 5,4,12,19
print(swap(values_list))
def Convert(string): 
    li = list(string.split(" ")) 
    return li 
  
# Driver code     
str1 = "Geeks for Geeks"
print(Convert(str1)) 

reversed(values_list)

