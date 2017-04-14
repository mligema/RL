
import matplotlib.pyplot as plt

iterations = 10000

nums = []
for i in range(iterations):

    # log
    #nums.append(1/((i/50) + 10))

    # linear
    nums.append(1. - (i/iterations))

print(nums)

plt.plot(nums)
plt.show()
