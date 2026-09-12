class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot(arr):
            start = 0
            end = len(nums)-1
            while start <= end:
                mid = start + (end-start) //2
                if mid < end and nums[mid] > nums[mid+1]:
                    return mid
                    
                elif mid > start and nums[mid] < nums[mid-1]:
                    return mid-1
                    
                elif nums[mid] <= nums[start]:
                    end = mid -1
                else:
                    start = mid+1
            return -1  
        
        pivot = findPivot(nums)
        print(pivot)


        def findInc(arr, pivot, tar):
            start = 0
            end = len(arr) -1
            if pivot == -1:
                end = len(arr) -1
            elif tar == arr[pivot]:
                return pivot
            elif tar >= arr[0]:
                end = pivot -1
            else:
                start = pivot +1

            while start <= end:
                mid = start + (end-start) //2
                if tar < arr[mid]:
                    end = mid-1 
                elif tar > arr[mid]:
                    start = mid+1
                else:
                    return mid

            return -1
        

        return findInc(nums, pivot, target)
        