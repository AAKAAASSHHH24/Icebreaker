from dotenv import load_dotenv
from linked import scrapeLinkedIn
 
load_dotenv()
 
data = scrapeLinkedIn()
print(data)