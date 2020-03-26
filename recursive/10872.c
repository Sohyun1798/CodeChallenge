#include<stdio.h>

int factorial(int n){

    if(n == 0) return 1;

    else return n*factorial(n-1);

}

int main(){

    int n = 0;

    printf("0부터 12사이의 정수 입력");
    scanf("%d", &n);

    printf("%d", factorial(n));

    return 0;
}