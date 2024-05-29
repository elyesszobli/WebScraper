from bs4 import BeautifulSoup

def find_html_page(page,found_emails):
    find_emails(page,found_emails)
    for link in page.find_all('a'):
        if not link['href'].endswith('html'):
            continue
        if 'index.html' in link['href']:
            continue
        else:
            page_to_open = BeautifulSoup(open(link['href'],'r',encoding='utf-8'),'html.parser')
            find_html_page(page_to_open,found_emails)
    return found_emails


def find_emails(page,found_emails):
    for email in page.find_all('a'):
        if '@' in email['href']:
            found_email = email['href'].split(':')[-1]
            if found_email not in found_emails:
                found_emails.append(found_email)
                
def main():
    with open('index.html','r',encoding='utf-8') as html_file:
        html_content = html_file.read()
        soup = BeautifulSoup(html_content,'html.parser')
        unique_emails = []
        found = find_html_page(soup,unique_emails)
        print(found)
        
if __name__ == '__main__':
    main()