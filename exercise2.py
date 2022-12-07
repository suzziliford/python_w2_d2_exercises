
#Using list comprehension, create a list of names of 4 letters or more and capitalize each  name

names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']



print([people.title() for people in names if type(people)==str and len(people)>=4 ])
