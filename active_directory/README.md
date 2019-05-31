# Active Directory

## Introduction
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids. The goal is to write a function that provides an efficient look up of whether the user is in a group.

## Approach
We will use recursion to solve this problem. The base case will be whether the given user is in the current group's user list. Otherwise, we will recursively check the user's availability in other subgroups. If no group contains that user, the result is False.

## Analysis
- We will traverse all of the users and groups in a group. Let the total numbers of users and groups N, then time complexity will be O(N).
- The space complexity of this implementation depends on the number of groups within a group, since we are recursively checking each subgroup, and the recursion will occupy the call stack with function calls.

