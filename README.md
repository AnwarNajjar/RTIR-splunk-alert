
# RTIR Alert for Splunk Enterprise Security

#### Release Notes
#### Version 1.0.0 March 26 2020
#### RTIR Alert for Splunk Enterprise Security 1.0.

## About RTIR Alert for Splunk Enterprise Security

 RTIR Alert for Splunk Enterprise Security allows Splunk ES users to open a ticket with the IR team  on the [RTIR platform](https://bestpractical.com/rtir) in the ES adaptive response actions, correlation search and saved search. 

Note: The app written in python3 and it's compatible with ES v5.0.1+ and Splunk enterprise v7.0.0+.

## Requirements

- RTIR platfrom 4.2.2+
- Splunk ES v5.0.1+

## Installation

> Install from Splunk  GUI

1. Download Application file from the [link](https://raw.githubusercontent.com/AnwarNajjar/RTIR-splunk-alert/master/TA-rtir-1.0.0.spl?token=ANHCZCHEGONZMKRFDY7UOPS6PSDKK) : 
2. Login to Splunk portal and go to the home page 
3. Click on the app gear

![](https://user-images.githubusercontent.com/55454856/77635554-6ecf2e00-6f5b-11ea-9b2d-ca23fad3573c.png)

4. click install app from file

![](https://user-images.githubusercontent.com/55454856/77635755-b8b81400-6f5b-11ea-9ef2-806ff88cd61b.png)


5. Click on browse to upload the app then click on Upload

![](https://user-images.githubusercontent.com/55454856/77629283-f2841d00-6f51-11ea-990b-43de006fae78.png)

6. Open the RTIR app 

7. click on Add-on settings and fill up your RTIR information.

![](https://user-images.githubusercontent.com/55454856/77627770-0f1f5580-6f50-11ea-96ab-757caeae10b0.png)

8. You can configure proxy setting if it's required. ( optional )
 
![](https://user-images.githubusercontent.com/55454856/77627921-4e4da680-6f50-11ea-9e4a-0f56553f8995.png)



9. After doing the above steps you will find the RITR action appear on ES adaptive response. 

![](https://user-images.githubusercontent.com/55454856/77630722-31b36d80-6f54-11ea-93ea-ea4afac19209.png)


**Note: make sure that RTIR user has the right access to open tickets on RTIR, otherwise the ticket will not be opened.**

> install from CLI 

1. SSH to splunk instance 
2. clone the app from github reposotriy 


```
git clone https://github.com/AnwarNajjar/RTIR-splunk-alert.git
```

3. cp app files to $splunk_home/etc/apps/
```

cp -rp RTIR-splunk-alert /$splunk_home/etc/apps 

```
4. restart splunk service 

```
$splunk_home/bin/splunk restart
```

5. repeat  setps from 6 to 9 in GUI installtion
