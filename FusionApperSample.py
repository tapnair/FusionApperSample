import adsk.core

from .commands import SampleCommand1, SampleCommand2, SamplePaletteCommand, SampleCustomEvent, SampleDocumentEvents
from .apper.FusionApp import FusionApp
# from .apper.Fusion360Utilities import get_std_out_file, get_std_err_file, get_log_file

import sys

my_app = FusionApp('SampleApp', "MyOrganization", False)

# std_err_file = get_std_err_file(my_app.name)
# std_out_file = get_std_out_file(my_app.name)
# sys.stdout = open(std_out_file, 'w')
# sys.stderr = open(std_err_file, 'w')

SampleCommand1.SampleCommand1(
    'Sample Command 1',
    my_app,
    {
        'cmd_description': 'Hello World!',
        'cmd_id': 'sample1',
        'workspace': 'FusionSolidEnvironment',
        'toolbar_tab_id': 'Sample Tab',
        'toolbar_panel_id': 'Commands3',
        'cmd_resources': 'demo_icons',
        'command_visible': True,
        'command_promoted': True,
    }
)

SampleCommand2.SampleCommand2(
    'Sample Command 2',
    my_app,
    {
        'cmd_description': 'A simple example of a Fusion 360 Command with various inputs',
        'cmd_id': 'sample2',
        'workspace': 'FusionSolidEnvironment',
        'toolbar_tab_id': 'Sample Tab',
        'toolbar_panel_id': 'Commands3',
        'cmd_resources': 'demo_icons',
        'command_visible': True,
        'command_promoted': False,
    }
)

SamplePaletteCommand.SamplePaletteShowCommand(
    'Sample Palette Command - Show',
    my_app,
    {
        'cmd_description': 'Fusion Demo Palette Description',
        'cmd_id': 'palette_show',
        'workspace': 'FusionSolidEnvironment',
        'toolbar_tab_id': 'Sample Tab',
        'toolbar_panel_id': 'Palette',
        'cmd_resources': 'demo_icons',
        'command_visible': True,
        'command_promoted': True,
        'palette_id': 'sample_palette',
        'palette_name': 'Sample Fusion 360 HTML Palette',
        'palette_html_file_url': './lib/commands/palette_html/demo.html',
        'palette_is_visible': True,
        'palette_show_close_button': True,
        'palette_is_resizable': True,
        'palette_width': 500,
        'palette_height': 600,
    }
)

SamplePaletteCommand.SamplePaletteSendCommand(
    'Sample Palette Command - Send',
    my_app,
    {
        'cmd_description': 'Send data from a regular Fusion 360 command to a palette',
        'cmd_id': 'palette_send',
        'workspace': 'FusionSolidEnvironment',
        'toolbar_tab_id': 'Sample Tab',
        'toolbar_panel_id': 'Palette',
        'cmd_resources': 'demo_icons',
        'command_visible': True,
        'command_promoted': False,
        'palette_id': 'sample_palette',
    }
)

SampleCustomEvent.SampleCustomEvent1("message_system", my_app)

app = adsk.core.Application.cast(adsk.core.Application.get())
SampleDocumentEvents.SampleDocumentEvent1("open_event", app.documentActivated, my_app)
SampleDocumentEvents.SampleDocumentEvent2("close_event", app.documentClosed, my_app)

# Set to True to display various useful messages when debugging your app
debug = False


def run(context):
    my_app.run_app()


def stop(context):
    my_app.stop_app()
