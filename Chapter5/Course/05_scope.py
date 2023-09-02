"""
# variable locale

def testA():
    num = 100
    print(num)

testA()
print(num)
"""

num = 100

def testA():
    print(num)

def testB():
    print(num)

testA()
testB()