# Union and Intersection

## Introduction
Given two linked lists, return a linked list that is composed of either the union or intersection, respectively.

## Aprroach
In both problems, a set will be used since it can help eliminate the duplications from both given list.
- For union, we will traverse the first list, add each element to the set and the result linked list. Then, we traverse the second list, but only append the element that is not available in the set into the result linked list.
- For intersection, we will keep track of non-duplicated elements from the first list. Then, when iterating the second list, we will append those elements that are already available in our set into the result linked list, which means we keep track of the same element from both lists.

## Analysis
Let N be the number of elements in both linked lists.
- The time complexity will be O(N), since we will need to traverse both the list for both union and intersection operation.
- The space complexity both union and intersection will be O(N)
