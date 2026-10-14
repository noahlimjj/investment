#!/usr/bin/env bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

# Stop any earlier poller for this project: older versions held no lock, so two could run at
# once and split your Telegram messages between them.
for pid in $(pgrep -f "telegram_(app|bridge)\.py"); do
  cwd=$(lsof -a -p "$pid" -d cwd -Fn 2>/dev/null | sed -n 's/^n//p')
  if [ "$cwd" = "$DIR" ]; then
    echo "Stopping earlier poller (pid $pid)"
    kill "$pid" 2>/dev/null || true
  fi
done
sleep 1

echo "================================================================================"
echo "VALUE PIPELINE TELEGRAM BRIDGE"
echo "Same commands as the app; free-form chat goes to the Antigravity agent, which"
echo "cannot issue verdicts. /analyse runs on Gemini in Antigravity, so start this from"
echo "the Antigravity agent (it needs Antigravity's session). Replaces any running bot."
echo "================================================================================"

python3 telegram_bridge.py
