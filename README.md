# 🚀 Day 24 – Continuous Subarray Sum

## 📌 Problem

Given an integer array `nums` and an integer `k`, return `true` if the array has a continuous subarray of size at least 2 whose elements sum up to a multiple of `k`.

In other words:

```python
subarray_sum % k == 0
```

### Example

```python
Input: nums = [23,2,4,6,7], k = 6
Output: True
```

Explanation:

```python
[2,4] sums to 6, and 6 % 6 == 0
```

---

# 💡 Approach – Prefix Sum + Hash Map

We use:

* Running prefix sum
* Hash map to store remainders

### Key Observation

If:

```python
prefix_sum % k
```

produces the same remainder at two different indices,
then the subarray between those indices has a sum divisible by `k`.

---

# ⚙️ Python Solution

```python
class Solution:
    def checkSubarraySum(self, nums, k):
        remainder_map = {0: -1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            remainder = prefix_sum % k

            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i

        return False
```

---

# 🧠 Dry Run

Input:

```python
nums = [23,2,4,6,7]
k = 6
```

| Index | Prefix Sum | Remainder | Map                    | Result   |
| ----- | ---------- | --------- | ---------------------- | -------- |
| 0     | 23         | 5         | {0:-1, 5:0}            | continue |
| 1     | 25         | 1         | {0:-1, 5:0, 1:1}       | continue |
| 2     | 29         | 5         | remainder already seen | ✅        |

Final Answer:

```python
True
```

---

# ⏱️ Complexity Analysis

| Complexity       | Value        |
| ---------------- | ------------ |
| Time Complexity  | O(n)         |
| Space Complexity | O(min(n, k)) |

---

# 🧠 Key Learning

This problem teaches:

* Prefix sum technique
* Modular arithmetic
* Efficient hash map usage

Combining prefix sums with hashing is a powerful pattern for subarray problems.

---

# ⚠️ Important Insight

If two prefix sums give the same remainder when divided by `k`, their difference is divisible by `k`.

That mathematical observation is the foundation of the solution.

---

# 🔗 LeetCode

Continuous Subarray Sum – LeetCode #523

---

# 📈 Progress Log

✅ Day 24 of DSA Journey
