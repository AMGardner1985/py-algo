# Python Algorithim Practice

Making the dring for leet code practice more interesting with practicing python again from scratch.  Don't remember a lot of the practices since I haven't used it consistently in past 5 years. 

[link to template](https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4723/)


## insights and take aways
- can be overwhelming at first try to makes sure you put the problem in your own words first
- create at least a couple of test cases to test your code against, if doing tdd break them out by simplest to hardest to help you build up the algo
- start with just talking out a intuitive approach with a picture or drawing
- think about coding that or if there are data stores / algorithims you know of to make this solution better



## Two pointers 
[video link explaining] (https://www.youtube.com/watch?v=VEPCm3BCtik)
- TLDR
    - use two pointers and have some condition change one and/or other pointer
        - types
            - one pointer starts at start, other at the end
            - one pointer is slow, one pointer is fast
    - saves time and space
    - possible uses
        - finding middle node of linked list 
            - [example problem](https://leetcode.com/problems/middle-of-the-linked-list/description/)
        - finding two numbers that add to a sum in a sorted/unsorted list
            - [example problem](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)
        - finding if there is a cycle in a linked list
            - floyds cycle
        - string problems (anagram)
## Sliding window
[leetcode problems](https://leetcode.com/tag/sliding-window/)
- TLDR
    - use to put some tye of continuous subsection of a dataset through an analysis
    - has usually an time complexity of O(n)
    - reduces the amount of computation by having a subset of data and
        - able to put that subset through calculations
        - modify the subset to reduce computational load
## prefix sum
[problem list](https://leetcode.com/tag/prefix-sum/)
- TLDR
    - calculate running sum or running calculation of a data structure, and store it somehwere, this opens up a lot of other possibilities for calculations down the road
    - possible uses
        - sum of a subarrays [example leetcode 560](https://www.youtube.com/watch?v=fFVZt-6sgyo)
        - 
## efficient string building
this is more just a pattern to make a string easily 
```
def fn(arr):
    ans = []
    for c in arr:
    ans.append(c)
    return "".join(ans)
```

## reversing a linked list
- TLDR 
    - useful pattern just to reverse linked list
    