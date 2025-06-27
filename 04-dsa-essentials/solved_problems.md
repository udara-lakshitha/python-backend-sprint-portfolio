# DSA Essentials: Arrays & Hashing

This file logs my solutions and understanding of key problems in the "Arrays & Hashing" category. Each entry includes the problem, the core pattern used, time/space complexity, and the optimized solution logic.

---

### LC 217: Contains Duplicate

- **Link:** [https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/)
- **Pattern:** Hash Set for Efficient Lookups
- **Time Complexity:** O(n) - We iterate through the list once to build the set.
- **Space Complexity:** O(n) - In the worst case, the set stores all n unique elements.
- **Core Logic (Pythonic One-Liner):**
    ```python
    # The most concise solution. A set by definition cannot contain duplicates.
    # If the length of the set is less than the length of the list,
    # it means duplicates were present and were removed.
    return len(set(nums)) != len(nums)
    ```

### LC 242: Valid Anagram

- **Link:** [https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/)
- **Pattern:** Fixed-Size Array as a Frequency Map
- **Time Complexity:** O(n) - We iterate through the strings once. n is the length of the strings.
- **Space Complexity:** O(1) - The counts array is always of size 26, regardless of the input string length. This is constant space.
- **Core Logic (Optimal Array Method):**
    ```python
    # This solution is optimal for a known, limited character set.
    if len(s) != len(t):
            return False
        counts = [0] * 26
        for i in range(len(t)):
            counts[ord(t[i]) - ord('a')] += 1
            counts[ord(s[i]) - ord('a')] -= 1
        
        for count in counts:
            if count != 0:
                return False
        return True
    ```

### LC 1: Two Sum

- **Link:** [https://leetcode.com/problems/two-sum/]( https://leetcode.com/problems/two-sum/)
- **Pattern:** One-Pass Hash Map for "Seen" Values
- **Time Complexity:** O(n) - A single pass through the list.
- **Space Complexity:**  O(n) - In the worst case, the hash map stores all n elements.
- **Core Logic:**
    ```python
    my_dict = {}
    for i in range(len(nums)):
        if target - nums[i] in my_dict:
            return [my_dict.get(target - nums[i]), i]
        else:
            my_dict.update({nums[i]: i})
    ```

# DSA Essentials: Two Pointers

This section covers problems solved using the Two Pointers pattern, a technique for optimally traversing data structures in a single pass.

---

### LC 125: Valid Palindrome

- **Link:** [https://leetcode.com/problems/valid-palindrome/](https://leetcode.com/problems/valid-palindrome/)
- **Pattern:** Converging Two Pointers
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Core Logic (Optimal In-Place Solution):**
    ```python
    s = s.strip()
    s = s.lower()
    s = s.replace(" ", "")
    for char in string.punctuation:
        s = s.replace(char, "")
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
    ```

### LC 121: Best Time to Buy and Sell Stock

- **Link:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- **Pattern:** Single Pass with Minimum Price Tracking (A variation of Two Pointers)
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)
- **Core Logic:**
    ```python
    left = 0
        right = left + 1
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
    ```