import sys
import os
import re
from datetime import datetime

logLine = sys.argv[1]
kbHandle = sys.argv[2]
tradeId = ""
msg = ""

# new trade
match = re.search( "TradeEvents.+We got a new trade", logLine )
if match is not None:
    tail = logLine[ ( re.search( " id=", logLine ) ).end(0): ]
    tradeId = tail[ 0:re.search( '-', tail ).start(0) ]
    msg = "New Trade! ID: {tradeId}".format( tradeId = tradeId )

# deposit confirmed
match = re.search( "Set new state.+DEPOSIT_CONFIRMED_IN_BLOCK_CHAIN", logLine )
if match is not None:
    tail = logLine[ ( re.search( " \(id=", logLine ) ).end(0): ]
    tradeId = tail[ 0:re.search( '\)', tail ).start(0) ]
    msg = "{tradeId}: Deposit tx Confirmed".format( tradeId = tradeId ) # datetime.now()

# buyer has started payment
match = re.search( "Set new state.+SELLER_RECEIVED_FIAT_PAYMENT_INITIATED_MSG", logLine )
if match is not None:
    tail = logLine[ ( re.search( " \(id=", logLine ) ).end(0): ]
    tradeId = tail[ 0:re.search( '\)', tail ).start(0) ]
    msg = "{tradeId}: Buyer Made Payment".format( tradeId = tradeId )

# seller has received payment / trade complete
match = re.search( "Set new state.+BUYER_RECEIVED_PAYOUT_TX_PUBLISHED_MSG", logLine )
if match is not None:
    tail = logLine[ ( re.search( " \(id=", logLine ) ).end(0): ]
    tradeId = tail[ 0:re.search( '\)', tail ).start(0) ]
    msg = "{tradeId}: Trade Complete".format( tradeId = tradeId )

# receive trader chat message
match = re.search( "TraderChatManager.+Received ChatMessage", logLine )
if match is not None:
    tail = logLine[ ( re.search( " with tradeId ", logLine ) ).end(0): ]
    tradeId = tail[ 0:re.search( '-', tail ).start(0) ]
    msg = "{tradeId}: New Message (Trader Chat)".format( tradeId = tradeId )

# mediation opened 
match = re.search( "MediationManager.+Received PeerOpenedDisputeMessage", logLine )
if match is not None:
    tail = logLine[ ( re.search( " with tradeId ", logLine ) ).end(0): ]
    tradeId = tail[ 0:re.search( '-', tail ).start(0) ]
    msg = "{tradeId}: Mediation Opened".format( tradeId = tradeId )

# new mediation message
match = re.search( "MediationManager.+Received ChatMessage", logLine )
if match is not None:
    tail = logLine[ ( re.search( " with tradeId ", logLine ) ).end(0): ]
    tradeId = tail[ 0:re.search( '-', tail ).start(0) ]
    msg = "{tradeId}: New Message (Mediation). Please respond quickly, within 48 hours at most.".format( tradeId = tradeId )

# receive mediation result
match = re.search( "MediationManager.+Received DisputeResultMessage", logLine )
if match is not None:
    tail = logLine[ ( re.search( " with tradeId ", logLine ) ).end(0): ]
    tradeId = tail[ 0:re.search( '-', tail ).start(0) ]
    msg = "{tradeId}: Received Mediation Suggestion. Please accept or reject ASAP.".format( tradeId = tradeId )

# payout from mediation
match = re.search( "Received MediatedPayoutTxPublishedMessage", logLine )
if match is not None:
    tail = logLine[ ( re.search( " with tradeId ", logLine ) ).end(0): ]
    tradeId = tail[ 0:re.search( '-', tail ).start(0) ]
    msg = "{tradeId}: Trade Complete (Mediation Payout Accepted)".format( tradeId = tradeId )

# arbitration opened
match = re.search( "RefundManager.+Received PeerOpenedDisputeMessage", logLine )
if match is not None:
    tail = logLine[ ( re.search( " with tradeId ", logLine ) ).end(0): ]
    tradeId = tail[ 0:re.search( '-', tail ).start(0) ]
    msg = "{tradeId}: Arbitration Opened".format( tradeId = tradeId )

# new arbitration message
match = re.search( "RefundManager.+Received ChatMessage", logLine )
if match is not None:
    tail = logLine[ ( re.search( " with tradeId ", logLine ) ).end(0): ]
    tradeId = tail[ 0:re.search( '-', tail ).start(0) ]
    msg = "{tradeId}: New Message (Arbitration). Please respond quickly, within 48 hours at most.".format( tradeId = tradeId )

# payout from arbitration
match = re.search( "RefundManager.+Received DisputeResultMessage", logLine )
if match is not None:
    tail = logLine[ ( re.search( " with tradeId ", logLine ) ).end(0): ]
    tradeId = tail[ 0:re.search( '-', tail ).start(0) ]
    msg = "{tradeId}: Trade Complete (Arbitration Payout)".format( tradeId = tradeId )

if msg:
    print( "{time} {msg}".format( time = datetime.now(), msg = msg ) )
    os.system( "keybase chat send {kbHandle} \"{msg}\"".format( kbHandle = kbHandle, msg = msg ) )

# exit
sys.exit(0)
