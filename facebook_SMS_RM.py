#!/usr/bin/env python
from splinter import Browser
import time

"""
Facebook SMS Recover Method V1.0

This tool will help you recover your facebook account using Facebook SMS Recover Method 

How It Work 

First You Input Your Username Or Email Or Phone Number

Second You Will Input Your New Facebook Password  

Third Your Code That You will Receive   

Last The Toole Will Open Your Browser  And Do  Everything For You .

Tools Create Using ( Splinter )

Created By XxoraxX 

"""

# Define the username and password
userid = raw_input("Please Enter Your Username Or Email Or Phone:")

userps = raw_input("Please Enter Your New Password:")

# Chose the browser (default is Firefox)
browser = Browser()

# Fill in the url
browser.visit('https://www.facebook.com/login/identify?ctx=recover&lwv=110')

# Findind Email Form
browser.find_by_id('identify_email').fill(userid)

# Findind Search Button And Clinking It 
button = browser.find_by_id("u_0_0")
button.click()

# Find Sms Button and Clicking It 
sms = browser.find_by_name("recover_method").last
sms.click()

# Find Continue Button And Clicking It 
ccontinue = browser.find_by_id("u_0_0")
ccontinue.click()

# Input reset code 
codeid = raw_input("Please Enter Your Code:")

# Find Code And Clicking It
code = browser.find_by_name("n").fill(codeid)

# Find Continue Button And Clicking It 
ccontinue = browser.find_by_id("u_0_0")
ccontinue.click()

# Post The New Password
browser.find_by_id("password_new").fill(userps)

# Find Continue And Clicking It 
ccontinue = browser.find_by_id("btn_continue")
ccontinue.click()

f = open('user.txt', 'w')
f.write("username:" + userid + "\n" + "password:" + userps + '\n')
f.close()

time.sleep(2)

# Finsih Closeing Browser 
browser.quit()