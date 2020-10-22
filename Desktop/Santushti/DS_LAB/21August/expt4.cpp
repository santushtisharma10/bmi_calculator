//Expt 4 reverse array 

#include <stdio.h>

void Reverse_Array(int arr[], int size) {
	
	printf("Reversed Array :\n");
	
	for(int i = size-1; i >= 0; --i) {
		
		printf("%d\n", arr[i]);
	}
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
	
	Reverse_Array(arr, num);
	
	return 0;
}
