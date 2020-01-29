# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Copyright (c) 2020 by Patrick Rainsberry.                                   ~
#  :license: Apache2, see LICENSE for more details.                            ~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  SampleCommandEvents.py                                                      ~
#  This file is a component of ApperSample.                                    ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import apper


class SampleCommandEvent(apper.Fusion360CommandEvent):

    def command_event_received(self, event_args, command_id, command_definition):
        ao = apper.AppObjects()
        msg = "You just started the {} command with id: {} ".format(command_definition.name, command_id)
        ao.ui.messageBox(msg)
