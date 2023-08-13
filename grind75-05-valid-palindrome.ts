// https://leetcode.com/problems/valid-palindrome/

// O(n) - 70th percentile
function isPalindrome(s: string): boolean {
    const ALPHANUM = new Set('abcdefghijklmnopqrstuvwxyz0123456789')
    // not using flat str here b/c its immutability makes looped '+=' inefficient
    let charList: string[] = []
    for (let char of s.toLowerCase()) {
        if (ALPHANUM.has(char)) {
            charList.push(char)
        }
    }
    return charList.join('') === charList.reverse().join('')
}
