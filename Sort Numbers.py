def solution(nums: list) -> list:
    try:
        nums.sort()
        return nums
    except:
        if nums == None:
            return []
        else:
            return nums


print(solution([]))