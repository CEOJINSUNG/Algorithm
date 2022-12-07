// https://blog.naver.com/ndb796/221236952158
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#define MAX 10001

using namespace std;

int id, d[MAX];
bool finished[MAX];
vector<int> a[MAX];
vector<vector<int>> SCC;
stack<int> s;

// DFS는 총 정점의 개수만틈 실행
int dfs(int x) {
    d[x] = ++id;
    s.push(x);

    int parent = d[x];
    for (int i = 0; i < a[x].size(); i++) {
        int y = a[x][i];
        if (d[y] == 0) {
            parent = min(parent, dfs(y));
        } else if (!finished[y]) {
            parent = min(parent, d[y]);
        }
    }

    if (parent == d[x]) {
        vector<int> scc;

        while (1) {
            int t = s.top();
            s.pop();
            scc.push_back(t);
            finished[t] = true;
            if (t == x) {
                break;
            }
        }
        SCC.push_back(scc);
    }

    return parent;
}