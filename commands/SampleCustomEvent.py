# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Copyright (c) 2020 by Patrick Rainsberry.                                   ~
#  :license: Apache2, see LICENSE for more details.                            ~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  SampleCustomEvent.py                                                        ~
#  This file is a component of ApperSample.                                    ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import json
import time

import apper


class SampleCustomEvent1(apper.Fusion360CustomThread):

    def custom_event_received(self, event_dict):
        ao = apper.AppObjects()
        ao.ui.messageBox(str(event_dict))

    def run_in_thread(self, thread, event_id, input_data=None):
        ao = apper.AppObjects()
        ao.ui.messageBox("test")
        # Every five seconds fire a custom event, passing a random number.
        for i in range(3):
            message = {
                "text": "Hello World!",
                "index": str(i),
                "event_id": event_id
            }
            time.sleep(3)
            ao.app.fireCustomEvent(event_id, json.dumps(message))

