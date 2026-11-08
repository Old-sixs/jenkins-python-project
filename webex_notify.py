
import os
import sys
import json
import urllib.request
import urllib.error

def send_notification(status):
    token = os.environ["WEBEX_TOKEN"]
    room_id = os.environ["WEBEX_ROOM_ID"]
    job_name = os.environ.get("JOB_NAME", "Python-GitHub-Pipeline")
    build_number = os.environ.get("BUILD_NUMBER", "Unknown")
    build_url = os.environ.get("BUILD_URL", "")

    message = (
        f"Jenkins Build: {status}\n"
        f"Job: {job_name}\n"
        f"Build Number: {build_number}\n"
        f"Python Unit Tests: "
        f"{'PASSED' if status == 'SUCCESS' else 'FAILED'}\n"
        f"Build URL: {build_url}"
    )

    data = json.dumps({
        "roomId": room_id,
        "text": message
    }).encode("utf-8")

    request = urllib.request.Request(
        "https://webexapis.com/v1/messages",
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            print(f"WebEx notification sent! HTTP {response.status}")
    except urllib.error.HTTPError as error:
        print(f"WebEx API error: HTTP {error.code}")
        sys.exit(1)
    except urllib.error.URLError as error:
        print(f"WebEx connection failed: {error.reason}")
        sys.exit(1)

if __name__ == "__main__":
    send_notification(sys.argv[1])
