# set discard() - no error if not present
s = {1, 2, 3}
print(s)
s.discard(2)
print(s)
s.discard(10)
print(s)