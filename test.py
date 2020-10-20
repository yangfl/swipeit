#!/usr/bin/env python3

import sys
import os

import time
from threading import Thread

from Xlib.display import Display
from Xlib.ext import xinput


def main(argv):
    display = Display()
    try:
        extension_info = display.query_extension('XInputExtension')
        xinput_major = extension_info.major_opcode

        version_info = display.xinput_query_version()
        print('Found XInput version %u.%u' % (
          version_info.major_version,
          version_info.minor_version,
        ))

        screen = display.screen()
        screen.root.xinput_select_events([
          (xinput.AllDevices, xinput.KeyPressMask | xinput.KeyReleaseMask),
        ])

        while True:
            event = display.next_event()
            if (
              event.type == display.extension_event.GenericEvent
              and event.extension == xinput_major
            ):
                print(event)

    finally:
        display.close()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
