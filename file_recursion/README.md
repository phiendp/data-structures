# File Recursion

## Introduction
The goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c".

## Approach
A recursive solution is used that will scan all of the sub-directories, then add the files with the targeted suffix to the final result array.

## Analysis
- Since we need to check each file and directory, the time complexity is O(N), in which N is the total number of files and directories in the search space. Furthermore, since we are using a resursive solution, the call stack will take linear space to the depth of the subdirectories, which equals the recursion's level.
- The space complexity is O(M), in which M is the number of files that match the targeted suffix.
