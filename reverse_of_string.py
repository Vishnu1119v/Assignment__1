
#sentence = input("Enter sentence: ")
#longest = sorted(sentence.split(),key=len)
#print("Longest word is: ", longest[-1])
str1=input("Enter sentence: ")
str2=str1.split()
max_len=-1
for i in str2:
    if len(i)>max_len:
      max_len=len(i)
    result=i
print(result)