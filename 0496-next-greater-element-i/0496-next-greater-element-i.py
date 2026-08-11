class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        answer = []

        for num in nums1:

            # Find num's position in nums2
            index = nums2.index(num)

            greater = -1

            # Check elements to the right
            for i in range(index + 1, len(nums2)):

                if nums2[i] > num:
                    greater = nums2[i]
                    break

            answer.append(greater)

        return answer