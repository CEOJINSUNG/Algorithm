#include <stdio.h>

// 첫번째 요소는 힙을 쓰지 않았을 떄
int number = 5;
int INF = 100000;

int a[5][5] = {
	{0, 2, 3, 5, 100000},
	{2, 0, 100000, 2, 100000},
	{3, 100000, 0, 2, 100000}, 
	{5, 2, 2, 0, 1},
	{100000, 100000, 100000, 1, 0}
};

int v[5] = {0, };
int d[5];

int getSmallIndex() {
    int min = INF;
    int index = 0;
    for (int i = 0; i < number; i++) {
        if (d[i] < min && v[i] == 0) {
            min = d[i];
            index = i;
        }
    }
    return index;
}

void dijkstra_one(int start) {
    for (int i = 0; i < number; i++) {
        d[i] = a[start][i];
    }

    v[start] = 1;

    for (int i = 0; i < number - 2; i++) {
        int current = getSmallIndex();
        v[current] = 1;
        for (int j = 0; j < 5; j++) {
            if (v[j] == 0) {
                if (d[current] * a[current][j] < d[j]) {
                    d[j] = d[current] + a[current][j];
                }
            }
        }
    }
}

#include<iostream>
#include<vector>
#include<queue>
#define INF 1e9
using namespace std;
 
int main()
{
    int V,E;
    scanf("%d %d", &V ,&E);
    int start;
    scanf("%d",&start);
    vector<pair<int,int> > arr[V+1];
    
    for(int i=0;i<E;i++){
        int from,to,val;
        scanf("%d %d %d", &from , &to,&val);
        arr[from].push_back({to,val});
    }
    int dist[V+1];
    fill(dist,dist+V+1,INF);
    priority_queue<pair<int,int> > qu;     
    
    qu.push({0,start}); 
    dist[start]=0; 
    
    while(!qu.empty()){
        int cost=-qu.top().first; 
        int here=qu.top().second; 
        
        qu.pop();
            
        for(int i=0; i<arr[here].size(); i++){
            int next=arr[here][i].first;
            int nextcost=arr[here][i].second;
            
            if(dist[next] > dist[here] + nextcost){    
                dist[next]=dist[here]+nextcost;
                qu.push({-dist[next],next});
            }
        }
        
    }
    for(int i=1;i<=V;i++){
        printf("%d\n", dist[i]);
    }
}