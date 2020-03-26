Welcome file
Welcome file

# RTIR Alert for Splunk Enterprise Security

#### Release Notes

##### Version 1.0.0 March 26 2020
##### RTIR Alert for Splunk Enterprise Security 1.0.0

## About RTIR Alert for Splunk Enterprise Security

The RTIR Alert for Splunk Enterprise Security allow Splunk ES users to open a ticket with IR team on [RTIR platform](https://bestpractical.com/rtir) within the ES adaptive respone actions ,correlation search and saved search. 

Note: The app written in python3 and it's compatible with ES v5.0.1+ and splunk enterprise v7.0.0+. 

## Requirements

- RTIR platfrom 4.2.2+
- Splunk ES v5.0.1+

## Installation

> Install from Splunk  GUI

1. Download App from Splunkbase website : 
2. Login to Splunk portal and go to the home page 
3. Click on the app gear and click on mange app 
4. click install app from file
5. Click on browse to upload the app then click on Upload

![Selection_011](https://user-images.githubusercontent.com/55454856/77629283-f2841d00-6f51-11ea-990b-43de006fae78.png)

8. go to apps and open the RTIR app 

9. click on Add-on settings and fill up your RTIR information.

![](https://user-images.githubusercontent.com/55454856/77627770-0f1f5580-6f50-11ea-96ab-757caeae10b0.png)

9. You can configure proxy setting if it's required. ( optional )
 
![](https://user-images.githubusercontent.com/55454856/77627921-4e4da680-6f50-11ea-9e4a-0f56553f8995.png)


> install from CLI 

1. SSH to splunk instance 
2. clone the app from github reposotriy 

git clone 

3. cp app files to /etc/apps/

cp -rp /$splunk_home/etc/apps 

4. restart splunk service 

$splunkhome/bin/splunk restart

5. repeat  setps from 6 to 9 in GUI installtion

After doing the above steps you will find the RITR action appear on ES adaptive response and ES notable action. 

** Note: make sure that RTIR user have the right access to open ticket on RTIR, otherwise the ticket will not opened. ** 







RTIR Alert for Splunk Enterprise Security
Release Notes
Version 1.0.0 March 26 2020
RTIR Alert for Splunk Enterprise Security 1.0.0
About RTIR Alert for Splunk Enterprise Security
The RTIR Alert for Splunk Enterprise Security allow Splunk ES users to open a ticket with IR team on RTIR platform within the ES adaptive respone actions ,correlation search and saved search.

Note: The app written in python3 and it’s compatible with ES v5.0.1+ and splunk enterprise v7.0.0+.

Requirements
RTIR platfrom 4.2.2+
Splunk ES v5.0.1+
Installation
Install from Splunk GUI

Download App from Splunkbase website :
Login to Splunk portal and go to the home page
Click on the app gear and click on mange app
click install app from file
Click on browse to upload the app then click on Upload
Selection_011

go to apps and open the RTIR app

click on Add-on settings and fill up your RTIR information.



You can configure proxy setting if it’s required. ( optional )


install from CLI

SSH to splunk instance
clone the app from github reposotriy
git clone

cp app files to /etc/apps/
cp -rp /$splunk_home/etc/apps

restart splunk service
$splunkhome/bin/splunk restart

repeat setps from 6 to 9 in GUI installtion
After doing the above steps you will find the RITR action appear on ES adaptive response and ES notable action.

** Note: make sure that RTIR user have the right access to open ticket on RTIR, otherwise the ticket will not opened. **

Markdown 1898 bytes 265 words 69 lines Ln 63, Col 0HTML 1168 characters 238 words 31 paragraphs
