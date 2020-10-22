// expt 5 - largest and smallest element in array

#include <stdio.h>
/*
author: Santushti Sharma
*/
int small_val(int arr[], int size) {
	
	int min = arr[0];
	
	for(int i = 1; i < size; ++i) {
		
		if(min > arr[i]) {
			
			min = arr[i];
		}
	}
	
	return min;
}

int large_val (int arr[], int size) {
	
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
	printf("Enter the size of array");
	
	int num;
	scanf("%d", &num);
	
	int arr[100];
	
	for(int i = 0; i < num; ++i) {
		
		scanf("%d", &arr[i]);
	}
	
	printf("Largest element of array : is %d \n", large_val(arr, num));
	printf("Smallest element of array : is %d \n", small_val(arr, num));
	
	return 0;
}
