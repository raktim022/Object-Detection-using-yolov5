from google.colab import drive
drive.mount("/content/drive/")

import pandas as pd
df=pd.read_csv("/content/drive/My Drive/previous_application.csv")

mondays=df[df["WEEKDAY_APPR_PROCESS_START"]=="MONDAY"]

non_null_drawing=mondays["DAYS_FIRST_DRAWING"].fillna(0)

mean_monday_drawing,std_monday_drawing=non_null_drawing.mean(),non_null_drawing.std()

mean_thresh=200000
std_thresh=180000

import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()


password=input("Enter Password:")

server.login('<Sender Email ID>',password)

if mean_monday_drawing<mean_thresh:
  msg="Notification! Mean Drawing on Monday below threshold. Value = {}".format(mean_monday_drawing)
  server.sendmail('<Sender Email ID>','<Receiver email ID>',msg)

if std_monday_drawing<std_thresh:
  msg="Notification! Std. Drawing on Monday below threshold. Value = {}".format(std_monday_drawing)
  server.sendmail('<Sender Email ID>','<Receiver email ID>',msg)
