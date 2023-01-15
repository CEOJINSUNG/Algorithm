# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 만약 트랜잭션이 생성이 되고 push, pop을 하면 그거를 어떻게 구현할까?
# Dict로 만들어서 사용을 할지
# transaction 이 시작되고 커밋이 완료되면 다시 트랜잭션은 1로 시작
# transaction이 시작하면 이전 트랜잭션 기록을 복사하고 넣어줌

# rollback과 commit은 트랜잭션이 존재하지 않으면 False가 됨 - Transaction 시작 지표가 필요함

from collections import defaultdict

class Solution(object):
    def __init__(self):
        # Implement your solution here
        self.transaction = 0
        self.begin_transaction = False # 처음에는 시작하지 않았기에 False
        self.stack = defaultdict(list)

    def push(self, value):
        # print("push", self.stack, "transaction", self.transaction)
        self.stack[self.transaction].append(value)

    def top(self):
        # print("top", self.stack, "transaction", self.transaction)
        if self.empty():
            return 0
        return self.stack[self.transaction][-1]

    def pop(self):
        # print("pop", self.stack, "transaction", self.transaction)
        if not self.empty():
            self.stack[self.transaction].pop()

    def begin(self):
        # print("begin", self.stack, "transaction", self.transaction)
        before_stack = self.stack[self.transaction].copy()
        self.begin_transaction = True
        self.transaction += 1
        self.stack[self.transaction] = before_stack

    def rollback(self):
        # print("rollback", self.stack, "transaction", self.transaction)
        if not self.begin_transaction:
            return False
        
        # 해당 트랜잭션 초기화
        self.stack[self.transaction] = []
        self.transaction -= 1
        if self.transaction == 0:
            self.begin_transaction = False
        return True

    def commit(self):
        # print("commit", self.stack, "transaction", self.transaction)
        if not self.begin_transaction:
            return False
        # 현재 실행 중인 트랜잭션 제거
        commit_stack = self.stack[self.transaction].copy()
        self.stack[self.transaction] = []

        self.transaction -= 1
        self.stack[self.transaction] = commit_stack
        if self.transaction == 0:
            self.begin_transaction = False
        return True

    def empty(self):
        if len(self.stack[self.transaction]) == 0:
            return True
        return False


def test():
    # Define your tests here
    sol = Solution()
    sol.push(42)
    assert sol.top() == 42, "top() should be 42"
