# -*- coding: utf-8 -*-

###################################################################################
# 
#    MuK Document Management System
#
#    Copyright (C) 2017 MuK IT GmbH
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

{
    'name': "MuK Documents Access Control",
    'summary': """Document Management System""",
    'description': """ 
        Access Control Extension
    """,
    'version': '10.0.1.0.0',   
    'category': 'Document Management',   
    'license': 'AGPL-3',    
    'author': "MuK IT",
    'website': "http://www.mukit.at",
    'contributors': [
        "Mathias Markl <mathias.markl@mukit.at>",
        "Kerrim Abdelhamed <kerrim.adbelhamed@mukit.at>",
    ],
    'depends': [
        'muk_dms',
        'hr',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/muk_dms_view_groups.xml',
        'views/muk_dms_view_directory.xml',
        'views/muk_dms_view_file.xml',
    ],
    'images': [
        'static/description/banner.png'
    ],
    "installable": True,
}
