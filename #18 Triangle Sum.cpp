#include <bits/stdc++.h>
#define ll long long
using namespace std;
const int N2 = 110, N3 = 1110, N4 = 1e4 + 10, N5 = 1e5 + 10, N6 = 1e6 + 10;

typedef pair <int, int> PII;

const int dx[4] = {1, 0, -1, 0}, dy[4] = {0, 1, 0, -1};

const int N = 510;

int n;
int a[N][N];
int f[N][N];

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    //input the number of layers:15
    cin >> n;
    //store the triangle
    for (int i = 1; i <= n;i++)
        for (int j = 1; j <= i;j++)
            cin >> a[i][j];
    //initialize the numbers with small numbers so we can use the max function later
    for (int i = 0; i <= n;i++)
        for (int j = 0; j <= n+1;j++)
            f[i][j] = -1e9;
    
    f[1][1] = a[1][1];
    //use dynamic programming to calculate the maximum value of every point on the triangle
    for (int i = 2; i <= n;i++)
        for (int j = 1; j <= i;j++)
            f[i][j] = max(f[i - 1][j - 1] + a[i][j], f[i - 1][j] + a[i][j]);

    int res = -1e9;
    //compare the maximum values on the bottom layer
    for (int i = 1; i <= n; i++)
        res = max(res, f[n][i]);
    cout << res;

    return 0;
}
