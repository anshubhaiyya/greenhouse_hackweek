import json
import requests
import os                             # Allows for the clearing of the Terminal Window
import time, datetime
import glob
import getpass

###  Defining Paper Token
papertoken = ""
calDescription = input_data["caldesc"]


###  folder input not needed for Zapier
###print('Lastly, input the folder URL here (or type "none" to skip this): ')
###paperFolder = raw_input()

### Getting the calDescription variable from Zapier and getting the URL out of it
urlIndex = calDescription.find("https://dropbox.greenhouse.io")
equalIndex = calDescription.find("=") + 9
greenhouseURL = calDescription[urlIndex:equalIndex]

###  Breaking down the inputted URLs by the user, for the candidate ID, application ID and Paper Folder ID
URLending = greenhouseURL.split("/people/")[-1]
candidateID = int(URLending.split("/")[0])
applicationID = int(URLending.split("=")[-1])
###  Breaking down the inputted URLs by the user, for the candidate ID, application ID and Paper Folder ID

###  Will need to replace these with real API calls when Greenhouse API is available
fakeCandresp = '''
{
    "id": 80747142,
    "first_name": "John",
    "last_name": "Locke",
    "company": "The Tustin Box Company",
    "title": "Man of Mystery",
    "created_at": "2017-08-15T03:31:46.591Z",
    "updated_at": "2017-09-28T12:29:30.497Z",
    "last_activity": "2017-09-28T12:29:30.481Z",
    "is_private": false,
    "photo_url": "https://prod-heroku.s3.amazonaws.com/people/photos/053/883/394/original/corgi.jpg?AWSAccessKeyId=AKIAIK36UTOKQ5F2YNMQ&Expires=1509193807&Signature=cg%2BhyNTvvNgTTzWtsMJJZvPRYH4%3D",
    "attachments": [
        {
            "filename": "John_Locke_Offer_Packet_09_27_2017.pdf",
            "url": "https://prod-heroku.s3.amazonaws.com/person_attachments/data/077/683/131/original/John_Locke_Offer_Packet_09_27_2017.pdf?AWSAccessKeyId=AKIAIK36UTOKQ5F2YNMQ&Expires=1509193807&Signature=R5TbJPzD7TO5NgX8K8Y0yogPstY%3D",
            "type": "offer_packet"
        }
    ],
    "application_ids": [
        93950882,
        65153308
    ],
    "phone_numbers": [
        {
            "value": "555-555-5555",
            "type": "mobile"
        }
    ],
    "addresses": [
        {
            "value": "123 City Street\nNew York, Ny 10001",
            "type": "home"
        }
    ],
    "email_addresses": [
        {
            "value": "test@work.com",
            "type": "work"
        },
        {
            "value": "test@example.com",
            "type": "personal"
        }
    ],
    "website_addresses": [
        {
            "value": "mysite.com",
            "type": "personal"
        }
    ],
    "social_media_addresses": [
        {
            "value": "twitter.com/test"
        }
    ],
    "recruiter": {
        "id": 92120,
        "first_name": "Greenhouse",
        "last_name": "Admin",
        "name": "Greenhouse Admin",
        "employee_id": "67890"
        },
    "coordinator": {
        "id": 453636,
        "first_name": "Jane",
        "last_name": "Smith",
        "name": "Jane Smith",
        "employee_id": "12345"
    },
    "tags": [
        "Python",
        "Ruby"
    ],
    "applications": [
        {
            "id": 93950882,
            "candidate_id": 53883394,
            "prospect": false,
            "applied_at": "2017-09-27T12:03:02.728Z",
            "rejected_at": "2017-09-27T12:11:40.877Z",
            "last_activity_at": "2017-09-28T12:29:30.481Z",
            "location": { 
                "address": "New York, New York, USA" 
            },
            "source": {
                "id": 16,
                "public_name": "LinkedIn (Prospecting)"
            },
            "credited_to": {
                "id": 165372,
                "first_name": "Joel",
                "last_name": "Job Admin",
                "name": "Joel Job Admin",
                "employee_id": null
            },
            "rejection_reason": {
                "id": 9504,
                "name": "Hired another candidate",
                "type": {
                    "id": 1,
                    "name": "We rejected them"
                }
            },
            "rejection_details": {
                "custom_fields": {
                    "custom_rejection_question_field": null
                },
                "keyed_custom_fields": {
                    "custom_rejection_question_field": {
                        "name": "Custom Rejection Question Field",
                        "type": "short_text",
                        "value": null
                    }
                }
            },
            "jobs": [
                {
                    "id": 149995,
                    "name": "DevOps Engineer"
                }
            ],
            "status": "rejected",
            "current_stage": {
                "id": 1073533,
                "name": "Take Home Test"
            },
            "answers": [
                {
                    "question": "How did you hear about this job?",
                    "answer": "A friend"
                },
                {
                    "question": "Website",
                    "answer": "https://example.com"
                },
                {
                    "question": "LinkedIn Profile",
                    "answer": "https://linkedin.com/example"
                }
            ],
            "prospect_detail": {
                "prospect_pool": null,
                "prospect_stage": null,
                "prospect_owner": null
            }
        },
        {
            "id": 65153308,
            "candidate_id": 53883394,
            "prospect": false,
            "applied_at": "2017-08-15T03:31:46.637Z",
            "rejected_at": null,
            "last_activity_at": "2017-09-28T12:29:30.481Z",
            "location": {
                "address": "New York, New York, United States"
            },
            "source": {
                "id": 12,
                "public_name": "Meetups"
            },
            "credited_to": {
                "id": 566819,
                "first_name": "Bob",
                "last_name": "Smith",
                "name": "Bob Smith",
                "employee_id": null
            },
            "rejection_reason": null,
            "rejection_details": null,
            "jobs": [
                {
                    "id": 299100,
                    "name": "Data Scientist - BK"
                }
            ],
            "status": "active",
            "current_stage": {
                "id": 2966800,
                "name": "Face to Face"
            },
            "answers": [],
            "prospect_detail": {
                "prospect_pool": null,
                "prospect_stage": null,
                "prospect_owner": null
            }
        }
    ],
    "educations": [
        {
            "id": 561227,
            "school_name": "University of Michigan - Ann Arbor",
            "degree": "Bachelor's Degree",
            "discipline": "Computer Science",
            "start_date": "2012-08-15T00:00:00.000Z",
            "end_date": "2016-05-15T00:00:00.000Z"
        }
    ],
    "employments": [
        {
            "id": 8485064,
            "company_name": "Greenhouse",
            "title": "Engineer",
            "start_date": "2012-08-15T00:00:00.000Z",
            "end_date": "2016-05-15T00:00:00.000Z"
        }
    ],
    "custom_fields": {
        "desired_salary": "1000000000",
        "work_remotely": true,
        "graduation_year": "2018"
    },
    "keyed_custom_fields": {
        "desired_salary": {
            "name": "Desired Salary",
            "type": "short_text",
            "value": "1000000000"
        },
        "work_remotely": {
            "name": "Work Remotely",
            "type": "boolean",
            "value": true
        },
        "graduation_year_1": {
            "name": "Graduation Year",
            "type": "single_select",
            "value": "2018"
        }
    }
}'''
fakeScoreresp = '''
[
  {
    "id": 211231,
    "updated_at": "2016-08-22T19:52:38.384Z",
    "created_at": "2016-08-22T19:52:38.384Z",
    "interview": "Application Review",
    "candidate_id": 80747142,
    "application_id": 93950882,
    "interviewed_at": "2016-08-18T16:00:00.000Z",
    "submitted_by": {
      "id": 4080,
      "first_name": "Kate",
      "last_name": "Austen",
      "name": "Kate Austen",
      "employee_id": "12345"
    },
    "submitted_at": "2014-03-26T21:59:51Z",
    "overall_recommendation": "yes",
    "attributes": [
      {
        "name": "Communication",
        "type": "Skills",
        "note": "What a great communicator!",
        "rating": "yes"
      },
      {
        "name": "Adaptable",
        "type": "Skills",
        "note": null,
        "rating": "yes"
      },
      {
        "name": "Relationship Manager",
        "type": "Skills",
        "note": null,
        "rating": "mixed"
      },
      {
        "name": "Project Management",
        "type": "Qualifications",
        "note": null,
        "rating": "mixed"
      },
      {
        "name": "Problem Solver",
        "type": "Qualifications",
        "note": null,
        "rating": "no"
      },
      {
        "name": "Analytical",
        "type": "Skills",
        "note": null,
        "rating": "definitely_not"
      }
    ],
    "ratings": {
      "definitely_not": [
        "Analytical"
      ],
      "no": [
        "Problem Solver"
      ],
      "mixed": [
        "Relationship Manager",
        "Project Management"
      ],
      "yes": [
        "Communication",
        "Adaptable"
      ],
      "strong_yes": []
    },
    "questions": [
      {
        "id": null,
        "question": "Key Take-Aways",
        "answer": "Seems like a decent candidate."
      },
      {
        "id": null,
        "question": "Private Notes",
        "answer": "Seems like a decent candidate."
      },
      {
        "id": 1234567,
        "question": "Does the candidate have experience designing APIs?",
        "answer": "Yes"
      },
      {
        "id": 1234568,
        "question": "Which team would you suggest for this candidate?",
        "answer": "Alpha Team"
      },
      {
        "id": 1234569,
        "question": "Where would the candidate be willing to work?",
        "answer": "London, Dubai, San Diego"
      }
    ]
  },
  {
    "id": 3414169,
    "updated_at": "2016-01-08T19:07:08.295Z",
    "created_at": "2016-01-08T19:07:08.295Z",
    "interview": "Behavioral Phone Interview",
    "candidate_id": 14271904,
    "application_id": 23558552,
    "interviewed_at": "2016-01-08T17:00:00.000Z",
    "submitted_by": {
        "id": 158104,
        "first_name": "Jane",
        "last_name": "Doe",
        "name": "Dane Doe",
        "employee_id": "034509364"
    },
    "submitted_at": "2016-01-08T19:07:08.295Z",
    "overall_recommendation": "no",
    "attributes": [
      {
        "name": "Communication",
        "type": "Skills",
        "note": "What a great communicator!",
        "rating": "yes"
      },
      {
        "name": "Adaptable",
        "type": "Skills",
        "note": null,
        "rating": "yes"
      },
      {
        "name": "Relationship Manager",
        "type": "Skills",
        "note": null,
        "rating": "mixed"
      },
      {
        "name": "Project Management",
        "type": "Qualifications",
        "note": null,
        "rating": "mixed"
      },
      {
        "name": "Problem Solver",
        "type": "Qualifications",
        "note": null,
        "rating": "no"
      },
      {
        "name": "Analytical",
        "type": "Skills",
        "note": null,
        "rating": "definitely_not"
      }
    ],
    "ratings": {
      "definitely_not": [
        "Analytical"
      ],
      "no": [
        "Problem Solver"
      ],
      "mixed": [
        "Relationship Manager",
        "Project Management"
      ],
      "yes": [
        "Communication",
        "Adaptable"
      ],
      "strong_yes": []
    },
    "questions": [
      {
        "id": null,
        "question": "Key Take-Aways",
        "answer": "Seems like a decent candidate."
      },
      {
        "id": null,
        "question": "Private Notes",
        "answer": "Seems like a decent candidate."
      },
      {
        "id": 1234567,
        "question": "Does the candidate have experience designing APIs?",
        "answer": "Yes"
      },
      {
        "id": 1234568,
        "question": "Which team would you suggest for this candidate?",
        "answer": "Alpha Team"
      },
      {
        "id": 1234569,
        "question": "Where would the candidate be willing to work?",
        "answer": "London, Dubai, San Diego"
      }
    ]     
  }
]
'''
###  Will need to replace these with real API calls when Greenhouse API is available


