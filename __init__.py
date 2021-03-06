# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GPXTrackManager
                                 A QGIS plugin
 A plugin to simplify the process of creating and editing GPX routes
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-10-28
        copyright            : (C) 2021 by Dave Barter
        email                : dave@phased.co.uk
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GPXTrackManager class from file GPXTrackManager.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .gpxTrackManager import GPXTrackManager
    return GPXTrackManager(iface)
