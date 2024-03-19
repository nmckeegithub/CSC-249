from collections import Counter
lst=["kiran","arun","varun","kunnal","tiya","rhea" ]
frequency = Counter(lst)
if(frequency["kunnal"] > 0):
   print("Yes, kunnal exists in list")
else:
   print("No, kunnal does not exists in list")
