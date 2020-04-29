#include<stdio.h>

void Pqueue(int *array, int *pqlen, int n){

    int x = 0;
    int a = 0;
    int temp = *pqlen;
    int temp2 = 0;
    int top = 0;
    

    while(n>0){

        n--;
        scanf("%d", &x);

        if(x > 0){

            array[temp] = x;
            temp += 1;
            a = temp - 1;
            
            while(a>0){
                if(array[a]>array[(a-1)/2]){
                    temp = array[a];
                    array[a] = array[(a-1)/2];
                    array[(a-1)/2] = temp;
                    a = (a-1)/2;
                }
                else break;
            }
        }

        else if(x==0){

            if(temp == 0) printf("%d", 0);

            else {
                printf("%d", array[top]);
                top++;
                temp--;
                }
        }

        }

    }

int main(){

    int array[100000] = {0};
    int pqlen = 0;
    int n = 0;

    scanf("%d", &n);
    Pqueue(array, &pqlen, n);

}