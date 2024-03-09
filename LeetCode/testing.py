# from leetcode import *
# from horology import Timing
#
# for x in range(12):
#     with Timing(name="time: "):
#         mergeTwoLists_selection_0([0, 1, 2], [1, 2, 4])
# print("(╬ಠ益ಠ)")
# for x in range(10):
#     with Timing(name="time: "):
#         mergeTwoLists_selection([0, 1, 2], [1, 2, 4])

# #sorting visualisation
# #https://towardsdatascience.com/5-sorting-algorithms-in-python-c7ece9df5dd6
# import sortings
# from horology import Timing
# from random import shuffle
#
#
# def repeat_Timing(list1, list2, sort_func):
#     def mergeTwoLists(list1, list2, sorting):
#         return sorting(list1 + list2)
#     for times in range(10):
#         with Timing(name="time: ", unit="ms"):
#             mergeTwoLists(list1, list2, sort_func)
#
#
# list1, list2 = [3, 6, 1], [4, 2, 5]
#
# for c in range(8):
#     list1 *= 2
#     list2 *= 2
#     shuffle(list1)
#     shuffle(list2)
#     print("\n\n\nSize of list:", len(list1+list2))
#     print("\npython's default sorted(Tim Sort's sorting)")
#     # for x in range(10):
#     #     with Timing(name="time: ", unit="ms"):
#     #         mergeTwoLists(list1, list2, sorted)
#     repeat_Timing(list1, list2, sorted)
# #
#     print("\nbubble sort")
#     # for x in range(10):
#     #     with Timing(name="time: "):
#     #         mergeTwoLists(list1, list2, sortings.bubble)
#     repeat_Timing(list1, list2, sortings.bubble)
# #
#     print("\nselection sort")
#     # for x in range(10):
#     #     with Timing(name="time: "):
#     #         mergeTwoLists(list1, list2, sortings.selection)
#     repeat_Timing(list1, list2, sortings.selection)
#
# #
#     print("\ninsertion")
#     # for x in range(10):
#     #     with Timing(name="time: "):
#     #         mergeTwoLists(list1, list2, sortings.insertion)
#     repeat_Timing(list1, list2, sortings.insertion)
# #
#     print("\nmerge")
#     # for x in range(10):
#     #     with Timing(name="time: "):
#     #         mergeTwoLists(list1, list2, sortings.merge)
#     repeat_Timing(list1, list2, sortings.merge)
# #
#     print("\nquicksort")
#     def quickSort(array, low, high):
#         def partition(array, low, high):
#             pivot = array[high]
#             i = low - 1
#             for j in range(low, high):
#                 if array[j] <= pivot:
#                     i = i + 1
#                     (array[i], array[j]) = (array[j], array[i])
#             (array[i + 1], array[high]) = (array[high], array[i + 1])
#             return i + 1
#
#         if low < high:
#             pi = partition(array, low, high)
#             quickSort(array, low, pi - 1)
#             quickSort(array, pi + 1, high)
#
#         return array
#
#
#     for x in range(10):
#         with Timing(name="time: ", unit="ms"):
#             list3 = list1+list2
#             quickSort(list3, 0, len(list3)-1)

# def forTiming(func, text):
#     for x in range(10):
#         with Timing(name="time: ", unit="ms"):
#             func(text)
#
# print("\nlengthOfLongestSlllengthOfLongestSulengthOfLongestSubstringgthOfLongestSubstringestSubstringtSubstringengthOfLongestSubstringtring")
#
# forTiming(lengthOfLongestSubstring, "lengthOfLongestSlllengthOfLongestSulengthOfLongestSubstringgthOfLongestSubstringestSubstringtSubstringengthOfLongestSubstringtring")
# print()
# forTiming(lengthOfLongestSubstring_1, "lengthOfLongestSlllengthOfLongestSulengthOfLongestSubstringgthOfLongestSubstringestSubstringtSubstringengthOfLongestSubstringtring")
#
# print("\naab")
#
# forTiming(lengthOfLongestSubstring, "aab")
# print()
# forTiming(lengthOfLongestSubstring_1, "aab")
#
# print("\nawwxmur")
#
# forTiming(lengthOfLongestSubstring, "awwxmur")
# print()
# forTiming(lengthOfLongestSubstring_1, "awwxmur")



# # # # 26. Remove Duplicates from Sorted Array
# from horology import Timing
# import leetcode
# def for_Timing(func, nums):
#     with Timing(unit='ms'):
#         func(nums)
#
#
# nums = [0, 0, 1, 2, 2, 3, 4, 4, 5]
# for x in range(8):
#     for_Timing(leetcode.removeDuplicates, nums)
#     for_Timing(leetcode.removeDuplicates_1, nums)
#     print()
#     nums *= 4

