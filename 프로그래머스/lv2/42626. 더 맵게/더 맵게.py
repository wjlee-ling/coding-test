import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while heapq:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + 2*second)
        answer += 1
    """heapq.heapify(scoville)
    while len(scoville) >= 2:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        second = heapq.heappop(scoville)
        new = first + 2*second
        answer += 1
        if scoville == [] and new < K:
            return -1
        heapq.heappush(scoville, new)"""
    return answer