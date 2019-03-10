def sum67(nums):
  Sum=0
  ok=1
  for i in nums:
    if(i==6):
      ok=0
    if(i==7 and ok==0):
      ok=1
      continue
    if(ok):
      Sum+=i
  return Sum
