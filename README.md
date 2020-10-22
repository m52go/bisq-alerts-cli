# bisq-alerts-cli

Leave this script running while Bisq is running and it will alert you of trade events: new trades, deposit tx confirmation, peer sending money, chat messages (from trading peers, mediators, and arbitrators), dispute resolution events, and payouts / trade completions.

This script was inspired by inpharmaticist's [MintSigGraph](https://github.com/inpharmaticist/MintSigGraph).

## Requirements

- Python 3
- jq

## Instructions

Fill in Bisq log file path and Keybase handle in `settings.json`. See this article for default locations across operating systems:
https://bisq.wiki/Data_directory#Default_locations

Make sure Bisq is running.

Then run `monitor.sh`.

You should get alerts on your Keybase app every time there is an action with one of your Bisq trades.

## Notes

This script is currently only configured to send notifications via Keybase.

You may want to use another messaging tool like Signal (perhaps via `signal-cli`) or Matrix. PRs are welcome.
