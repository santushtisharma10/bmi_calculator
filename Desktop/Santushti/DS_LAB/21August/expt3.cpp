// expt 3 - program to find the sum of array
#include <stdio.h>

int sum_of_num (int arr[], int size) {
	
	int sum = 0;
	
	for(int i = 0; i < size; ++i) {
		
		sum += arr[i];
	}
	
	return sum;
}

int main() {
	
	printf("SANTUSHTI SHARMA\n 10314802719\n");
	
	printf("Enter the size of array :");
	
	int num;
	scanf("%d", &num);
	
	int arr[100];
	
	for(int i = 0; i < num; ++i) {
		
		scanf("%d", &arr[i]);
	}
	
	printf("sum of numbers in array is : %d", sum_of_num(arr, num));
	
	return 0;
}
