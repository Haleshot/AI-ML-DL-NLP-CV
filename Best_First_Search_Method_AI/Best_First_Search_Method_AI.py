# -*- coding: utf-8 -*-
"""prac05_IS-1_August 29th, 2022.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/114z7m8_jsexoCzY_ZKsQRguMM7PWYgXi
"""


def addlocations():
  def sort_second(l):
    return l[1]
  n = int(input("Enter the number of locations: "))
  lst=[]
  for i in range(n):
    P=[] 
    node, SLD= map(str,input(f"Enter Name and Straight line distance for location: ").split())
    P.append(node)
    P.append(SLD)
    lst.append(P)
  for i in range(n):
    temp=int(lst[i][1])
    lst[i][1]=temp
  Main.extend(lst)
  Main.sort(key=lambda row: (row[1]))
  return Main 
A,A1=map(str,input("Enter Name and Straight line distance of initial state: ").split())
Z,Z1=map(str,input("Enter Name and Straight line distance of goal state: ").split())
A2=[]
Z2=[]
A2.append(A)
A2.append(int(A1))
I=[]
I.append(A2)
Z2.append(Z)
Z2.append(int(Z1))
I1=[]
I1.append(Z2) 
print(I)
print(I1)
temp=0
open=[]
close=[]
close.extend(I)
final=0
Main=[]
while(final==0):
  if I==I1:
    print("Goal test successful")
    final=1
  else:
    addlocations()
    print(Main)
    print("The node with shortest distance from goal state is:",Main[0])
    print(f"Expanding node {Main[0]} into:")
    close.extend(Main[0])
    if Main[0][0]==I1[0][0] and Main[0][1]==I1[0][1]:
      print("Goal test successful")
      print(f"The Best first search algorithm suggests the following route to reach the goal state: {close}")
      final=1