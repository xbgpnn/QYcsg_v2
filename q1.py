# """
# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

# 程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
# (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
# (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
# """

# def divPrime(num):
#     factor = []
#     print(num, '=', end=' ')
#     while num != 1:
#         for i in range(2, int(num+1)):
#             if num % i == 0:  # i是num的一个质因数
#                 factor.append(i)
#                 num = num / i # 将num除以i，剩下的部分继续分解
#                 break
#     for i in range(0, len(factor)-1):
#         print(factor[i], '*', end=' ')
 
#     print(factor[-1])

# divPrime(80)

def divPrime(num):
	factor = []

	while num != 1:
		for i in range(2,int(num+1)):
			if num % i == 0:
				factor.append(i)
				num = num / i
				break

	for i in range(0, len(factor)-1):
		print(factor[i], "*", end =" ")

	print(factor[-1])


divPrime(80)