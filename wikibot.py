import wikipedia

#https://pypi.org/project/wikipedia/
#wikipedia.summary("Facebook", sentences=1) 

def scrape(name="Microsoft", length=1):
    result = wikipedia.summary(name, sentences=length)
    print(result)

print(scrape("Microsoft"))