#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int h[100001];
int currentSize = 0;

int pop()
{
  int nReturn = h[1];

  int reloc = 1;
  int val = h[currentSize];
  currentSize--;
  while (reloc * 2 <= currentSize) {
    int childLoc = reloc * 2;
    if (childLoc <= currentSize) {
      childLoc = h[childLoc] > h[childLoc + 1] ? childLoc : childLoc + 1;
    }

    if (val < h[childLoc]) {
      h[reloc] = h[childLoc];
      reloc = childLoc;
    }
    else {
      break;
    }
  }

  h[reloc] = val;
  
  return nReturn;
}

void push(int a)
{
  currentSize++;

  
  int loc = currentSize;
  h[loc] = a;
  while (loc >= 1) {
    int parent = loc / 2;
    if (parent >= 1) {
      if (h[loc] > h[parent]) {
        h[loc] = h[parent];
        h[parent] = a;
        loc = parent;
        continue;
      }
      else {
        break;
      }
    }
    else {
      break;
    }
  }
}

int main(void) {
  
  int n;

  scanf("%d", &n);

  for (int i = 0; i < n; i++) {
    int x;
    scanf("%d", &x);
    if (!x) {
      if (currentSize < 1) {
        printf("0\n");
        continue;
      }
      else {
        printf("%d\n", pop());
      }
    }
    else {
      push(x);
    }

  }
  return 0;
}