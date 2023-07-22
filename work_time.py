"""
To determine time needed to complete a job by 3 persons subject to the following condn:
one person works for whole time while remaining two take part alternately, B takes 1st turn.
"""
A,B,C = [float(_) for _ in input("No. of days A, B and C take to do the job (separate by space): ").split()]
work=1.0 ; time=0.0 # days
while(work>=0):
    partner = C if (time+1)%2==0 else B
    workInDay= (1/A+1/partner)
    work -= workInDay
    if work>=0:
        time+=1  # updates daily
    else:
        time+= (work+workInDay)/workInDay  # condition on last day
        break
print (f"Total Time required={time:0.3f} ")