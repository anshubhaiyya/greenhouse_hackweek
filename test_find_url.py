import json
import requests
import os                             # Allows for the clearing of the Terminal Window
import time, datetime
import glob
import getpass

calDescription = '''@Mai, Shadow Mod, observational only 
@Kenny, noted this is not a Austin friendly time but with it being hack week I am trying to keep meetings to the mornings. 

Thanks,
Sinead

Recruiter: Fiona Keating
Hiring Manager:Maeve O'Meara 
MOD: Shake Lahoti

 

Greenhouse Interview Kit (resume + lineup): 
https://dropbox.greenhouse.io/guides/8761116/people/80747142/interview?application_id=93950882




Recruiting Coordinator: Sinead Cronin

***Please ensure that you check into the room before starting your interview - otherwise you risk losing the room booking for the interview***

NOTE: If you believe you should not be interviewing this candidate due to a non-solicit or other reason, please let recruiting team know as soon as possible so they can identify a replacement.
'''


urlIndex = calDescription.find("https://dropbox.greenhouse.io")
print(urlIndex)
equalIndex = calDescription.find("=") + 9
greenhouseUrl = calDescription[urlIndex:equalIndex]
print(greenhouseUrl)
