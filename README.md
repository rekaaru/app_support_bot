🛠️ Application Log Processor
This Python script automates the process of parsing, categorizing, summarizing, and reporting application logs by team. It reads logs from a centralized CSV file, generates per-team reports, and simulates email dispatch with log summaries and attachments.

📁 Project Structure
graphql
Copy
Edit
.
├── application_logs.csv     # Main input CSV file containing logs
├── team_logs/               # Auto-generated folder containing per-team log files
├── log_reporter.py          # Main Python script
└── README.md                # Project documentation
🚀 Features
Parses a CSV file of application logs

Groups logs by ApplicationTeam

Saves individual CSV reports for each team

Summarizes log levels: INFO, WARNING, ERROR

Simulates email dispatch (prints to console)

📄 CSV Format
The input CSV file (application_logs.csv) should have the following headers:

csv
Copy
Edit
Timestamp,ApplicationTeam,LogLevel,Message
2025-05-13 08:55:01,Payments,INFO,Initialized payment gateway
...
⚙️ Configuration
Update the following variables in the script if needed:

python
Copy
Edit
LOG_FILE = 'application_logs.csv'     # Input log file
LOG_DIR = 'team_logs'                 # Directory to save team logs
GMAIL_USER = 'noreply@report.com'     # Simulated sender email
SENDER_NAME = 'App Support Bot'       # Sender name
GMAIL_PASS = 'xxxxxxxxxxxxxxxx'       # [Should be moved to environment variable]
For real email sending, integrate an email service (e.g. smtplib) and use secure credential management (e.g., environment variables).

📦 How to Run
Ensure Python 3.6+ is installed.

Place your log file as application_logs.csv in the project directory.

Run the script:

bash
Copy
Edit
python log_reporter.py
Outputs will appear:

Team-specific logs in the team_logs/ directory

Email simulations printed in the terminal

🔐 Security Note
Avoid hardcoding passwords or sensitive credentials directly in the script. Instead, use environment variables:

python
Copy
Edit
import os
GMAIL_PASS = os.getenv('GMAIL_PASS')
Set it in your environment:

bash
Copy
Edit
export GMAIL_PASS='your-secure-password'
🧪 Sample Output
yaml
Copy
Edit
----- EMAIL TO: payments@securelife.com -----
From   : App Support Bot <noreply@report.com>
Subject: Daily Log Report - Payments
Body:

Hello Payments,

Please find attached your log report for 2025-05-14.

Summary:
INFO:    12
WARNING: 2
ERROR:   1

This is an automated message from the Application Support Team.
Attachment: Payments_logs.csv (1453 bytes)
--------------------------------------
📬 Future Enhancements
Integrate real email sending (e.g. with Gmail SMTP)

Schedule as a daily cron job

Add support for other formats (e.g. JSON input/output)

Include log severity thresholds for alerts

👩‍💻 Author
Application Support Bot
Email: rekauni171@gmail.com