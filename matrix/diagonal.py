
        n=len(mat)
        if(n==1):
            return(mat[0][0])
        else:
            diag_sum=0
            for i in range(n):  
                diag_sum=diag_sum+mat[i][i]

            
            j=n-1
            i=0
            while(i<(n//2)):  
                diag_sum=diag_sum+mat[i][j]+mat[j][i] 
                i+=1; j-=1
            return diag_sum