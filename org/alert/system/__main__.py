import csv
import os
from collections import defaultdict, Counter
from datetime import datetime

# Configuration
LOG_DIR = 'team_logs'
LOG_FILE = 'application_logs.csv'
SENDER_EMAIL = GMAIL_USER = 'noreply@report.com'
SENDER_NAME = 'App Support Bot'
GMAIL_PASS = 'xxxxxxxxxxxxxxxx'

def parse_logs(file_path):
    """Parse logs and group by ApplicationTeam."""
    team_logs = defaultdict(list)
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                team = row.get('ApplicationTeam')
                level = row.get('LogLevel')
                if not team or not level:
                    raise ValueError("Missing required 'ApplicationTeam' or 'LogLevel' in a log entry.")
                team_logs[team].append(row)
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
    except Exception as e:
        print(f"[ERROR] Failed to read log file: {e}")
    return team_logs

def save_team_logs(team_logs):
    """Save individual team logs into separate CSV files."""
    os.makedirs(LOG_DIR, exist_ok=True)
    for team, logs in team_logs.items():
        file_path = os.path.join(LOG_DIR, f"{team}_logs.csv")
        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=logs[0].keys())
                writer.writeheader()
                writer.writerows(logs)
        except Exception as e:
            print(f"[ERROR] Could not save logs for {team}: {e}")

def generate_summary(team_logs):
    """Generate a count of INFO, WARNING, and ERROR log levels for each team."""
    summaries = {}
    for team, logs in team_logs.items():
        levels = Counter(log.get('LogLevel') for log in logs)
        summaries[team] = {
            'INFO': levels.get('INFO', 0),
            'WARNING': levels.get('WARNING', 0),
            'ERROR': levels.get('ERROR', 0)
        }
    return summaries

def send_email(team, summary, attachment_path):
    """Simulate sending an email by printing the content and attachment info."""
    recipient = f"{team.lower()}@securelife.com"
    date_str = datetime.now().strftime('%Y-%m-%d')
    subject = f'Daily Log Report - {team}'
    body = (
        f"\nHello {team},\n\n"
        f"Please find attached your log report for {date_str}.\n\n"
        f"Summary:\n"
        f"  INFO:    {summary['INFO']}\n"
        f"  WARNING: {summary['WARNING']}\n"
        f"  ERROR:   {summary['ERROR']}\n\n"
        "This is an automated message from the Application Support Team."
    )

    print(f"----- EMAIL TO: {recipient} -----")
    print(f"From   : {SENDER_NAME} <{GMAIL_USER}>")
    print(f"Subject: {subject}")
    print("Body:")
    print(body)

    if os.path.exists(attachment_path):
        size = os.path.getsize(attachment_path)
        print(f"Attachment: {os.path.basename(attachment_path)} ({size} bytes)")
    else:
        print("Attachment file not found.")
    print("--------------------------------------\n")

def main():
    team_logs = parse_logs(LOG_FILE)
    if not team_logs:
        print("[INFO] No logs to process. Exiting.")
        return

    save_team_logs(team_logs)
    summaries = generate_summary(team_logs)

    for team, summary in summaries.items():
        attachment = os.path.join(LOG_DIR, f"{team}_logs.csv")
        send_email(team, summary, attachment)

if __name__ == '__main__':
    main()
