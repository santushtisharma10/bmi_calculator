// program to find maximum of n input numbers
#include <stdio.h>

int findmax(int arr[], int size) {
	
	int max = arr[0];
	
	for(int i = 1; i < size; ++i) {
		
		if(max < arr[i]) {
			
			max = arr[i];
		}
	}
	
	return max;
} 

int main() {
	
	printf("SANTUSHTI SHARMA\n 10314802719\n");
	printf("Enter the n:");
	
	int num;
	scanf("%d", &num);
	
	int arr[100];
	
	for(int i = 0; i < num; ++i) {
		
		scanf("%d", &arr[i]);
	}
	printf("Maximum of array is : %d", findmax(arr, num) );
	
	return 0;
}
