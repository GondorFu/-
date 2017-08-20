
print('====== same balls, diff boxes, allow zero ======')
print()

M, N = 10, 10

dp = [[0 for j in range(M+1)] for i in range(N+1)]

for i in range(1, M+1):
	dp[1][i] = 1
for i in range(1, N+1):
	dp[i][0] = 1
	
for i in range(2, N+1):
	for j in range(1, M+1):
		dp[i][j] = dp[i-1][j] + dp[i][j-1];
		
start = 5	
for iM in range(start, M+1):
	for iN in range(start, N+1):
		cal_rlt = 1
		temp = 1
		for i in range(2, iN):
			temp *= i
		for i in range(iM+1, iM+iN):
			cal_rlt *= i
		cal_rlt /= temp

		sim_rlt = dp[iN][iM]
		print('M: ', iM, 'N: ', iN)
		print("  sim_rlt: ", sim_rlt, "  check: ", sim_rlt == cal_rlt)
		print("  cal_rlt: ", int(cal_rlt))
		
print()
print()	
print('over!')













