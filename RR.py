
def average_time(list_process,burst_time,q):
    # Number of process
    n=len(list_process)
    quantum=q

    # Times
    #teps=list_process
    aux=list_process

    controle=True
    
    aux=burst_time.copy()
    pos=0
    val=aux.copy()
    for i in range(0,n):
        
        while aux[pos]>0:
            
            aux[pos]-=quantum

            if(abs(burst_time[pos])-abs(aux[pos])==quantum):
                    pos=i+1
            elif(aux[pos]-burst_time[pos]<=0):
                aux[pos]=0
                pos=pos+1
                if(pos==n):
                    pos=pos-n
                break
                
    print(val)
    #print(aux_cont)        

    
    #print(f'Tep{i+1}: {teps[i]} ',end="")
if __name__ =="__main__":
    list_process=[]
    burst_time=[]


    flag=1
    '''
    while(flag!=0):
        process=int(input('Process: '))
        list_process.append(process)
        burst=int(input('Burst time: '))
        burst_time.append(burst)
        flag=int(input('0 - Exit ,1 - Continue: '))
    '''
    quantum=4
    list_process=[1,2,3]
    burst_time=[24,3,3]
    print('Process '+ 'Burst Time')
    for i in range(len(list_process)):
        print(f'''{list_process[i]}          {burst_time[i]}''')
    average_time(list_process,burst_time,quantum)
    