###  Defining the Paper Doc's base variables for formatting in HTML
title = ""
references = '<a href="'+ greenhouseURL + '">Greenhouse Profile</a><br>'
decisionTable = '<h1>Feedback</h1><br><table><tr><td><b>Interviewer</b></td><td><b>Decision</b></td><td><b>Focus</b></td></tr>'
feedback = "<h2>Greenhouse Feedback</h2><br>";
###  Defining the Paper Doc's base variables for formatting in HTML



###  Making the Candidate Info and Scorecard into workdable dictionaries in Python
CandidateInfo = json.loads(fakeCandresp, strict=False)
Scorecard = json.loads(fakeScoreresp, strict=False)
###  Making the Candidate Info and Scorecard into workdable dictionaries in Python


###  Building the Doc Title using the Candidate API response
title = CandidateInfo["first_name"] + " " + CandidateInfo["last_name"] + " - " 
for i in CandidateInfo["applications"]:
    if int(i["id"]) == applicationID:
        currentApp = i["jobs"][0]
        title = title + str(currentApp["name"]) + " - "+ datetime.datetime.now().strftime("%d/%B/%Y")+ "<br>"
###  Building the Doc Title


##  Simultaneously building the decision table and feedback body using the Scorecard API response
for j in Scorecard:
    decisionTable = decisionTable + "<tr><td>" + j["submitted_by"]["name"] + "</td><td>" + j["overall_recommendation"] + "</td><td>" + j["interview"] + "</td></tr>"
    feedback = feedback + "<b>" + j["submitted_by"]["name"] + "</b><br><b>" + j["overall_recommendation"] + "</b><br>"
    for k in j["questions"]:
        feedback = feedback + "<u>" + k["question"] + "</u><br>" + k["answer"] + "<br>"
    for l in j["attributes"]:
        feedback = feedback + "<u>" + l["name"] + "</u><br>" + str(l["note"]) + "<br>"
    feedback = feedback + "<br>"
decisionTable = decisionTable + "</table><br>"
###  Simultaneously building the decision table and feedback body using the Scorecard API response

###  Building one total doc variable for cleanliness
totaldoc = title+decisionTable+feedback


###  Define the API Arguments
apiArgs = json.dumps({"import_format": "html"})

###  Define the API headers and URL
apiHeaders = {'Content-Type': 'application/octet-stream',
		'Authorization': 'Bearer %s' % papertoken, 
		'Dropbox-API-Arg': '%s' % apiArgs}
apiUrl = "https://api.dropboxapi.com/2/paper/docs/create"
###  Define the API headers and URL

###  Call the API to create the Paper Doc
apiResult = requests.post(apiUrl, headers=apiHeaders, data = totaldoc)
###  Call the API