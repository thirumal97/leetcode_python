def merge_lists(nums1, nums2):

    # Replace this placeholder return statement with your code
    nums1 = nums1 + nums2
    return sorted(nums1)


def merge_lists_actual_sol(nums1, nums2):
    p1 = 0
    p2 = 0
    

    while p1 < len(nums1) and p2 < len(nums2):
        if(nums1[p1] > nums2[p2]):
            nums1.insert(p1, nums2[p2])
            p1 += 1
            p2 += 1
        
        else:
            p1 += 1

    if p2 < len(nums2):
        nums1.extend(nums2[p2:])


    return nums1    


def main():
    nums1 = [[23, 33, 35, 41, 44, 47, 56, 91, 105], [1, 2], [1, 1, 1], [6], [12, 34, 45, 56, 67, 78, 89, 99]]
    nums2 = [[32, 49, 50, 51, 61, 99], [7], [1, 2, 3, 4], [-99, -45], [100]]

    for i in range(len(nums1)):
        print(i+1, ".\tFirst list: ", nums1[i])
        print("\tSecond list: ", nums2[i])
        print("\tMerged list: ", merge_lists(nums1[i], nums2[i]))
        print("-"*100, "\n")


if __name__ == "__main__":
    main()