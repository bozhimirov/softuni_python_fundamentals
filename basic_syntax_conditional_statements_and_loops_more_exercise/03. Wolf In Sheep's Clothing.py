string=input().split(", ")
list=[]
list=string
n=len(list)

for i in (range(n)):


       if list[n-1]=="wolf" :

              print("Please go away and stop eating my sheep")
              break
       elif list[i]=="wolf" :
              print(f"Oi! Sheep number {n-i-1}! You are about to be eaten by a wolf!")
              break