

def average_time(list_process,burst_time):

    # Number of process
    n=len(list_process)

    # Times
    teps=list_process
    for i in range(0,n):
        if(i==0):
            teps[0]=0
        else:
            teps[i]=teps[i-1]+burst_time[i-1]
        print(f'Tep{i+1}: {teps[i]} ',end="")
    
    total=0   
    for i in range(0,n):

        total+=teps[i];  
    media=total/n 
    print(' ')
    print(f'Average Time: {media} ms')
        
if __name__ =="__main__":
    list_process=[]
    burst_time=[]


    flag=1
    
    while(flag!=0):
        process=int(input('Process: '))
        list_process.append(process)
        burst=int(input('Burst time: '))
        burst_time.append(burst)
        flag=int(input('0 - Exit ,1 - Continue: '))
    
    print('Process '+ 'Burst Time')
    for i in range(len(list_process)):
        print(f'''{list_process[i]}          {burst_time[i]}''')
    average_time(list_process,burst_time)
    