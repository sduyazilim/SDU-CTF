#include<stdio.h>

int main(){
	
	int arry[50];
	int i = 0 ;
	
	for(i=0;i<=49;i++){
		
		printf(" %d = %d\n", i, &arry[i]);
	}
	
	return 0 ;
}