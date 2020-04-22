#include <stdio.h>
#define MAX 1000000
#define SWAP(x,y){int t = x; x = y; y = t;}

int N, arr[MAX];

void Qsort(int *array, int left, int right){

    int mLeft = left;
    int mRight = right;
    int pivot = array[(left + right)/2];

    while(mLeft <= mRight){

        while(pivot > array[mLeft]) mLeft++;

        while(pivot < array[mRight]) mRight--;

        if(mLeft <= mRight){
            SWAP(array[mLeft],array[mRight]);
            mLeft++;
            mRight--;
        }

        if(left < mRight) Qsort(arr, left, mRight);
        if(mLeft < right) Qsort(arr, mLeft, right);
    }

}

int main(){

    int i;

    scanf("%d",&N);

    for(i = 0; i < N; i++){
        scanf("%d", &arr[i]);
    }

    Qsort(arr, 0, N-1);

    for(i = 0; i < N; i++){
        printf("%d", arr[i]);
    }

    return 0;

}
