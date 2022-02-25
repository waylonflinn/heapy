# heapy

## general
def swap(a, i, j): (a[i], a[j]) = (a[j], a[i])

## heap
def parent(i): return (i - 1) // 2

def left(i): return 2 * i + 1

def right(i): return 2 * i + 2

def is_root(i): return i == 0

def is_leaf(L, i): return left(i) >= len(L) and right(i) >= len(L)

def one_child(L, i): return right(i) == len(L)

def down_heapify(L, i, I):
	if is_leaf(L, i): return

	# check children
	l = left(i)
	r = right(i) if not one_child(L, i) else left(i)

	if L[l][1] < L[i][1] or L[r][1] < L[i][1]:
		c = l if L[l][1] <= L[r][1] else r


		# swap values
		swap(L, c, i)

		# update index
		I[L[c][0]] = c
		I[L[i][0]] = i

		down_heapify(L, c, I)

	return

def up_heapify(L, i, I):
	if i == 0: return L

	p = parent(i)

	if L[p][1] > L[i][1]:
		swap(L, p, i)
		I[L[p][0]] = p
		I[L[i][0]] = i

		up_heapify(L, p, I)

	return

def build_heap(L, I):

	# equivalent to recursive calls to build_heap followed by down_heapify
	for i in range(len(L) - 1, -1, -1):
		down_heapify(L, i, I)

	return L


## Max Versions

def down_heapify_max(L, i, I):
	if is_leaf(L, i): return

	# check children
	l = left(i)
	r = right(i) if not one_child(L, i) else left(i)

	if L[l][1] > L[i][1] or L[r][1] > L[i][1]:
		c = l if L[l][1] >= L[r][1] else r


		# swap values
		swap(L, c, i)

		# update index
		I[L[c][0]] = c
		I[L[i][0]] = i

		down_heapify_max(L, c, I)

	return

def up_heapify_max(L, i, I):
	if i == 0: return L

	p = parent(i)

	if L[p][1] < L[i][1]:
		swap(L, p, i)
		I[L[p][0]] = p
		I[L[i][0]] = i

		up_heapify_max(L, p, I)

	return

def build_heap_max(L, I):

	# equivalent to recursive calls to build_heap followed by down_heapify
	for i in range(len(L) - 1, -1, -1):
		down_heapify_max(L, i, I)

	return L
