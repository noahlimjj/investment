"""Notification helper for Investment workflow via ntfy.sh.
Sends push notifications to the user's topic (default: 'hallux').
"""
from __future__ import annotations

import urllib.request
import sys

def notify(
    message: str,
    title: str = "Value Investing Update",
    topic: str = "hallux",
    priority: str = "default",
    tags: str = "chart_with_upwards_trend"
) -> bool:
    """Send an instant push notification via ntfy.sh."""
    url = f"https://ntfy.sh/{topic}"
    try:
        req = urllib.request.Request(
            url,
            data=message.encode("utf-8"),
            headers={
                "Title": title,
                "Priority": priority,
                "Tags": tags,
                "User-Agent": "Antigravity-Investment-Bot"
            }
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.status == 200
            if status:
                print(f"[ntfy] Notification sent successfully to https://ntfy.sh/{topic}")
            return status
    except Exception as exc:
        print(f"[ntfy warning] Failed to send notification: {exc}")
        return False

def main():
    msg = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Task completed successfully."
    notify(msg)

if __name__ == "__main__":
    main()
