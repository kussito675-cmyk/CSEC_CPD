n=int(input())
events=list(map(int,input().split()))
recruited_officers=0
crime=0
for event in events:
    if event>0:
        recruited_officers+=event
    else:
        if recruited_officers+event<0:
            crime+=-event
        else:
            recruited_officers+=event
print(crime)
