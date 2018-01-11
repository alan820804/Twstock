import requests
import csv
import os
import pandas as pd
import numpy as np

str=input("請輸入股票代碼: ")

Stock_Number=int(str)

str=input("請輸入開始查詢的年分: ")

Start_Year=int(str)

str=input("請輸入開始查詢的月份: ")

Start_Month=int(str)

str=input("請輸入結束查詢的年分: ")

End_Year=int(str)

str=input("請輸入結束查詢的年份: ")

End_Month=int(str)


if (Start_Year == End_Year):

	counter=1

	for x in range(Start_Month,End_Month+1):
		
		
		r = requests.post('http://app.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAYMAIN.php',data={
                                  'download': 'csv',
                                  'query_year':Start_Year,
                                  'query_month':x,
                                  'CO_ID':Stock_Number
                                  })
		f = open('/home/centos/Test.txt','w')
		f.write(r.text)
		f.close()
		f = open('/home/centos/Test.txt','r')
		data_list=f.readlines()
		f.close()
		os.remove("/home/centos/Test.txt")
		if (counter == 1):
			f=open("/home/centos/Final_Result.txt","a+")
			f.writelines(data_list)
			f.close() 
		else:
			del data_list[:2]
			f=open("/home/centos/Final_Result.txt","a+")
			f.writelines(data_list)
			f.close()

		counter = counter+1

else:

	for x in range(Start_Year,End_Year+1):
		if (x == Start_Year):

			counter = 1

			for y in range(Start_Month,13):
				r = requests.post('http://app.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAYMAIN.php',data={
                                  'download': 'csv',
                                  'query_year':x,
                                  'query_month':y,
                                  'CO_ID':Stock_Number
                                  })
				f = open('/home/centos/Test.txt','w')
				f.write(r.text)
				f.close()
				f = open('/home/centos/Test.txt','r')
				data_list=f.readlines()
				f.close()
				os.remove("/home/centos/Test.txt")
				if (counter == 1):
					f=open("/home/centos/Final_Result.txt","a+")
					f.writelines(data_list)
					f.close()
				else:
					del data_list[:2]
					f=open("/home/centos/Final_Result.txt","a+")
					f.writelines(data_list)
					f.close()

				counter = counter+1


		elif(x == End_Year):

			for y in range(1,End_Month+1):
				r = requests.post('http://app.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAYMAIN.php',data={
                                  'download': 'csv',
                                  'query_year':	x,
                                  'query_month':y,
                                  'CO_ID':Stock_Number
				})
				f = open('/home/centos/Test.txt','w')
				f.write(r.text)
				f.close()
				f = open('/home/centos/Test.txt','r')
				data_list=f.readlines()
				f.close()
				os.remove("/home/centos/Test.txt")
				del data_list[:2]
				f=open("/home/centos/Final_Result.txt","a+")
				f.writelines(data_list)
				f.close()

                            			


		else:
			for y in range(1,13):
				r = requests.post('http://app.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAYMAIN.php',data={
                                  'download': 'csv',
                                  'query_year': x,
                                  'query_month':y,
                                  'CO_ID':Stock_Number
				})
				f = open('/home/centos/Test.txt','w')
				f.write(r.text)
				f.close()
				f = open('/home/centos/Test.txt','r')
				data_list=f.readlines()
				f.close()
				os.remove("/home/centos/Test.txt")
				del data_list[:2]
				f=open("/home/centos/Final_Result.txt","a+")
				f.writelines(data_list)
				f.close()


with open( "/home/centos/Final_Result.txt" , "r") as txt_file:

	with open("/home/centos/Final_Result.csv","w") as csv_file:

		in_txt=csv.reader(txt_file, delimiter=',') # Interator

		out_csv=csv.writer(csv_file)
		
		out_csv.writerows(in_txt)

os.remove("/home/centos/Final_Result.txt")

	
