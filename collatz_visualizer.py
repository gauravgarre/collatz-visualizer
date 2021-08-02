import matplotlib.pyplot as plt

while(True):
    nums = []
    num = int(input("Enter a number to perform the Collatz conjecture: "))
    nums.append(num)


    while(num != 1):
        if(num % 2 == 0):
            num = num / 2
        else:
            num = 3 * num + 1
        nums.append(num)

    dist = range(1, len(nums) + 1)

    plt.plot(dist,nums)
    plt.axis("off")

    plt.show()
