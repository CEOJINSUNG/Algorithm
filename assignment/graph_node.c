#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define VERTICES 26
#define ALPHA_ASCII 97

// ---------------------- flight path 관련 함수 ----------------------

typedef struct City {
    char alpha;
    int x;
    int y;
    struct City* next_city;
} City;

typedef struct Flight { 
    int count;
    City* list[VERTICES];
} Flight;

static int random_x[26];
static int random_y[26];
void init_city_location(int seed) {
    srand((unsigned int) time(NULL) + seed);
    for (int i = 0; i < 26; i++) {
        int x = rand()%3000 + (-1) * rand()%3000;
        int y = rand()%3000 + (-1) * rand()%3000;
        random_x[i] = x;
        random_y[i] = y;
    }
}

// 해당 그래프를 거치게 되면 python 상으로 아래와 같은 형태를 띄게 된다.
// {
//     "a": City,
//     "b": City,
//     ...
// }
void init_flight(Flight* flight) {
    char c = 'a';
    flight->count = 0;
    for (int i = 0; i < 26; i++) {
        City* city = (City*) malloc(sizeof(City));
        char alpha = c + i;
        flight->list[i] = city;
        flight->list[i]->alpha = alpha;
        flight->list[i]->x = random_x[i];
        flight->list[i]->y = random_y[i];
        flight->list[i]->next_city = NULL;
    }
}

void print_city_location(Flight* flight) {
    printf("=========== 도시 위치 출력 ===========\n");
    for (int i = 0; i < 26; i++) {
        City* city = flight->list[i];
        printf("도시 %c의 위치 : (x, y) -> (%d, %d)\n", city->alpha, city->x, city->y);
    }
    printf("\n");
}


// 1을 반환하면 start와 end의 길이 존재한다. 0을 반환하면 길이 존재하지 않는다.
int find_flight_path(Flight* flight, char start, char end) {
    // a->97라는 아스키 코드이기에 97를 빼준다.
    int start_num = start - ALPHA_ASCII;
    int end_num = end - ALPHA_ASCII;

    int exist_city[26] = {0, };
    exist_city[start_num] = 1;

    City* start_city = flight->list[start_num];
    City* n_city = start_city->next_city;
    
    while (n_city != NULL) {
        int num = n_city->alpha - ALPHA_ASCII;
        exist_city[num] = 1;
        n_city = n_city -> next_city;    
    }
    if (exist_city[end_num] == 1) {
        return 1;
    }
    return 0;
}

// 1이면 start와 end가 연결되었음 0이면 삽입되지 않았음
int insert_flight_path(Flight* flight, char start, char end) {
    int start_num = start - ALPHA_ASCII;
    int end_num = end - ALPHA_ASCII;
    City* end_city = flight->list[end_num];

    int exist = find_flight_path(flight, start, end);
    if (exist == 0) {
        City* city = (City*) malloc(sizeof(City));
        city->alpha = end;
        city->x = end_city->x;
        city->y = end_city->y;
        city->next_city = flight->list[start_num]->next_city;
        
        flight->list[start_num]->next_city = city;
        return 1;
    }
    return 0;
}

int find_flight_path_count(Flight* flight, char city) {
    int count = 0;
    int city_num = city - ALPHA_ASCII;
    City* current_city = flight->list[city_num];
    City* n_city = current_city -> next_city;
    while (n_city != NULL) {
        count++;
        n_city = n_city->next_city;
    }
    return count;
}

void init_flight_random_path(int seed, Flight* flight, char start) {
    // 시작하는 도시에서 갈 수 있는 경로의 개수
    int start_count = find_flight_path_count(flight, start) - 1;
    srand((unsigned int) time(NULL) + seed);
    while (start_count < 10) {
        // 도착하는 도시에서 갈 수 있는 경로의 개수
        char end = 'a' + rand()%26;
        int end_count = find_flight_path_count(flight, end);
        if (end_count >= 26) {
            continue;
        }
        if (end == start) {
            continue;
        }
        int type = insert_flight_path(flight, start, end);
        if (type) {
            insert_flight_path(flight, end, start);
            start_count++;
        }
    }
}

