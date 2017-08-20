
import random

day = 365
N = 30

# calculate as formula
s = 1
for i in range(day, day - N, -1):
	s *= i/day
cal_rlt = 1 - s


# calculate as simulation
import random
MCNT = 100000

sum = 0
for i in range(MCNT):
	m = set()
	for i in range(N):
		val = random.randint(1, day)
		if val in m:
			sum += 1
			break
		m.add(val)

sim_rlt = sum / MCNT

print('cal_rlt: ', cal_rlt)
print('sim_rlt: ', sim_rlt)











			