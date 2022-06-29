#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if a == 'q' or a == 'e':
	continue
    print("{:c}".format(a), end='')
