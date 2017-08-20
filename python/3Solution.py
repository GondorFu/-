
print('====== same balls, same boxes, not allow zero ======')
print()

M, N = 10, 10

dp = [[0 for j in range(M+1)] for i in range(N+1)]
for i in range(1, M+1):
	dp[1][i] = 1
for i in range(1, N+1):
	dp[i][i] = 1
		
for i in range(2, N+1):
	for j in range(i+1, M+1):
		for k in range(1, i+1):
			if  j - i >= k:
				dp[i][j] += dp[k][j-i]

start = 3
for iM in range(start, M+1):
	for iN in range(start, iM+1):
		sim_rlt = dp[iN][iM]
		print('M: ', iM, 'N: ', iN)
		print("  sim_rlt: ", sim_rlt)	

print()
print()

print('over!')











