# -*- coding: utf-8 -*-
##############################################################################
#
#   Smtp Mail User
#   Copyright 2018 RGB Consulting, SL
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
    'name': "Smtp Mail User",
    'version': '8.0.1.0.0',
    'category': 'Mail',
    'summary': 'Personalized mail server',
    'description': """Mail server""",
    'author': 'RGB Consulting SL',
    'license': 'AGPL-3',
    'website': "https://www.rgbconsulting.com",
    "depends" : ['mail'],

    'data': [
        'security/ir.model.access.csv',
    ],

}
