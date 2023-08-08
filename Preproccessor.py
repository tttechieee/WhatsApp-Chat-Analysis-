import re
import pandas as pd

def preprocess(data):
    pattern = '\d{2}/\d{2}/\d{2}, \d{2}:\d{2}:\d{2}'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_data': dates})
    # convert message_data type
    df['message_data'] = pd.to_datetime(df['message_data'], format='%d/%m/%y, %H:%M:%S')

    # rename column to 'data'
    df.rename(columns={'message_data': 'date'}, inplace=True)

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

    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['only_date'] = df['date'].dt.date
    df['date'].dt.day_name()
    df['day_name'] = df['date'].dt.day_name()
    df['month'] = df['date'].dt.month_name()
    df['month'].value_counts()
    df['hours'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    period = []
    for hours in df[['day_name', 'hours']]['hours']:
        if hours == 23:
            period.append(str(hours) + "-" + str('00'))
        elif hours == 0:
            period.append(str('00') + "-" + str(hours + 1))
        else:
            period.append(str(hours) + "-" + str(hours + 1))
    df['period'] = period

    return df
