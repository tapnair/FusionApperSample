import adsk.core
import adsk.fusion
import traceback

import json
import time

from ..apper.Fusion360AppEvents import Fusion360DocumentEvent


class SampleDocumentEvent1(Fusion360DocumentEvent):
    # def __init__(self, event_id, event_type):
    #     ao = AppObjects()
    #     ao.ui.messageBox("test")
    #     try:
    #         super().__init__(event_id, event_type)
    #     except:
    #         ao.ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

    def document_event_received(self, event_args, document):
        app = adsk.core.Application.cast(adsk.core.Application.get())
        msg = "You just ACTIVATED a document called: {} ".format(document.name)
        # msg = "You just opened a document"
        app.userInterface.messageBox(msg)


class SampleDocumentEvent2(Fusion360DocumentEvent):

    def document_event_received(self, event_args, document):
        app = adsk.core.Application.cast(adsk.core.Application.get())
        msg = "You just CLOSED a document called: {}".format(document.name)
        app.userInterface.messageBox(msg)
