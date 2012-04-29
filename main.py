def all_completed(lvl):
	for i in lvl:
		if i[1] == 0:
			return 0
	return 1

def find_min(lvl):
	if all_completed(lvl):
		return -1, 0
	index = 0
	min   = -1
	for i in range(0, len(lvl)):
		if lvl[i][1] == 0 and (min == -1 or lvl[i][0] < min):
			min = lvl[i][0]
			index = i
	return min, index
	
def find_suitable(lvl, lvl2, t):
	out = []
	for i in range(0, len(lvl)):
		if lvl[i][1] == 0 and lvl[i][0] <= t:
			out.append(i)
	
	suitable = -1
	for i in out:
		if lvl2[i][1] != 1 and (suitable == -1 or lvl2[i][0] > lvl2[suitable][0]):
			suitable = i
	return suitable

fp = open('inputs.txt', 'r')
input = fp.readlines()
fp.close()
fp = open('output.txt', 'w')
cases = int(input[0].strip('\n'))
levels = 0
i = 0
case = 1
while case <= cases:
	# Parse input
	i = i+1
	levels = int(input[i].strip('\n'))
	lvl1 = []
	lvl2 = []
	
	for a in range(i + 1, i + levels + 1):
		line = input[a].strip('\n').split()
		lvl1.append([int(line[0]), 0])
		lvl2.append([int(line[1]), 0])
		i += 1

	# lets start the real logic

	s = 0
	stages_done = 0
	out = ''
	loop = 0
	
	while stages_done < levels:
		min1,  x  = find_min(lvl2)
		min2,  y  = find_min(lvl1)
		# lets try to attempt level2 stages
		if min1 != -1 and min1 <= s:
			if lvl1[x][1] == 1:
				s += 1
			else:
				s += 2
			lvl2[x][1] = 1
			stages_done += 1
		elif min2 != -1 and min2 <= s:
			m = find_suitable(lvl1, lvl2, s)
			if m == -1:
				out = 'Too Bad'
				break
			lvl1[m][1] = 1
			s += 1
		else:
			out = 'Too Bad'
			break
		loop += 1	
	if out != '':
		# TOO BAD
		fp.write('Case #%d: ' % case  + out + '\n')
		#print('Case #%d: ' % case  + out + '\n')
	else:
		fp.write('Case #%d: ' % case  + str(loop) + '\n')
		#print('Case #%d: ' % case  + str(loop) + '\n')
	case += 1
fp.close()