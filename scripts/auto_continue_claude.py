#!/usr/bin/env python3
"""
Automated scheduler to bring the Investment window & Claude Code tab to the front
at 1:50 AM, and send 'continue' at 2:00 AM (after the session limit resets).
"""

import sys
import os
import time
import datetime
import subprocess
import objc
import Quartz
from Foundation import NSURL, NSDictionary

LOG_FILE = "/Users/User/Desktop/Projects/Investment/scripts/auto_continue_claude.log"
VERIFICATION_IMG = "/Users/User/Desktop/Projects/Investment/scripts/claude_2am_result.png"

def log(msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{now}] {msg}"
    print(formatted, flush=True)
    try:
        with open(LOG_FILE, "a") as f:
            f.write(formatted + "\n")
    except Exception as e:
        print(f"Error writing to log: {e}", flush=True)

def bring_investment_window_front():
    log("Activating Antigravity IDE and raising Investment window...")
    script = '''
    tell application id "com.google.antigravity-ide" to activate
    delay 0.5
    tell application "System Events"
        tell process "Electron"
            set frontmost to true
            set targetWindows to (every window whose name starts with "Investment")
            if (count of targetWindows) > 0 then
                perform action "AXRaise" of first item of targetWindows
            end if
        end tell
    end tell
    '''
    subprocess.run(["osascript", "-e", script], check=True)
    time.sleep(0.5)

def find_tab_and_input():
    capture_path = "/tmp/claude_screen_capture.png"
    subprocess.run(["screencapture", "-x", capture_path], check=True)
    
    Vision = objc.loadBundle('Vision', globals(), bundle_path='/System/Library/Frameworks/Vision.framework')
    VNRecognizeTextRequest = objc.lookUpClass('VNRecognizeTextRequest')
    VNImageRequestHandler = objc.lookUpClass('VNImageRequestHandler')

    url = NSURL.fileURLWithPath_(capture_path)
    req = VNRecognizeTextRequest.alloc().init()
    handler = VNImageRequestHandler.alloc().initWithURL_options_(url, NSDictionary.dictionary())
    handler.performRequests_error_([req], None)

    w, h = 1710, 1107
    tab_pos = None
    input_pos = None

    for obs in req.results():
        candidate = obs.topCandidates_(1)[0]
        text = str(candidate.string()).lower()
        bbox = obs.boundingBox()
        x = bbox.origin.x * w
        y = (1.0 - (bbox.origin.y + bbox.size.height)) * h
        bw = bbox.size.width * w
        bh = bbox.size.height * h
        cx, cy = x + bw / 2, y + bh / 2

        # Check tab bar (y < 130)
        if "value investing multi-ag" in text and y < 130:
            tab_pos = (cx, cy)
            log(f"Detected tab '{candidate.string()}' at {tab_pos}")
        elif "value investing" in text and y < 130 and not tab_pos:
            tab_pos = (cx, cy)

        # Toolbar controls near input box
        if ("0 agents" in text or "opus 5.5" in text) and not input_pos:
            # The text prompt box is slightly above the toolbar row
            input_pos = (cx, cy - 25)
            log(f"Detected input area near '{candidate.string()}' at {input_pos}")

    if not tab_pos:
        tab_pos = (876.0, 100.0)
        log(f"Tab not detected via OCR, using default coordinate: {tab_pos}")
    if not input_pos:
        input_pos = (910.0, 608.0)
        log(f"Input area not detected via OCR, using default coordinate: {input_pos}")

    return tab_pos, input_pos

def mouse_click(x, y):
    pt = Quartz.CGPoint(x=x, y=y)
    evt_down = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseDown, pt, Quartz.kCGMouseButtonLeft)
    evt_up = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseUp, pt, Quartz.kCGMouseButtonLeft)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, evt_down)
    time.sleep(0.05)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, evt_up)
    time.sleep(0.3)

def click_tab_only():
    bring_investment_window_front()
    tab_pos, _ = find_tab_and_input()
    log(f"Clicking Claude Code tab at {tab_pos}...")
    mouse_click(tab_pos[0], tab_pos[1])
    log("Tab clicked successfully and brought to front.")

