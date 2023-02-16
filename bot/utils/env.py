import os
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv("GMAIL_PASSWORD1")
EMAIL = "botibha@gmail.com"
PERSONAL = {
        "name": "Albin Anthony",
        "phone": "+91 63790 56811",
        "role": "(Python & Django Developer)"
      }

MESSAGE = """Dear {hr},

Please find my application for the {position} role. I’ve attached, {docs}

I’m excited to apply for the position. I’ve reviewed the job specification and researched your company {company}, and I believe I have the skills, experience, and approach to perform in the role.

You can find details of my qualifications and achievements in my CV. If you have any questions, please get in touch with me at {email} or {phone}.

Please provide me with details on the next steps in the process.

Best Regards,
{name}
{role}

Attatchments:
{docs}

Email: {email}
Phone: {phone}

"""

