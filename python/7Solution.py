
print('============= Two Kings =====================')
print()

import random

M = 54
N = 3
K1, K2 = 1, 2 # King representation

# calculate as formula
cal_rlt = 17/53


# calculate as simulation
import random
MCNT = 100000

sum = 0
for i in range(MCNT):
	arr = [i for i in range(1, M+1)]
	random.shuffle(arr)
	pK1 = arr.index(K1)
	pK2 = arr.index(K2)
	if pK1//(M/N) == pK2//(M/N):
		sum += 1

sim_rlt = sum / MCNT

print('cal_rlt: ', cal_rlt)
print('sim_rlt: ', sim_rlt)











			