def send_continue_prompt():
    bring_investment_window_front()
    tab_pos, input_pos = find_tab_and_input()
    
    # 1. Click tab to ensure it's selected
    log(f"Clicking tab at {tab_pos}...")
    mouse_click(tab_pos[0], tab_pos[1])
    time.sleep(0.5)

    # 2. Click inside the chat input box
    log(f"Clicking input area at {input_pos}...")
    mouse_click(input_pos[0], input_pos[1])
    time.sleep(0.5)

    # 3. Use cmd+esc as well to guarantee Claude input focus
    script_focus = '''
    tell application "System Events"
        tell process "Electron"
            key code 53 using {command down}
            delay 0.2
        end tell
    end tell
    '''
    subprocess.run(["osascript", "-e", script_focus], check=True)
    time.sleep(0.3)
    mouse_click(input_pos[0], input_pos[1])
    time.sleep(0.3)

    # 4. Clear any existing text (Cmd+A, Backspace) then type 'continue' and hit Return (key code 36)
    log("Typing 'continue' and pressing Return...")
    script_type = '''
    tell application "System Events"
        tell process "Electron"
            keystroke "a" using {command down}
            delay 0.1
            key code 51
            delay 0.2
            keystroke "continue"
            delay 0.5
            key code 36
        end tell
    end tell
    '''
    subprocess.run(["osascript", "-e", script_type], check=True)
    log("Prompt 'continue' sent.")

    # 5. Wait and capture verification screenshot
    time.sleep(5)
    subprocess.run(["screencapture", "-x", VERIFICATION_IMG], check=True)
    log(f"Saved verification screenshot to {VERIFICATION_IMG}")

def run_scheduler():
    log("=" * 60)
    log("Starting Claude Auto-Continue Scheduler (Target: 7:00 AM Reset)")
    log("Phase 1: Around 06:50 AM -> Bring Investment window to front & click tab")
    log("Phase 2: At 07:00:20 AM -> Type 'continue' and send to Claude Code")
    log("=" * 60)

    # Prevent system sleep using caffeinate
    caffeinate_proc = None
    try:
        caffeinate_proc = subprocess.Popen(["caffeinate", "-dimsu"])
        log(f"Caffeinate background process started (PID: {caffeinate_proc.pid}) to prevent sleep.")
    except Exception as e:
        log(f"Warning: could not start caffeinate: {e}")

    try:
        phase1_done = False
        phase2_done = False

        while True:
            now = datetime.datetime.now()
            # Phase 1: 06:50 AM to 06:59 AM
            if not phase1_done:
                if (now.hour == 6 and now.minute >= 50) or (now.hour == 7 and now.minute == 0 and now.second < 15):
                    log(">>> [PHASE 1 TRIGGERED] 06:50 AM reached. Raising tab to front.")
                    try:
                        click_tab_only()
                    except Exception as e:
                        log(f"Phase 1 error: {e}")
                    phase1_done = True

            # Phase 2: 07:00:20 AM
            if not phase2_done:
                # Trigger at 7:00 AM with a 20-second safety margin to ensure API session reset is active
                if (now.hour == 7 and (now.minute > 0 or now.second >= 20)) or (now.hour > 7):
                    log(">>> [PHASE 2 TRIGGERED] 07:00:20 AM reached. Sending 'continue' to Claude.")
                    try:
                        send_continue_prompt()
                    except Exception as e:
                        log(f"Phase 2 error: {e}")
                    phase2_done = True
                    log("All phases completed successfully! Exiting.")
                    break

            time.sleep(10)
    finally:
        if caffeinate_proc:
            log("Terminating caffeinate process...")
            caffeinate_proc.terminate()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test-tab":
        log("Testing Phase 1 (tab click only)...")
        click_tab_only()
    elif len(sys.argv) > 1 and sys.argv[1] == "--test-continue":
        log("Testing Phase 2 (send continue)...")
        send_continue_prompt()
    else:
        run_scheduler()
