#include <cstdio>
using namespace std;

int main() {

    int i, j, n, k;
    int dp[10001] = {0, };

    scanf("%d %d", &n, &k);

    int coins[n];

    for (i = 0; i < n; i++) scanf("%d", &coins[i]);
    
    dp[0] = 1;
    
    for (i = 0; i < n; i++) for (j = coins[i]; j <= k; j++) if (j - coins[i] >= 0) dp[j] += dp[j - coins[i]];

    printf("%d\n", dp[k]);
    return 0;
} 
