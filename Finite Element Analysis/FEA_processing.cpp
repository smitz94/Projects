#include <bits/stdc++.h>

using namespace std;


	// defining function to calculate shape fucntion at specified gauss point 
	
	float shapefunction(float psi[],int k,int m,int i)
	{
		float N; // value of shape function at specified gauss point
		int j;
		float n=1.0,d=1.0; // numerator and denominator in shape fucntion respectively
		
		for(j=0;j<m;j++)
		{
			if(j!=i)
			{
				n=n*(psi[k]-psi[j]);
				
			}
		}
		
		for(j=0;j<m;j++)
		{
			if(j!=i)
			{
				d=d*(psi[i]-psi[j]);
				
			}
		}

		N=n/d;
		
		return N;
	}
	
	// defining function to calculate differentiation of shape function at specified gauss point
	
	float dshapefunction(float psi[],int k,int m,int i)
	{
		float dN; // value of differentiation of shape function at specified gauss point
		int j;
		float n=0.0,d=1.0; // numerator and denominator in diffentiation of shape funtion respectively
		
		for(j=0;j<m;j++)
		{
			if(j!=i)
			{
				n=n+(psi[k]-psi[j]);
				
			}
		}
		
		for(j=0;j<m;j++)
		{
			if(j!=i)
			{
				d=d*(psi[i]-psi[j]);
				
			}
		}
		
		dN=n/d;
		
		return dN;
	}
	
int main()

