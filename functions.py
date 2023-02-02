
# #maximum of three numbers
l=[1,9,2]
def max_of_num(m):
    maxi=m[0]
    for i in m:
        if i>maxi:
            maxi=i
    print(f"Maximum number in the list is {maxi}")
max_of_num(l)


# #sum of all numbers in a list
a_list=[1,2,3,4,5]
def sum_of_list(b):
    sum=0
    for i in b:
        sum=sum + i
    print(f"Answer to all numbers in the list being multiplied is {sum}")
sum_of_list(a_list)

# #mult all numbers in a list
a=[1,2,3,4,5]
def mult_of_list(b):
    mult=1
    for i in b:
        mult=mult * i
    print(f"Answer to all numbers in the list being multiplied is {mult}")
mult_of_list(a)

# reverse a string (pending logic)
# a="ayesha"
# def rev(b):
#     length=len(b)
#     for i in b:
#         for i in range(1,length):
#             w=b[(length-1)]
# rev(a)

# Print number of upper and lower case in a string
string="AyesHa"
def count_case(s):
    count=0
    upper=0
    for i in s:
        if i.islower():
            count=count+1
        elif i.isupper():
            upper=upper+1
    print(f"The lower case count is  {count}")
    print(f"The lower case count is {upper}")

count_case(string)
