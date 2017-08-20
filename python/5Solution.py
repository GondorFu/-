
print('====== diff balls, same boxes, not allow zero ======')
print()

corr_val = [[1], 
			[1,1], 
			[1,3,1], 
			[1,7,6,1],
			[1,15,25,10,1],
			[1,31,90,65,15,1],
			[1,63,301,350,140,21,1],
			[1,127,966,1701,1050,266,28,1],
			[1,255,3025,7770,6951,2646,462,36,1]]

M, N = len(corr_val), len(corr_val[-1])

dp = [[0 for j in range(N+1)] for i in range(M+1)]
for i in range(1, M+1):
	dp[i][1] = 1
for i in range(1, N+1):
	dp[i][i] = 1
		
for i in range(3, M+1):
	for j in range(2, i):
		dp[i][j] = dp[i-1][j-1] + j*dp[i-1][j]
	
start = 1
for iM in range(start, M+1):
	for iN in range(start, iM+1):
		sim_rlt = dp[iM][iN]
		corr_rlt = corr_val[iM-1][iN-1]
		print('M: ', iM, 'N: ', iN)
		print("  sim_rlt: ", sim_rlt, 'check: ', sim_rlt == corr_val[iM-1][iN-1])
		print("  corr_rlt: ", corr_val[iM-1][iN-1])	

print()
print()

print('over!')











