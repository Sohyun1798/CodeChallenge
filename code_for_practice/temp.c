#include <stdio.h>
#include <stdlib.h>

int main(){

    int n1 = 0; int n2 = 0;

    printf("정수 입력:\n");
    scanf("%d %d", &n1, &n2);

    if(abs(n1-n2)<=10){
        printf("차이가 10이하");
    }
    else printf("11이상 차이 남");

    return 0;
}

