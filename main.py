import whois

sites = ['spotify.com', 'facebook.com', 'instagram.com']
companies = [whois.whois(s).org for s in sites]
emails = [whois.whois(s).emails for s in sites]
print(companies)
print(emails)


#res = whois.whois('spotify.com')
#print(res)
#print(res.org)
#print(res.creation_date)
