#List of elements
num=[0,6,9,8,16,12,81,18,8]
n=len(num)
gsum=sum(num)
mean=gsum/n

#Median sort elements
print("\n original list before sort:",num)
num.sort()
if n%2==0:
	med1=num[n//2]
	med2=num[n//2-1]
	med=(med1+med2)/2
else:
	med.num[n//2]
LK=[]
i=0
while i<n:
	LK.append(num.count(num[i]))
	i+=1
d1=dict(zip(num,LK))
d2={k for(k,v) in d1.items() if v==max(LK)}
print("original list after sort:",num)
print("\n mean=",mean)
print("\n median=",med)
print("\n mode=",str(d2))