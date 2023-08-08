#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import pandas as pd


# In[ ]:


f=open('YOUR FILE URL','r',encoding='utf-8')


# In[ ]:


data=f.read()


# In[ ]:


print(data)


# In[ ]:


pattern='\d{2}/\d{2}/\d{2}, \d{2}:\d{2}:\d{2}'


# In[ ]:


pattern = r'\d{2}/\d{2}/\d{2}, \d{2}:\d{2}:\d{2}'
messages = re.split(pattern, data)[1::]
print(messages)


# In[ ]:


dates = re.findall(pattern, data)
print(dates)


# In[ ]:


df=pd.DataFrame({'user_message':messages,'message_data':dates})
#convert message_data type
df['message_data'] = pd.to_datetime(df['message_data'], format='%d/%m/%y, %H:%M:%S')



# rename column to 'data'
df.rename(columns={'message_data': 'date'}, inplace=True)

# Display the DataFrame
df.head()


# In[ ]:


df.shape


# In[ ]:



# Assuming you have already loaded the DataFrame 'df' with the 'user_message' column

users = []
messages = []

for message in df['user_message']:
    entry = re.split('([\w\W]+?):\s', message)
    if entry[1:]:  # user name
        users.append(entry[1])
        messages.append(entry[2])
    else:
        users.append('group notification')
        messages.append(entry[0])

df['user'] = users
df['message'] = messages
df.drop(columns=['user_message'], inplace=True)
df.head()


# In[ ]:


df['year']=df['date'].dt.year 


# In[ ]:


df.head()


# In[ ]:


df['month']=df['date'].dt.month_name()


# In[ ]:


df['hours']=df['date'].dt.hour


# In[ ]:


df['minute']=df['date'].dt.minute


# In[ ]:





# In[ ]:


df.head()


# In[ ]:


df[df['user'] == 'Sahil Garg Gd'].shape


# In[ ]:


words=[]
for message in df['message']:
    words.extend(message.split())
    


# In[ ]:


len(words)


# In[ ]:


df[df['message'] == 'image omitted\n['].shape[0]


# In[ ]:


from urlextract import URLExtract

extractor = URLExtract()
urls = extractor.find_urls("Let's www.gmail.com have url stackoverflow.com as an example")
urls


# In[ ]:


links  =[]
for message in df['message']:
    links.extend(extractor.find_urls(message))
    


# In[ ]:


len(links)


# In[ ]:


df


# In[ ]:


x=df['user'].value_counts().head(5)


# In[ ]:


import matplotlib.pyplot as plt
name=x.index
count=x.values


# In[ ]:


plt.bar(name,count)
plt.xticks(rotation='vertical')
plt.show()


# In[ ]:


import pandas as pd

# Assuming you have already loaded the DataFrame 'df' with the chat data

# Group the DataFrame by 'user' and count the number of messages for each user
user_message_counts = df['user'].value_counts()

# Find the user with the highest message count
most_busy_user = user_message_counts.idxmax()
most_busy_user_message_count = user_message_counts.max()

print(f"The most busiest user is '{most_busy_user}' with {most_busy_user_message_count} messages.")


# In[ ]:


round((df['user'].value_counts()/df.shape[0])*100, 2).reset_index().rename(columns={'index':'name','user':'percent'})


# In[ ]:


temp = df[df['user'] != 'Gd students👨🏻‍💻👨🏻‍🎓💖']
temp[temp['message'] != 'image omitted']


# In[ ]:



f = open('HINGLISH FILE URL', 'r')  
stop_words = f.read()


# In[ ]:


words=[]
for messsage in temp['message']:
    for word in message.lower().split():
        if word not in stop_words:
            words.append(word)
        
    


# In[ ]:


from collections import Counter
pd.DataFrame(Counter(words).most_common(20))


# In[ ]:


get_ipython().system('pip install emoji')


# In[ ]:


'''import emoji

emojis = []
for message in df['message']:
    emojis.extend([c for c in message if c in emoji.UNICODE_EMOJI['en']])
'''
#UNICODE_EMOJI module has been removed by Python in there latest version you can try in your IDE if it is available 


# In[ ]:


#pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))


# In[ ]:


df['month_num']=df['date'].dt.month


# In[ ]:


timeline = df.groupby(['year','month_num','month']).count()['message'].reset_index()


# In[ ]:


timeline


# In[ ]:


time=[]
for i in range(timeline.shape[0]):
    time.append(timeline['month'][i]+"-" +str(timeline['year'][i]))


# In[ ]:


timeline['time']=time


# In[ ]:


timeline


# In[ ]:


plt.plot(timeline['time'],timeline['message'])
plt.xticks(rotation='vertical')
plt.show()


# In[ ]:


df['only_date']=df['date'].dt.date


# In[ ]:


daily_timeline=df.groupby('only_date').count()['message'].reset_index()


# In[ ]:


plt.figure(figsize=(18,18))
plt.plot(daily_timeline['only_date'],daily_timeline['message'])


# In[ ]:


df['date'].dt.day_name()


# In[ ]:


df['day_name'].value_counts()


# In[ ]:


df.head()


# In[ ]:


period=[]
for hour in df[['day_name','hours']]['hours']:
    if hour==23:
        period.append(str(hours) + "-" + str('00'))
    elif hour == 0:
        period.append(str('00') + "-" + str(hour+1))
    else:
        period.append(str(hour) + "-" + str(hour+1))


# In[ ]:


df['period'] = period


# In[ ]:


df.samples(5)


# In[ ]:


import searborn as sns
plt.figure(figsize=(20,6))
sns.heatmap(df.pivot_table(index='day_name',columns='period',values='message',aggfunc='count').fillna(0))
plt.yticks(rotation='horizontal')
plt.show


# In[ ]:





# In[ ]:




