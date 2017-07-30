## Start Coding

Leetcode 139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

```
def word_break(s, words):
    dp = [False] * len(words)
    for i in xrange(len(words)):
        for w in words:
            if s[i-len(w)+1:i+1] == w and (dp[i-len(w)] or i - len(w) == -1):
                dp[i] = True
    return dp[-1]
```
