class SillyPythonList:
    def __init__(self):
        self.__list = [2L,4L]
    def __len__(self):
        return len(self.__list)
    def __iter__(self):
        return self.__list.__iter__()
    def mean(self):
        return 3L

load "/Users/jonesbe/Desktop/sage_testing/trac_9028.py"
R=SillyPythonList()
len(R)
mean(R)
variance(R)
variance(R, bias=True)


### LOG (before patch)
sage: L = SillyPythonList()
sage: list(L)
[2L, 4L]
sage: len(L)
2
sage: mean(L)
3L
sage: variance(L)
1
sage: variance(L, bias=True)
1

sage: R = [2,4]
sage: mean(R)
3
sage: variance(R)
2
sage: variance(R,bias=True)
1

### LOG (after patch)
sage: load "/Users/jonesbe/Desktop/sage_testing/trac_9028.py"
sage: R=SillyPythonList()
sage: len(R)
2
sage: mean(R)
3L
sage: variance(R)
2
sage: variance(R, bias=True)
1
sage: R = [2,4]
sage: variance(R)
2
sage: variance(R, bias=True)
1
