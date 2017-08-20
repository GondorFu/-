
print('====== diff balls, same boxes, allow zero ======')
print()

corr_val = [[1,1,1,1,1,1,1,1,1], 
			[1,2,2,2,2,2,2,2,2], 
			[1,4,5,5,5,5,5,5,5], 
			[1,8,14,15,15,15,15,15,15],
			[1,16,41,51,52,52,52,52,52],
			[1,32,122,187,202,203,203,203,203],
			[1,64,365,715,855,876,877,877,877],
			[1,128,1094,2795,3845,4111,4139,4140,4140],
			[1,256,3281,11051,18002,20648,21110,21146,21147]]

M, N = len(corr_val), len(corr_val[-1])

dp = [[0 for j in range(N+1)] for i in range(M+1)]
for i in range(1, M+1):
	dp[i][1] = 1
for i in range(1, N+1):
	dp[i][i] = 1
		
for i in range(3, M+1):
	for j in range(2, i):
		dp[i][j] = dp[i-1][j-1] + j*dp[i-1][j]

dp2 = [[0 for j in range(N+1)] for i in range(M+1)]	
for i in range(1, M+1):
	dp2[i][1] = 1

for i in range(1, M+1):
	for j in range(1, N+1):
		dp2[i][j] = dp2[i][j-1] + dp[i][j]

start = 5
for iM in range(start, M+1):
	for iN in range(start, N+1):
		sim_rlt = dp2[iM][iN]
		corr_rlt = corr_val[iM-1][iN-1]
		print('M: ', iM, 'N: ', iN)
		print("  sim_rlt: ", sim_rlt, 'check: ', sim_rlt == corr_val[iM-1][iN-1])
		print("  corr_rlt: ", corr_val[iM-1][iN-1])	

print()
print()

print('over!')











