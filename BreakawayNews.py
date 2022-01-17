import pandas as pd
from pygooglenews import GoogleNews
import datetime

gn = GoogleNews()

def get_news(search):
    stories = []
    start_date = datetime.date(2022,1,13)
    end_date = datetime.date(2022,1,14)
    delta = datetime.timedelta(days=1)
    date_list = pd.date_range(start_date, end_date).tolist()
    
    for date in date_list[:-1]:
        result = gn.search(search, from_=date.strftime('%Y-%m-%d'), to_=(date+delta).strftime('%Y-%m-%d'))
        newsitem = result['entries']

        for item in newsitem:
            story = {
                'title':item.title,
                'link':item.link,
                'published':item.published
            }
            stories.append(story)

    return stories


search_terms = ["Ricoh USA", "Ricoh Americas", "Ricoh North America", "bta + Ricoh", "Ricoh + patent infringement", "Ricoh David Levine", "Ricoh Donna Venable", "Ricoh Carsten Bruhn", "Ricoh Jim Coriddi", "Ricoh layoff", "Ricoh fired", "Kayesa Ransomware Attack Ricoh", "Ricoh print nightmare", "Mark Rowe arrested", "Jose Torres Boston area Ricoh", "alberta hip and knee clinic ransomware attack", "jesus antonio gonzalez georgia bureau of investigation", "Log4J Ricoh", "gurvinder singh arrested", "Ricoh raising prices", "Canon Solutions America", "HP Inc", "Xerox", "Koncia Minolta"]

for term in search_terms:
	results_list = get_news(term)
	

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

print('Dataframe is written to text file successfully.')
