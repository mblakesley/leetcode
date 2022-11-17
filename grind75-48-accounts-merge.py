# https://leetcode.com/problems/accounts-merge/
class Solution:
    # TODO: try "union find" AND/OR speed this up by just noting relationships at first, then rewriting all at the end
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        users = []
        user_eml_map = {}  # {user index: {emails}}
        eml_user_map = {}  # {email: user index}
        for i, account in enumerate(accounts):
            user, emails = account[0], set(account[1:])
            users += [user]
            to_override = []

            # use eml_user_map to find users to update
            for email in emails:
                old_i = eml_user_map.get(email)
                if old_i is not None and old_i != i:
                    to_override += [old_i]

            # take the emails away from those users
            for old_i in to_override:
                emails |= user_eml_map[old_i]
                user_eml_map[old_i] = set()

            # update both dicts
            user_eml_map[i] = emails
            for email in emails:
                eml_user_map[email] = i

        accounts = []
        for i, user in enumerate(users):
            emails = user_eml_map.get(i)
            if emails:
                accounts += [[user, *sorted(emails)]]
        return accounts
