__author__ = 'Alicia'
email = input('Please enter your email address: ').strip()


def valid(s):
    l = ['com', 'gov', 'edu', 'org', 'mil', 'net']
    try:
        username, domaingtld = s.split('@')
        domain, gtld = domaingtld.split('.')
        if gtld in l:
            return username, domain, gtld
        else:
            return 'Invalid gtld \nA valid gtld is .com, .gov, .edu, .org, .mil, or .net \nPlease try again.'
    except ValueError:
        return 'Your email must be of the form username@domain.gTLD'



print(valid(email))