import math
def janitor(trash):
    # print(list(set(map(lambda x:x>=1.5,trash))))
    if len(set(trash)) == 1 and trash[0] == 1.5:
        return math.ceil(len(trash)/2)
    elif list(set(map(lambda x:x>=1.5,trash))) == [True]:
        return len(trash)
    else:
        trash.sort(reverse = True)
        less = list(filter(lambda x:x<1.5,trash))
        more = list(filter(lambda x:x>=1.5,trash))
        # print(less,more)
        count = len(more)
        while(len(less) and len(more)):

            num1 = more.pop(0)

            temp = [num1]
            for j in less:
                if j + sum(temp) <= 3.0:
                    temp.append(j)
                    # print(temp)
                    less.pop(less.index(j))

        # print(count)
        # print(less)
        if len(less) != 0:
            # print('yes')
            count3 = 0
            sum_ = 0
            for i in range(len(less)):
                # print(sum_)
                sum_ += less[i]
                if sum_ > 3.0:
                    count3 += 1
                    sum_ = less[i]
            if sum_ < 3.0:
                count3 += 1
            count += count3
        # print(count)
        return count




trash = []
n = int(input())
for i in range(n):
    trash.append(float(input()))
x = janitor(trash)
print('%d' % x)


