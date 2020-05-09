
# encoding = utf-8
from rtkit.resource import RTResource
from rtkit.authenticators import CookieAuthenticator
from rtkit.errors import RTResourceError
from rtkit import set_logging
import logging
import time
import json
import requests
import os
import solnlib.splunkenv

# Splunk parameter

def process_event(helper, *args, **kwargs):
    
    ## Setup 
    
    rtir_ip = helper.get_global_setting('rtir_ip')
    

    username = helper.get_global_setting("username")
    
    password = helper.get_global_setting("password")
        
    splunk_ip = helper.get_global_setting("splunk_ip")
        
    ## User input
        
    title = helper.get_param("title")
        
    queue_number = helper.get_param("queue_number")
        
    message = helper.get_param("message")
        
    sla = helper.get_param("sla")
    
    owner = helper.get_param("owner")
        
    req_email = helper.get_param("req_email")
        
    cc_email = helper.get_param("cc_email")
        
    admin_cc_email = helper.get_param("admin_cc_email")
        
        
        
    ## notable input 
        
    action =  helper.get_param("action")
        
    event_id = helper.get_param("event_id")
        
    urgency  = helper.get_param("urgency")

    
    def get_content () :
    
        spk_url = "https://{}:8000/en-GB/app/search/search?q=search%20%60notable%60%20%7C%20search%20event_id%3D".format(splunk_ip) +str(event_id)
        
        es_url = "https://{}:8000/en-GB/app/SplunkEnterpriseSecuritySuite/incident_review".format(splunk_ip)
        
        body =" \
        -------------------------------------------- \
        \n***** Notable details ***** \
        \nEvent ID : {0} \
        \nRule Title: {1} \
        \nUrgency: {2} \
        \nAction: {3} \
        \nNotable Url: {4} \
        \nSplunk ES Url: {5} \
        \n -------------------------------------------- \
        \n User Additional information \
        \n \
        \n {6}".format(str(event_id),str(title),str(urgency),str(action),str(spk_url) , str(es_url) ,str(message) )
        
       
        return body
    
    

    def create_ticket(*args):
        
        url = "https://{0}/REST/1.0/".format(str(rtir_ip))
        resource = RTResource( url , username , password , CookieAuthenticator)
        
        ttime = time.strftime("%T").split(":")[0]
        
        raw_data = get_content()

        content = {
            'content': {
                'Queue': queue_number,
                'Subject': title,
                'Text': raw_data,
                'status': 'open',
                'Owner': owner,
                "Sla" : urgency ,
                "Requestor" : req_email,
                "Cc": cc_email ,
                "AdminCc" : admin_cc_email
            }
        }  
        
        print(dir(content))
        print(content)  
        try:
            response = resource.post(path='ticket/new', payload=content,)
            
        except RTResourceError as e :
            
            logger.error(e.response.status_int)
            logger.error(e.response.status)
            logger.error(e.response.parsed)
    
    

    create_ticket()

    """
    # IMPORTANT
    # Do not remove the anchor macro:start and macro:end lines.
    # These lines are used to generate sample code. If they are
    # removed, the sample code will not be updated when configurations
    # are updated.

    [sample_code_macro:start]

    # The following example sends rest requests to some endpoint
    # response is a response object in python requests library
    response = helper.send_http_request("http://www.splunk.com", "GET", parameters=None,
                                        payload=None, headers=None, cookies=None, verify=True, cert=None, timeout=None, use_proxy=True)
    # get the response headers
    r_headers = response.headers
    # get the response body as text
    r_text = response.text
    # get response body as json. If the body text is not a json string, raise a ValueError
    r_json = response.json()
    # get response cookies
    r_cookies = response.cookies
    # get redirect history
    historical_responses = response.history
    # get response status code
    r_status = response.status_code
    # check the response status, if the status is not sucessful, raise requests.HTTPError
    response.raise_for_status()


    # The following example gets the setup parameters and prints them to the log
    rtir_ip = helper.get_global_setting("rtir_ip")
    helper.log_info("rtir_ip={}".format(rtir_ip))
    username = helper.get_global_setting("username")
    helper.log_info("username={}".format(username))
    password = helper.get_global_setting("password")
    helper.log_info("password={}".format(password))
    splunk_ip = helper.get_global_setting("splunk_ip")
    helper.log_info("splunk_ip={}".format(splunk_ip))

    # The following example gets the alert action parameters and prints them to the log
    queue_number = helper.get_param("queue_number")
    helper.log_info("queue_number={}".format(queue_number))

    title = helper.get_param("title")
    helper.log_info("title={}".format(title))

    owner = helper.get_param("owner")
    helper.log_info("owner={}".format(owner))

    sla = helper.get_param("sla")
    helper.log_info("sla={}".format(sla))

    message = helper.get_param("message")
    helper.log_info("message={}".format(message))

    req_email = helper.get_param("req_email")
    helper.log_info("req_email={}".format(req_email))

    cc_email = helper.get_param("cc_email")
    helper.log_info("cc_email={}".format(cc_email))

    admin_cc_email = helper.get_param("admin_cc_email")
    helper.log_info("admin_cc_email={}".format(admin_cc_email))

    urgency = helper.get_param("urgency")
    helper.log_info("urgency={}".format(urgency))

    event_id = helper.get_param("event_id")
    helper.log_info("event_id={}".format(event_id))

    action = helper.get_param("action")
    helper.log_info("action={}".format(action))


    # The following example adds two sample events ("hello", "world")
    # and writes them to Splunk
    # NOTE: Call helper.writeevents() only once after all events
    # have been added
    helper.addevent("hello", sourcetype="sample_sourcetype")
    helper.addevent("world", sourcetype="sample_sourcetype")
    helper.writeevents(index="summary", host="localhost", source="localhost")

    # The following example gets the events that trigger the alert
    events = helper.get_events()
    for event in events:
        helper.log_info("event={}".format(event))

    # helper.settings is a dict that includes environment configuration
    # Example usage: helper.settings["server_uri"]
    helper.log_info("server_uri={}".format(helper.settings["server_uri"]))
    [sample_code_macro:end]
    """

    helper.log_info("Alert action rtir started.")

    # TODO: Implement your alert action logic here
    return 0
