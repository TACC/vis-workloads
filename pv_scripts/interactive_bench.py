import time
Render()
Render()
Render()
times = []
print "running bench..."
st = time.time()
for i in range(0,3):
  st2 = time.time()
  Render()
  et2 = time.time()
  times.append(et2-st2)
et = time.time()
print "avg: " + str((et-st)/3.0)
print times
