def remdups(l):
	seen=set()
	seen_add=seen.add
	return [x for x in seq if not x in seen ]
