#include<stdio.h>
#include<stdlib.h>
void jordan(int n){
    int a[20][20];
    int i,j,k;
    printf("Enter the matrix\n");
    for(i=0;i<n;i++)
    {
        for(j=0;j<n+1;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    printf("%d",a);

    

}
int main(){
    jordan(3);
    
    return 0;}