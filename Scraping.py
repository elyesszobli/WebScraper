from bs4 import BeautifulSoup





def find_emails(page,found_emails):
    for email in page.find_all('a'):
        if '@' in email['href']:
            found_email = email['href'].split(':')[-1]
            if found_email not in found_emails:
                found_emails.append(found_email)