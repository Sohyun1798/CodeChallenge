#include<stdio.h>

void Pqueue(int *array, int pqlen, int n){

    int x = 0;
    int a = 0;
    int temp = pqlen;

    while(n>0){

        n--;
        scanf("%d", &x);

        if(x > 0){

            temp += 1; 
            array[temp] = x;
            a = temp;
             
            while(a>=1){

                if (a/2 >= 1){
                    if(array[a]>array[a/2]){
                        array[a] = array[a/2];
                        array[a/2] = x;
                        a = a/2;
                        continue;
                }

                else break;

                }
                
                else break;
            }
        }

        else if(x==0){

            if(temp < 1) printf("%d\n", 0);

            else {
                printf("%d\n", array[1]);

                int val = array[temp];
                int child = 1;
                temp--;
                
                while(child * 2 <= temp){
                    
                    int childloc = child * 2;
                    if(childloc <= temp){
                        childloc = array[childloc] > array[childloc+1] ? childloc : childloc+1;
                    }

                    if(val < array[childloc]){
                       array[child] = array[childloc];
                       child = childloc;
                    }

                    else break;
                }

                array[child] = val;

                }
        }

        }

    }

int main(){

    int array[100001] = {0};
    int pqlen = 0;
    int n = 0;

    scanf("%d", &n);
    Pqueue(array, pqlen, n);

}