TRAIN_DATA = [
    (
        "John Doe is the CEO of OpenAI based in San Francisco. Contact him at john.doe@openai.com.",
        {
            "entities": [
                (0, 8, "PERSON"),  # John Doe
                (19, 22, "JOB_TITLE"),  # CEO
                (30, 37, "COMPANY"),  # OpenAI
                (48, 63, "LOCATION"),  # San Francisco
                (76, 97, "CONTACT_INFO")  # john.doe@openai.com
            ]
        }
    ),
    (
        "Jane Smith works as a Senior Engineer at Tesla located in Palo Alto.",
        {
            "entities": [
                (0, 10, "PERSON"),  # Jane Smith
                (22, 38, "JOB_TITLE"),  # Senior Engineer
                (42, 47, "COMPANY"),  # Tesla
                (59, 68, "LOCATION")  # Palo Alto
            ]
        }
    ),
    (
        "Google is hiring for a Software Developer position. Reach out to hiring@google.com.",
        {
            "entities": [
                (0, 6, "COMPANY"),  # Google
                (22, 40, "JOB_TITLE"),  # Software Developer
                (64, 83, "CONTACT_INFO")  # hiring@google.com
            ]
        }
    ),
    (
        "Contact Jim at jim.recruiter@linkedin.com for job opportunities at LinkedIn in Mountain View.",
        {
            "entities": [
                (8, 11, "PERSON"),  # Jim
                (15, 41, "CONTACT_INFO"),  # jim.recruiter@linkedin.com
                (60, 68, "COMPANY"),  # LinkedIn
                (72, 84, "LOCATION")  # Mountain View
            ]
        }
    ),
    (
        "Microsoft is looking for an AI Specialist in Redmond. Get in touch with careers@microsoft.com.",
        {
            "entities": [
                (0, 9, "COMPANY"),  # Microsoft
                (30, 43, "JOB_TITLE"),  # AI Specialist
                (47, 54, "LOCATION"),  # Redmond
                (80, 104, "CONTACT_INFO")  # careers@microsoft.com
            ]
        }
    )
]
