// https://leetcode.com/problems/valid-parentheses/
// 80th percentile
function isValid(s: string): boolean {
    const BRACKETS = {
        '(': ')',
        '[': ']',
        '{': '}',
    }
    let closeBracketStack: string[] = []
    for (let bracket of s) {
        let closeBracket = BRACKETS[bracket]
        if (closeBracket !== undefined) {
            closeBracketStack.push(closeBracket)
        } else if (bracket !== closeBracketStack.pop()) {  // also handles undefined pop
            return false
        }
    }
    return !closeBracketStack.length
}