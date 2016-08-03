# -*- coding: utf-8 -*-
##############################################################################
#
#   WEB Percentage Widget
#   Copyright 2016 RGB Consulting, SL
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "WEB Percentage Widget",
    'version': '1.0',
    'depends': ['base', 'web'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "http://www.rgbconsulting.com",
    'category': 'web',
    'summary': """WEB Widget for percentages""",
    'description': """
WEB Percentage Widget
=====================
This module adds a new widget, *percentage*, to show float fields as a percentage.
    """,

    'data': [
        'views/add_js.xml',
    ],

    'qweb': [
        'static/src/xml/percentage_widget.xml',
    ],
}
