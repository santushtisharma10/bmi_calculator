// Program to find the sum of digits of number

#include <stdio.h>

int sum_of_digits(int num) {
	
	int ans = 0;
	
	while(num) {
		
		ans += num%10;
		num = num/10;
	}
	return ans;
}

int main() {
    
    printf("SANTUSHTI SHARMA\n 10314802719\n");
    
	printf("Enter a number :");
	
	int num;
	scanf("%d", &num);
	
	printf("Sum of digits of a number is %d", sum_of_digits(num));
	
	
	return 0;
}
