T = int(input())


#count = 0
if T in range(1,26):
    for i in range(0,T):
        student_name = []
        score = []
        N = int(input())
        if N in range(2,101):
            constraint = True
            for a in range(0,N):
                item = input().split()
                student_name.append(item[0])
                item[1] = float(item[1])
                if not (item[1] >= 0.0 and item[1] <= 100.0):
                    constraint = False
                score.append(item[1])
                #print(constraint)
            if constraint == True:
                maxname = []
                maxscore = max(score)
                for i in range(0,len(score)):
                    if score[i] == maxscore:
                        maxname.append(student_name[i])
                maxname.sort()
                
                for i in maxname:
                    print(i)
                        
        #count=count+1
        #print(count)
            
