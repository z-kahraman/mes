import sys
import paho.mqtt.client as mqtt

from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2 import QtCore
from PySide2.QtCore import Qt

from ui_arduino import Ui_MainWindow
from datetime import datetime
from data_base import insertVariableIntoTable, main

sql_insert = insertVariableIntoTable


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("ESP-01 Python and MQTT")

        self.lbl_durum = self.ui.lbl_durum
        self.list_durum = self.ui.list_widget

        self.show()


def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))
    # subscribe topic
    client.subscribe("TEMPERATURE")


@QtCore.Slot(int)
def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    window.lbl_durum.setText("{} -> {}".format(
        "\
        Incoming Data",
        message.payload.decode("utf-8"),
    ))
    print("Message Received-> " + message.topic + " " + data)
    now = datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
    print("type data {}".format(type(data)))
    print("str now {}".format(type(str(now))))
    sql_insert("machine", data, str(now))
    veri = [now + " " + "incoming data from sensor: " + data]
    window.list_durum.addItems(veri)
    # window.list_durum.setSortingEnabled(True)
    window.list_durum.sortItems(Qt.DescendingOrder)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    sql = main()

    mqttBroker = "broker.hivemq.com"
    client = mqtt.Client("Smartphone")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(mqttBroker)
    client.loop_start()

    sys.exit(app.exec_())
