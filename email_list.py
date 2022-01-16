def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(user +'@'+ domain)
    return(emails)


print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": [
      "barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
#Output:
# ['clark.kent@gmail.com', 'diana.prince@gmail.com', 'peter.parker@gmail.com', 'barbara.gordon@yahoo.com', 
# 'jean.grey@yahoo.com', 'bruce.wayne@hotmail.com']