#include <bits/stdc++.h>

using namespace std;

int main()

{
	float T[40][60]={0}, t[40][60]={0}; // numerical solution
	float Ta[40][60]={0}; // analytical solution
	int i,j,k,N=1,m=0,r;
	float e=0.001,E[40][60];
	int itr=1;
	for(i=0;i<40;i++)
	{
		for(j=0;j<60;j++)
		{
			T[i][j]=100;
		}
	}
	
	// intializing the initial guess and boundary values
	for(j=0;j<60;j++)
	{   
		T[0][j]=500;
		T[39][j]=300;
		
		Ta[0][j]=500;
		Ta[39][j]=300;
	}
	
	for(j=1;j<39;j++)
	{
		T[j][0]=300;
		T[j][59]=300;
		
		Ta[j][0]=300;
		Ta[j][59]=300;
	}
	
    float a[58], b[58] , c[58], d[58];
    float v=1.7477, u=-5.4954;
    float p[58],q[58],x[58];
    
    for(i=0;i<58;i++)
    {
    	a[i]=1;
    	c[i]=1;
    	b[i]=u;
	}
	
	//starting the iteration
	

	  
	while(N!=0)  
	{
	  m=0; //important condition
	  
	  for(i=0;i<40;i++)
	  {
	  	for(j=0;j<60;j++)
	  	{
	  		t[i][j]=T[i][j];
		  }
	  }
	  
	
	// starting line by line calculation of temperature distribution
	  
	  
	for(i=1;i<39;i++)
	{	
		for(j=1;j<=58;j++)
		{
			if(j==1)
			{    
			    
				d[j-1]=-T[i][j-1]-v*(T[i+1][j]+T[i-1][j]);
				
			}
			
			else
			{if(j==58)
			{
				 
				d[j-1]=-T[i][j+1]-v*(T[i+1][j]+T[i-1][j]);
					
			}
			
			else
			{
				 
				d[j-1]=-v*(T[i+1][j]+T[i-1][j]);
					
			}
		    }
	    }
	    
	   
	//TDMA for line by line GS
			
				
	
	            p[0]=(-c[0])/b[0];
	
	            q[0]=d[0]/b[0];
	
	            for(k=1;k<58;k++)
	             {
		             p[k]=(-c[k])/(b[k]+(a[k]*p[k-1]));
	              }
	
	             for(k=1;k<58;k++)
	            {
		            q[k]=(d[k]-(a[k]*q[k-1]))/(b[k]+(a[k]*p[k-1]));
	            }
	
	              x[57]= q[57];
	
	            for(k=56;k>=0;k--)
            	{
		            x[k]= (p[k]*x[k+1])+q[k];
            	}
            	
            	
            	
    // updating values to the temperature distribution matrix
            
            for(j=1;j<59;j++)
            {
            	T[i][j]=x[j-1];
            	
			}
		
         }
         
    //calculating the error for each iteration
	   
	    for(i=0;i<40;i++)
	    {
	    	for(j=0;j<60;j++)
	    	{
	    		E[i][j]=abs(T[i][j]-t[i][j]);
	    		
	    		if(e<(E[i][j]))
	    		{
	    			m=1;
				}
			}
		}
		
	//condition to continue iteration
		if(m==0)
		{
			N=0;
		}
		
   }
   
    // output the temperature distribution in the slab
    
    for(k=0;k<40;k++)
    {
    	for(j=0;j<60;j++)
    	{
    		cout<<T[k][j]<<endl;
		}
		cout<<endl;
	}
     
	 // calculating the analytical solution
	
	float X[60];
	float Y[40];
	float sum=0.0;
	int n;
	
	for(i=0;i<60;i++)
	{
		X[i]=i*(50.0/59.0);
	}

	for(i=0;i<40;i++)
	{
		Y[i]=i*(25.0/39.0);
		
	}
	
	for(i=1;i<39;i++)
	{
		for(j=1;j<59;j++)
		{   
		    sum=0.0; // important condition
		    
			for(n=1;n<=100;n++)
			{
				sum=sum+((((1-(pow(-1,n)))/n)*(sin((n*3.14*X[j])/50.0))*(sinh((n*3.14*Y[i])/50.0)))/(sinh((n*3.14*25.0)/50.0)));
			}
			
			Ta[39-i][j]=300+((400.0/3.14)*sum);
			
		}
	}
	
	// calculating the error between the solutions
	
	float Err[40][60];
	
	for(i=0;i<40;i++)
	{
		for(j=0;j<60;j++)
		{
			Err[i][j]=abs(Ta[i][j]-T[i][j]);
		}
	}
	
	// data extraction for plotting T vs y and T vs x for both analytical and numerical
	
	float ha[40],h[40];
	float la[60],l[60];
	
	for(i=0;i<40;i++)
	{
		ha[i]=Ta[i][30];
		h[i]=T[i][30];
	}
	
	for(i=0;i<60;i++)
	{
		la[i]=Ta[20][i];
		l[i]=T[20][i];
	}
	// plotting is done using python and code with data is also attached
}
