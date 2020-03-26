
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
5. Submite 

6. go to app and click on RTIR 
7. click on Add-on settings and fill up your RTIR information
8. You can configure proxy setting if it's required. 

> install from CLI 

1. SSH to splunk instance 
2. clone the app from github reposotriy 
3. cp app files to /etc/apps/
4. restart splunk service 
5. repeat GUI setps from 6 to 8 

## How to use