void print_flight_path(Flight* flight){
    printf("=========== 비행 경로 출력 ===========\n");
    for (int i = 0; i < 26; i++) {
        City* city = flight->list[i];
        printf("도시 %c의 경로", city->alpha);
        while(city != NULL){
            printf("->%c", city->alpha);
            city = city->next_city;
        }
        printf("\n");
    }
    printf("\n");
}


static int start_connected_path[26];
void find_exist_path(Flight* flight, char start) {
    // 시작하는 도시와 연결되어 있는 요소들을 찾기
    int start_num = start - ALPHA_ASCII;
    for (int i = 0; i < 26; i++) {
        start_connected_path[i] = 0;
    }
    start_connected_path[start_num] = 1;

    City* start_city = flight->list[start_num];
    City* n_city = start_city->next_city;
    
    while (n_city != NULL) {
        int num = n_city->alpha - ALPHA_ASCII;
        start_connected_path[num] = 1;
        n_city = n_city -> next_city;    
    }
}

// ---------------------- departure 관련 함수 ----------------------

// 출발 시간
static int departure[31][26][26];

// 시간을 30분 간격으로 진행
// 24시간 이기에 최대 48개가 생김
// 예를 들어, 00:00은 0으로 지정 00:30은 1로 지정 10:00은 20으로 지정
void init_departure(Flight* flight, char start, int day) {
    int start_num = start - ALPHA_ASCII;
    for (int i = 0; i < 26; i++) {
        departure[day][start_num][i] = 0;
    }
    srand((unsigned int) time(NULL) + day + start_num);
    
    // 시작하는 도시와 연결되어 있는 요소들을 찾기
    find_exist_path(flight, start);

    // 도착지 탐색 후 시간 지정
    for (int end = 0; end < 26; end++) {
        // 출발지와 다른지 확인
        if (end != start_num) {
            if (start_connected_path[end] == 1) {
                departure[day][start_num][end] = rand()%48;
            }
        } else {
            departure[day][start_num][start_num] = -1;
        }
    }
}

// 특정 날짜의 출발 시간을 출력함
void print_departure(int day) {
    printf("========= %d 일날 출발 시간입니다. =========\n", day + 1);
    for (int i = 0; i < 26; i++) {
        char start = 'a' + i;
        printf("%c|", start);
    }
    printf("\n");
    for (int i = 0; i < 26; i++) {
        char start = 'a' + i;
        for (int j = 0; j < 26; j++) {
            char end = 'a' + j;
            printf("%d|", departure[day][i][j]);
        }
        printf("%c\n", start);
    }
}

// ---------------------- bfs 함수 ----------------------
void bfs(Flight* flight, char start, char end) {
    int start_num = start - ALPHA_ASCII;
    int end_num = end - ALPHA_ASCII;

    int front = 0;
    int rear = 0;

    int visited[26] = {0};
    int queue[10000];

    queue[0] = start_num;
    visited[start_num] = 1;
    rear++;

    printf("출발지 : %c\n", start);
    while (front < rear) {
        int city_num = queue[front];
        front++;

        // 출발지와 연결된 요소를 갱신함
        char city = 'a' + city_num;
        find_exist_path(flight, city);
        for (int i = 0; i < 26; i++) {
            if (i != city_num) {
                if (start_connected_path[i] == 1 && visited[i] == 0) {
                    printf("%c->", start);
                    queue[rear] = i;
                    rear++;
                    visited[i] = 1;
                    char next_city = 'a' + i;
                    if (next_city == end) {
                        return;
                    }
                }
            }
        }
    }
}

int main() {
    Flight* flight = (Flight*)malloc(sizeof(Flight));
    // 초기 도시 위치 배열 생성
    init_city_location(1);

    // 비행 그래프 생성
    init_flight(flight);

    // 비행 경로 삽입
    for (int i = 0; i < 26; i++) {
        char start = 'a' + i;
        init_flight_random_path(i, flight, start);
    }

    // 비행 경로 출력
    print_flight_path(flight);

    // 도시 위치 삽입
    print_city_location(flight);

    // 출발 시간 입력
    for (int day = 0; day < 31; day++) {
        for (int i = 0; i < 26; i++) {
            char start = 'a' + i;
            init_departure(flight, start, day);
        }
    }

    print_departure(2);

    free(flight);
    return 0;
}