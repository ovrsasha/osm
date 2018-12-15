import QtQuick 2.5
import QtLocation 5.6
import QtPositioning 5.6

Rectangle {
    width: parent.width
    height: parent.height
    visible: true

    Plugin {
        id: mapPlugin
        name: "osm"
    }

    Map {
        objectName: "map"
        property real lat: 54.0
        property real lon: 54.0
        property int zoom: 14
        anchors.fill: parent
        plugin: mapPlugin
        center: QtPositioning.coordinate(lat, lon)
        zoomLevel: zoom
    }
}
