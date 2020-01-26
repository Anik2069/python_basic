is_tall = True
is_male= True

if is_male and is_tall:
    print("You are taller man")
elif is_male and not(is_tall):
    print("You are short man")
elif not(is_male) and is_tall:
    print("You are not man but tall")
else:
    print("You are not a male and not tall")


def max_num(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
        return n3

print("BIg Number is "+str(max_num(1,4,3)))

monthcoverstion ={
    "Jan":"January",
    "Feb":"Februaary",
    "Mar":"March",
}
print(monthcoverstion.get("Jan"))

i=1
while i<=10:
    print(i)
    i+=1;
print("Loop End")

for le in "Anik":
    print(le);

fr=['jim','karan','kavin']
for le in fr:
    print(le);
for i in range(10):
    print(i);
for i in range(3,10):
    print(i);
numb=[
    [1,2,3,4],
    [4,5,6,7],
    [7,8,9,10],
    [0]
]
for row in numb:
    for col in row:
        print(col)

# hh
# hhh
# hh
# hh

def tranlate(word1):

    trans=""
    for le in word1:
        if le in "AEIOUaeiou":
            trans=trans+"g"
        else:
            trans = trans + le
    return trans

print(tranlate("Anik"))