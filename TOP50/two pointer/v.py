nums=[1,2,4]
n=max(nums)
expected=n*(n+1)//2
actual=sum(nums)
v= actual-expected
print(v)
