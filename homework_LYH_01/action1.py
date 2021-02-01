import numpy


def sum1():
    sum = 0
    for i in range(2, 102, 2):
        sum += i
    print('2+4+6+8+...+100 =', sum)


def sum2():
    list1 = numpy.arange(2, 102, 2)
    print('2+4+6+8+...+100 =', numpy.sum(list1))


sum1()
sum2()
