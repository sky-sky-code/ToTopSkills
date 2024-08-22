def interaction_set():
    nums1 = {int(i) for i in input().split()}
    nums2 = {int(i) for i in input().split()}

    return sorted(nums1 & nums2)
