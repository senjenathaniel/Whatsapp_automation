# Time Flagging Messages - Log

## Problem

Basically, we want to flag each downloaded status with a time stamp, that way we can skip the already downloaded messages, and move on to the ones not yet downloaded.

Another problem encountered was that, the browser open the status page from the latest 'read' status. Thus if a user opens their status on their phone, this script will skip the 'read' messages, and thus we need to keep our own log for what messages were 'read' and which weren't by the script, not the user.

## Solution

- **Alternative 1:** Create a log file that keeps the message and it's timestamp, and use this for cheking.

- **Alternative 2:** Put a time stamp on each downloaded file, and use this time stamp to check for unread messages
