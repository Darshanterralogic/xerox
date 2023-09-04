#find the birthday of person

birthday = {
    'darshan':'30/04/1994',
    'latha':'05/06/1988',
    'kallapa':'01/01/1994',
    'mathew':'02/04/1993'
}

name = input("enter the name")

if name in birthday:
    print(birthday[name])
else:
    print("not found")