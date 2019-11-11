import traceback

import adsk.core

from .commands import SampleCommand1, SampleCommand2, SamplePaletteCommand, \
    SampleCustomEvent, SampleDocumentEvents, SampleWorkspaceEvents
from .apper import apper

my_app = apper.FusionApp('SampleApp', "MyOrganization", False)

my_app.add_command(
    'Sample Command 1',
    SampleCommand1.SampleCommand1,
    {
        'cmd_description': 'Hello World!',
        'cmd_id': 'sample_cmd_1',
        'workspace': 'FusionSolidEnvironment',
        'toolbar_tab_id': 'Sample Tab',
        'toolbar_panel_id': 'Commands',
        'cmd_resources': 'demo_icons',
        'command_visible': True,
        'command_promoted': True,
    }
)

my_app.add_command(
    'Sample Command 2',
    SampleCommand2.SampleCommand2,
    {
        'cmd_description': 'A simple example of a Fusion 360 Command with various inputs',
        'cmd_id': 'sample_cmd_2',
        'workspace': 'FusionSolidEnvironment',
        'toolbar_tab_id': 'Sample Tab',
        'toolbar_panel_id': 'Commands',
        'cmd_resources': 'demo_icons',
        'command_visible': True,
        'command_promoted': False,
    }
)

my_app.add_command(
    'Sample Palette Command - Show',
    SamplePaletteCommand.SamplePaletteShowCommand,
    {
        'cmd_description': 'Fusion Demo Palette Description',
        'cmd_id': 'sample_palette_show',
        'workspace': 'FusionSolidEnvironment',
        'toolbar_tab_id': 'Sample Tab',
        'toolbar_panel_id': 'Palette',
        'cmd_resources': 'demo_icons',
        'command_visible': True,
        'command_promoted': True,
        'palette_id': 'sample_palette',
        'palette_name': 'Sample Fusion 360 HTML Palette',
        'palette_html_file_url': 'palette_html/demo.html',
        'palette_is_visible': True,
        'palette_show_close_button': True,
        'palette_is_resizable': True,
        'palette_width': 500,
        'palette_height': 600,
    }
)

my_app.add_command(
    'Sample Palette Command - Send',
    SamplePaletteCommand.SamplePaletteSendCommand,
    {
        'cmd_description': 'Send data from a regular Fusion 360 command to a palette',
        'cmd_id': 'sample_palette_send',
        'workspace': 'FusionSolidEnvironment',
        'toolbar_tab_id': 'Sample Tab',
        'toolbar_panel_id': 'Palette',
        'cmd_resources': 'demo_icons',
        'command_visible': True,
        'command_promoted': False,
        'palette_id': 'sample_palette',
    }
)
app = adsk.core.Application.cast(adsk.core.Application.get())
ui = app.userInterface
try:

    my_app.add_custom_event("sample_message_system", SampleCustomEvent.SampleCustomEvent1)

    my_app.add_document_event("sample_open_event", app.documentActivated, SampleDocumentEvents.SampleDocumentEvent1)
    my_app.add_document_event("sample_close_event", app.documentClosed, SampleDocumentEvents.SampleDocumentEvent2)

    my_app.add_workspace_event("sample_workspace_event", ui.workspaceActivated, SampleWorkspaceEvents.SampleWorkspaceEvent1)
except:
    if ui:
        ui.messageBox('Load failed: {}'.format(traceback.format_exc()))

# Set to True to display various useful messages when debugging your app
debug = False


def run(context):
    my_app.run_app()


def stop(context):
    my_app.stop_app()
