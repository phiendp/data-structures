# Active Directory

## Introduction
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids. The goal is to write a function that provides an efficient look up of whether the user is in a group.

## Approach
We will use recursion to solve this problem. The base case will be whether the given user is in the current group's user list. Otherwise, we will recursively check the user's availability in other subgroups. If no group contains that user, the result is False.

## Analysis
Let the total numbers of users is N, and the total number of groups is M.
- The time complexity will be O(N * M), because we need to check all of the groups and users in the worst case.
- The space complexity is also O(N * M), because of the resursive call stack.
