import subprocess
import datetime
import csv
import os

with open('MacroTrends_Data_Download_UAL.csv', 'rb') as csvfile:
    # subprocess.call(['java','-jar','GetOldTweet\\got.jar'])
    stock_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    reader = list(stock_reader)
    print(len(reader))
    os.system("pause")
    for row in range(len(reader)):
        temp = ' '.join(reader[row])
        if len(temp) != 0 and temp[0] != "\"" and temp[0] != 'd':
            temp = temp.split(",")
            temp2 = ' '.join(reader[row + 1])
            temp2 = temp2.split(",")
            print(temp[0])
            temp_date = temp[0].split('-')
            temp_date2 = temp2[0].split('-')
            if int(temp_date[0]) >= 2015:
                date = datetime.datetime(int(temp_date[0]), int(
                    temp_date[1]), int(temp_date[2]))
                temp_day_1 = datetime.datetime(
                    int(temp_date2[0]), int(temp_date2[1]), int(temp_date2[2]))
                next_date2 = temp_day_1 + datetime.timedelta(days=-1)
                next_date = date + datetime.timedelta(days=1)
                temp_next_date = next_date.strftime('%Y-%m-%d')
                temp_next_date2 = temp_day_1.strftime('%Y-%m-%d')
                subprocess.call(['java', '-jar', 'GetOldTweets\\got.jar', 'querysearch=\"#UnitedAirlines\"',
                                 'since='+temp[0], 'until='+temp_next_date2, 'maxtweets=100'])
                for filename in os.listdir("."):
                    if filename == "output_got.csv":
                        os.rename(filename, temp[0]+".csv")
        else:
            continue
