# webscraping-and-report-generation
Overview: I wrote this program and shell script to comb Google News for particular search terms (over a defined date range) and return results in a particular format. 

Motivation: The motivation for this program was a task for my work - I am in charge of compiling daily news reports for particular industries and accounts, and I wanted to automate that process to cut down on the time I spend on it. Typically, this process would take me about an hour or more between running all the searches, finding the relevant articles, and getting all of the information needed for the email newsletter (article title, source, URL, and date published).

Results: Now, the entire process takes me about 15 minutes, including writing the actual email containing the newsletter. Each time I run the script, the only thing I have to edit is the date range I am searching over. After that, running the bash script executes the Python program and nicely formats and displays the results in a Word document. The only thing left to do is skim the document (organized by search term), see which articles are relevant, and copy and paste the entry over to the email.
