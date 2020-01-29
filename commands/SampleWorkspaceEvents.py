# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  Copyright (c) 2020 by Patrick Rainsberry.                                   ~
#  :license: Apache2, see LICENSE for more details.                            ~
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  SampleWorkspaceEvents.py                                                    ~
#  This file is a component of ApperSample.                                    ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import adsk.core
import adsk.fusion
import traceback

import apper


class SampleWorkspaceEvent1(apper.Fusion360WorkspaceEvent):

    def workspace_event_received(self, event_args, workspace):
        app = adsk.core.Application.cast(adsk.core.Application.get())
        msg = "You just ACTIVATED a workspace called: {} ".format(workspace.name)
        app.userInterface.messageBox(msg)

