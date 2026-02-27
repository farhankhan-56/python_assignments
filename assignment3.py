#set questions
#question 1
fruit_set= {"apple","banana","orange","guauaua","pinapple"}
fruit_set.add("grapes")
fruit_set.remove("apple")
print(fruit_set)

#question 2
set1= {1,2,3,4}
set2={3,4,5,6}

unon = set1 | set2
print(unon)

inter= set1 & set2
print(inter)

#tuple questions
#question 1
tup = (1,2,3,4,5)
print(tup[0],tup[4])

# question 2
tup2= (10,20,30,40,50)
total = sum(tup2)
print(total)

# question 3

tup3 = (1,2,3)
tup3.insert(5[3])
print(tup3)
# in tuple we cannot add new numbers

# list questions
# question 1
cities = ["nowshera","isalmabad","risalpur","mardan","karachi"]
cities.append("lahore")
cities.insert(1,"peshawar")
print(cities)

# question2
liist = [2,4,6,8,10]
for i in range (len(liist)):
     liist[i] = liist[i] * 2

print(liist)

# dectionary questions
# question 1
marks= {
     "english": 85,
     "urdu": 80,
     "computer": 98
 }

print (marks["computer"])

# question 2 

marks1= {
     "english": 85,
     "urdu": 80,
     "computer": 98
 }
marks1.update ({"maths":90})
print(marks1)

# question 3

marks2= {
      "english": 85,
      "urdu": 80,
      "computer": 98
  }

print(marks2)