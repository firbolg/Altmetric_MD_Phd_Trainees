#environment: conda minimal_ds
#thanks: PyAltmetric, laurenrevere, wearp

from pyaltmetricmod import Altmetric, Citation, HTTPException, AltmetricException 
import csv 
import time 

a = Altmetric ()
source = 'test.csv'


article = a.doi('10.1101/2020.05.04.20090555')

article2 = a.doi('10.1063/1.4819200')

citation = Citation(article2)

api_data = citation.get_fields('doi', 'pmid', 'title', 'authors', 'altmetric_jid', 'cited_by_policies_count', 'cited_by_msm_count', 'cited_by_tweeters_count', 
               'cited_by_feeds_count', 'cited_by_accounts_count', 'cited_by_posts_count', 'readers_count', 'cohorts', 'context', 'journal', 
               'similar_age_3m', 'similar_age_journal_3m', 'score', 'url')

print(api_data)

# with open('test.csv', 'r') as file:
    #dois = file.read()
    #with open('Altmetrics_MD_Phd_Trainees.csv', 'w') as outfile:
        #writer = csv.writer(outfile)
        
        #for item in infile:
           # time.sleep(.05)
           # item = item.rstrip()
          #  article = a.doi(item)
          #  if article:
             #   citation = Citation(article)
              #  api_data = citation.get_fields('doi', 'journal', 'cited_by_posts_count', 'cited_by_tweeters_count', 'cited_by_msm_count', 'cited_by_videos_count', 
               # 'cited_by_fbwalls_count', 'cited_by_gplus_count', 'cited_by_rdts_count', 'cited_by_feeds_count', 'score', 'url')
          #  else:
             #   api_data = [item, 'none']
           # writer.writerow(api_data)







