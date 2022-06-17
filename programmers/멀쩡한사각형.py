import math

# w + h - w와 h의 최대 공약수를 하면 겹치는 곳을 찾을 수 있다.
def solution(w,h):
    return w*h - (w + h - math.gcd(w, h)) 