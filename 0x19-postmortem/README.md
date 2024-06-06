By Marouane Fatih:
Earlier this week we experienced an error in the WordPress server, and today 
we providing an incident report that details the nature of the server error and our response.
The following is the incident report for the WordPress server error that occurred on
June 5, 2024. We understand this service issue has impacted our valued users,
And we apologize to everyone who was affected.
Issue Summary
From 04:17 PM to 4:59 PM GMT+1, Users were receiving a server response with error code 500, preventing access to the website. At its peak, the issue affected 100% of response to the users.


Timeline (all times in GMT+1 Time):
•	04:17 GMT+1: Configuration push begins
•	04:19 GMT+1: server error begins 
•	04:20 GMT+1: Datadog alerted me 
•	04:55 GMT+1: Successful configuration change rollback
•	04:55 GMT+1: server restart begins
•	04:59 GMT+1: server respond with code 200

Root Cause
A typo in the PHP configuration file led to the outage; "php" was entered as "pphp." Because of this error, the configuration file—more especially, the incorrect "pphp" directive—was not recognized by the server. The server as a whole suffered as a result, responding to requests with error code 500 every time. The server problem started right away, completely interrupting WordPress's functions. The server's prompt response revealed that the incorrect configuration was preventing it from properly processing any requests, making the website unavailable to all users. Until the misspelling was found and fixed, the error remained.

Resolution and recovery


At 04:20 GMT+1, the monitoring system alerted me, and I quickly acted to resolve the problem. By 04:50 PM GMT+1, I managed to figure the cause of the problem.

At 04:55 GMT+1, I attempted to rollback the problematic configuration change, I went to the WordPress php file, and I fix the misspelling.

After restarting the server at 04:59 GMT+1, it worked at its 100% of efficiency and the server successfully responding with code 200.



Corrective and Preventative Measures


In the last two days, we've conducted an internal review and analysis of the server error. The following are actions we are taking to address the underlying causes of the issue and to help prevent recurrence and improve response times

Disable the current configuration release mechanism until safer measures are implemented. (Completed.)

Change rollback process to be quicker and more robust

Fix the underlying authentication libraries and monitoring to correctly timeout/interrupt on errors.

Improve process for auditing all high-risk configuration options.

Add a faster rollback mechanism, so any future problems of this type can be corrected quickly.

Develop better mechanism for quickly delivering status notifications during incidents.

we committed to continually and quickly improving our technology and operational processes to prevent errors. We appreciate your patience and again apologize for the impact to you, your users, and your organization. We thank you for your business and continued support.

