#!/bin/sh
#
#    Copyright 2007-2009 Canonical Ltd.
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 2 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA

LIBFILES="formatstick.py raw_write.py raw_format.py mountutils.py"
DATAFILES="formatstick.ui"


if [ "$1" = "uninstall" ]; then
    rm -rf /usr/lib/formatstick
    rm -rf /usr/share/formatstick
    rm -r /usr/share/applications/formatstick.desktop
    rm -r /usr/share/applications/formatstick-kde.desktop
    rm -r /usr/share/applications/formatstick-format.desktop
    rm -r /usr/share/applications/formatstick-kde-format.desktop
    rm -f /usr/bin/formatstick
    rm -rf /usr/share/polkit-1/actions/org.linuxmint.im.policy
    rm -rf /usr/share/kde4/apps/solid/actions/formatstick-format.desktop
else
    cp share/applications/formatstick.desktop /usr/share/applications/
    cp share/applications/formatstick-format.desktop /usr/share/applications/
    cp share/applications/formatstick-kde.desktop /usr/share/applications/
    cp share/applications/formatstick-format-kde.desktop /usr/share/applications/
    cp share/polkit/org.linuxmint.im.policy /usr/share/polkit-1/actions
    cp share/kde4/formatstick-format_action.desktop /usr/share/kde4/apps/solid/actions
    cp formatstick /usr/bin/
    mkdir -p /usr/lib/formatstick
    mkdir -p /usr/share/formatstick

    for item in $LIBFILES; do
        cp lib/$item /usr/lib/formatstick/
    done

    for item in $DATAFILES; do
        cp share/formatstick/$item /usr/share/formatstick/
    done
fi
