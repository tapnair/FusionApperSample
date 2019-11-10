import adsk.core
import adsk.fusion
import traceback

import json
import time

from ..apper import apper


class SampleWorkspaceEvent1(apper.Fusion360WorkspaceEvent):

    def workspace_event_received(self, event_args, workspace):
        app = adsk.core.Application.cast(adsk.core.Application.get())
        msg = "You just ACTIVATED a workspace called: {} ".format(workspace.name)
        # msg = "You just opened a document"
        app.userInterface.messageBox(msg)

