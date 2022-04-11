import os
import string
class Singleton:
    __instance = None

    def __init__(self, pname:str, a:float):
        if(Singleton.__instance == None):
            self.name = pname
            self.age = a
            self.count = 0
            Singleton.__instance = self
        else:
            raise Exception("Singleton already created")
    
    @staticmethod
    def getInstance():
        if(Singleton.__instance == None):
            Singleton()
        return Singleton.__instance

    def print(self):
        print(f"Name : {self.name}, Age : {self.age}, funCount: {self.count}")
        self.count += 1

class Employee:
    _raise = 1.04

    def __init__(self,fn, ln) -> None:
        self.first = fn
        self.last = ln

    @property
    def fullname(self) -> string :
        return f"{self.first} {self.last}"
    
    @fullname.setter
    def fullname(self,name):
        f , l = name.split(" ")
        self.first = f
        self.last = l

    def __str__(self) -> str:
            return self.fullname
    
    def __repr__(self) -> str:
        return f"{self.first}, {self.last}, email ID: {self.first}{self.last}@company.com"


#decorator
def functionDecorator(f):
    
    def func(*k , **kar):
        print("started")
        rv = f(*k , **kar)
        print("end")
        return rv
    return func


def fib(num):
    if(num <= 0 ):
        return 0
    if (num <2):
         return 1
    else:
        return fib(num -1) + fib(num -2)

@functionDecorator
def foo() -> None:
    print("Hello from foo")

@functionDecorator
def foo1(num, num2) -> int:
    print(f"Hello from foo1 {num}")
    return num2

listdata = ["anna","hathaway","harry","becca", "becca"]
tupleData = ("anna","hathaway","harry","becca", "becca")
setData = {"anna","hathaway","harry","becca", "becca"}

dictData = {1:"anna",2:"hathaway",3:"harry",4:"becca",5:"becca"}

def ListMethods(lst):
    print(lst[:1])
    print(lst[1:2])
    print(lst[-3])
    print(lst.count("becca"))
    print(lst.pop())
    if "test" not in lst:
        lst.insert(1, "test")
    print(lst)
    lst.sort()
    print(lst)
    lst.extend(["potter","corey"])
    print(lst)

def ListPractice():
    l1 = [1,2,3,4]
    l2 = list(l1)
    if(l1 == l2):
        print("they are equal")

    l2.append(5)
    print(l1)
    l1String = " - ".join(listdata)
    print(l1String)
    print(l2)

    ListMethods(listdata)

def dictPractice():
    print (dictData.get(1))
    print (dictData.get(7))
    del dictData[5]
    print (dictData)
    print(dictData.values())

    for _key, _val in dictData.items():
        print(f" {_key} : {_val}")

def listComprehenshion():
    lst = [1,2,3,4,5]
    sqList = [ n*n for n in lst]
    sqCubeList = [ n*n*n  if (n & 0x1) else n*n for n in lst ]
    evenSqList = [ n*n for n in lst if not (n & 0x1) ]
    oddList = [ n for n in lst if (n & 0x1) ]
    print(list(filter(lambda n: n%2 == 0, lst)))
    print(list(map(lambda n: n*2, lst)))
    lst.sort(reverse= True)
    print(lst)
    print(sqList)
    print(sqCubeList)
    print(evenSqList)
    print(oddList)

def osPractice():
    
    #print(dir(os))
    os.chdir("../")
    os.mkdir("temp")
    for ro, fo , fi in os.walk(os.getcwd()):
        for file in fi:
            print(ro+"\\"+file)
    os.rmdir("temp")
    os.chdir("Practice")
    print("Current dir:", os.getcwd())

def classPractice() -> None:
    e1 = Employee("corey", "shafer")
    print(e1.fullname)
    e1.fullname = "alex derudo"
    print(e1.fullname)
    print(repr(e1))
    print(e1)

def shiftGrid(grid, k): #leet 1260
    row, col = len(grid), len(grid[0])
    while k>0:
        previous = 0
        for i in range(row):
            for j in range(col):
                previous, grid[i][j] = grid[i][j], previous
        grid[0][0] = previous
        k -=1
    return grid
    
print (shiftGrid([[1,2,3],[4,5,6],[7,8,9]],2))