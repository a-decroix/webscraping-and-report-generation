import pandas as pd
from pygooglenews import GoogleNews
import datetime

#initiate the GoogleNews client
gn = GoogleNews()

#dates are changed daily here in actual use
def get_news(search):
    stories = []
    start_date = datetime.date(2022,1,13)
    end_date = datetime.date(2022,1,14)
    delta = datetime.timedelta(days=1)
    date_list = pd.date_range(start_date, end_date).tolist()
    
    for date in date_list[:-1]:
        result = gn.search(search, from_=date.strftime('%Y-%m-%d'), to_=(date+delta).strftime('%Y-%m-%d'))
        newsitem = result['entries']

	#This pulls out the attributes I need to grab - title, link, and date published
        for item in newsitem:
            story = {
                'title':item.title,
                'link':item.link,
                'published':item.published
            }
            stories.append(story)

    return stories

#define a list of search terms (left blank here)
search_terms = []

#get the results for each search term
for term in search_terms:
	results_list = get_news(term)
	
#write results to 'results.txt'
	with open('results.txt', 'a') as f:
		f.write(term)
		f.write("\n")
		f.write('---------------------------------------')
		f.write("\n")
		
		for article in results_list:
			f.write(article['title'])
			f.write("\n")
			f.write(article['link'])
			f.write("\n")
			f.write(article['published'])
			f.write("\n \n")

#success message			
print('Data is written to text file successfully.')
