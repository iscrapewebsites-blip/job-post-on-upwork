from lxml import html

page  = ''
with open('page.html', 'r', encoding='utf-8') as f:
     page  = f.read()

tree = html.fromstring(page)

elements = tree.xpath('//*[@id="main"]/div[4]/div[4]/div[2]/div[2]/div[2]/section/article')
print(len(elements))

data = []
for el in elements:
     dict = {}
     title = el.xpath('.//div/h2/a')
     if len(title)!=0:
          title = title[0].text_content()
          clean_title = ' '.join(title.split())
          dict['title'] = clean_title
     
     desc = el.xpath('.//div/div/p')
     if len(desc)!=0:
          desc = desc[0].text_content()
          clean_desc = ' '.join(desc.split())
          dict['description'] = clean_desc

     skills = el.xpath('.//div[@data-test="TokenClamp JobAttrs"]')
     if len(skills)!=0:
          skills = skills[0].text_content()
          skill_set = ' '.join(skills.split())
          dict['skills'] = skill_set
     
     job = el.xpath('.//div/ul[@data-test="JobInfo"]')
     if len(job)!=0:
          job = job[0]

     if len(job)!=0:
          try:
               job_type = job.xpath('.//li[@data-test="job-type-label"]')[0].text_content()
               job_type = ' '.join(job_type.split())
               dict['job_type'] = job_type
          except:
               pass
          try:
               experience = job.xpath('.//li[@data-test="experience-level"]')[0].text_content()
               experience = ' '.join(experience.split())
               dict['experience'] = experience
          except:
               pass
          try:
               rate = job.xpath('.//li[@data-test="job-type-label"]')[0].text_content()
               rate = ' '.join(rate.split())
               dict['rate'] = rate
          except:
               pass
          try:
                budget = job.xpath('.//li[@data-test="is-fixed-price"]')[0].text_content()
                budget = ' '.join(budget.split())
                dict['rate'] = budget
          except:
               pass

     loc = el.xpath('.//div/ul/li[@data-test="location"]')
     if len(loc)!=0:
          loc = loc[0].text_content()
          loc = ' '.join(loc.split())
          loc = ' '.join(loc.split()[1:])
          dict['location'] = loc
     
     data.append(dict)

import json
data_str = json.dumps(data)

with open('jobs.json', 'w', encoding='utf-8') as f:
     f.write(data_str)