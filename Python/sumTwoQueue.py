def solution(queue1, queue2):
	lst = list(queue1 + queue2)
	length = len(lst)
	q1 = 0
	q2 = length // 2
	target, flag = divmod(sum(lst), 2)
	if flag:
		return -1
	answer = 0
	sum1 = sum(lst[q1:q2])
	while q1 >= 0 and q2 < length and q1 < q2:
		if sum1 == target:
			return answer
		elif sum1 < target:
			sum1 += lst[q2]
			q2 += 1
			answer += 1
		else:
			sum1 -= lst[q1]
			q1 += 1
			answer += 1
	return -1