{
	int n_e=40; //number of elements
	
	int m=3; // number of nodes per element
	
	int n; // total number of nodes in the FEM analysis
	n=(n_e*(m-1))+1;
	
	
	int c[n_e][m]; //connectivity matrix
	
	int i,j,h=1,k,p,q,r,s; // dummy variables
	
	float c1=30; //specified concentration at left end
	
	float D=6*pow(10,-12); // diffusion coefficient

	float Q_m=1.2*pow(10,-9); // specified mass flow rate at right end
	
	// initializing connectivity matrix
	
	for (i=0;i<n_e;i++)
	{
		for(j=0;j<m;j++)
		{
			c[i][j]=j+h;
		}
		h=c[i][m-1];
	}
	
	float L=1;// length of the rod in m
	
	// defining global co-ordinate vector
	
	float X[n];
	
	for(i=0;i<n;i++)
	{
		X[i]=(L/(n-1))*i;
	}
	
	float K[n][n]; // global stiffness matrix
	
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			K[i][j]=0.0;
		}
	}

	float k_e[m][m]; // elemental stiffness matrix
	
	for(i=0;i<m;i++)
	{
		for(j=0;j<m;j++)
		{
			k_e[i][j]=0.0;
		}
	}
	
	float F[n]; //global right side vactor
	
	for(i=0;i<n;i++)
	{
		F[i]=0;
	}
	
	float f[m]; // elemental or local right side vector
	
	for(i=0;i<m;i++)
	{
		f[i]=0.0;
	}
	
	float C[n]; // global notation for primary variable or concentration in this case
	
	for(i=0;i<n;i++)
	{
		C[i]=0;
	}
	
	float x[m]; // local or elemental co-ordinate vector
	
	int e; // dummy variable to run through all elements
	
	float l; // length of an element
	
	int n_G=3; // number of gauss points for numerical integration
	
	float psi[n_G]={-0.77460,0.0,0.77460}; // natural co-ordinates for gauss integration
	
	float w[n_G]={0.55556,0.88889,0.55556}; //weights corresponding to natural co-ordinates for gaussian numerical integration
	
	float A[n]; // area at the defined nodes
	
	// initializing area at all nodes
	for(i=0;i<n;i++)
	{
		A[i]=3+(4*X[i]);
	}
	
	float a[m]; // area defined for m-noded element 
	
	l=X[m-1]-X[0]; // length of the element
	
	float A_e=0.0; // area at specified gauss point for numerical integration
	
	float B[m]; // matrix containg value of differentiation of shape funtion 
	
	float G[m][m]; // matrix as a result of multiplying matrix B and transpose(B)
	
	// computing [k] and [f] over all elements
	for(e=0;e<n_e;e++)  // addition changing element to 1
	{   
	    for(i=0;i<m;i++)
	    {
	    	j=c[e][i];
	    	x[i]=X[j-1];
	    		
		}
		for(i=0;i<m;i++)
		{
		     j=c[e][i];
		     a[i]=A[j-1];
		     
		}
		
		// computing numerical integration for calculting [k] and [f] according to weights
		for(k=0;k<n_G;k++) 
		{   
		    A_e=0.0;
			for(i=0;i<m;i++)
			{
				A_e=A_e+((shapefunction(psi,k,m,i))*a[i]);  //value of shape function at psi[k]
			}
			
			for(i=0;i<m;i++)
			{
				B[i]= dshapefunction(psi,k,m,i); // value of differentiation of shape function at psi[k]
				
			}
			
			// carrying out matrix multiplication
			for(i=0;i<m;i++)
			{
				for(j=0;j<m;j++)
				{
					G[i][j]=B[i]*B[j];
				}
			}
			
			
			for(i=0;i<m;i++)
			{
				for(j=0;j<m;j++)
				{
					k_e[i][j]=k_e[i][j]+((w[k]*A_e*D*2*G[i][j])/l);
				}
			}
			
			// [f] for all elements is 0 in our case as we dont have any c term in our variational functional			
		}
		
		// Assembly of global stiffness matrix
		
		for(p=0;p<m;p++)
		{   
		    r=c[e][p];
		    
		    F[r-1]=F[r-1]+f[p];
		    
			for(q=0;q<m;q++)
			{
			   s=c[e][q];
			   
			   K[r-1][s-1]=K[r-1][s-1]+k_e[p][q];
			}
		}
					
	}
		
	//Application of essential boundary conditions
	F[n-1]=-Q_m;
	C[0]=c1;
	
	// removing the meaningless row and modifying the matrices
	
	float K_new[n-1][n-1];   // new stiffness matrix for computation
	
	for(i=0;i<n-1;i++)
	{
		for(j=0;j<n-1;j++)
		{
			K_new[i][j]=K[i+1][j+1];
		}
	}
	
	float F_new[n-1]; // modified right hand side vector
	
	for(i=0;i<n-1;i++)
	{
		F_new[i]=F[i+1]-(K[i+1][0]*C[0]);
	}
	
	// modified Concentration matrix
	float C_new[n-1];
	
	for(i=0;i<n-1;i++)
	{
		C_new[i]=0;
	}
	
	
	//Calculating the concentration at each nodes using gauss seidel method
	
	float t=0.001,E[n]; // t is tolerance and E is error matrix
	
    int z=1,v=0; // dummy variables
    
	float y[n-1]; // storing values for previous iteration for comparison
    
	float sum=0.0; // du,,y variable for summation
    
    while(z!=0)
	{    v=0;
	    for(i=0;i<n-1;i++)
	    {
	    	y[i]=C_new[i];
		}
		
    	for(i=0;i<n-1;i++)
    	{    sum=0;
    	
    		for(j=0;j<n-1;j++)
    		{       
				if(j!=i)
				{ 
    		     sum=sum+(K_new[i][j]*C_new[j]);
    		     
				}
		    }
    		
			C_new[i]=(F_new[i]-sum)/K_new[i][i];
				
		}
		
		
		for(i=0;i<n-1;i++)
		{
			E[i]=abs(C_new[i]-y[i]);
			if(t<E[i])
			{
				v=1;
			}
		}
		
		if(v==0)
		{
			z=0;
		}

    }
    
    // substituting value of C_new to original C matrix
    for(i=0;i<n-1;i++)
    {
    	C[i+1]=C_new[i];
	}
	
	
    cout<<endl<<"Using the Gauss Siedel the calculated solution for concentration is:"<<endl<<endl;
    
    for(i=0;i<n;i++)
    {
    	cout<<C[i]<<endl;
	}
	
}

