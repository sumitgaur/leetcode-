from typing import List


def numUniqueEmails(emails: List[str]) -> int:
    unique_emails = set()
    for email in emails:
        local_name, domain_name = email.split('@')[0], email.split('@')[1]
        local_name = local_name.replace('.', '').split('+')[0]
        unique_emails.add(local_name + "@" + domain_name)
    return len(unique_emails)


print(numUniqueEmails(["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"]))
