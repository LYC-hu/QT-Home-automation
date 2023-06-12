import ctypes
import sys
import threading
import control_panel
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtWidgets
import MainWindow_action
import hmac
from hashlib import sha1
import time
from paho.mqtt.client import MQTT_LOG_INFO, MQTT_LOG_NOTICE, MQTT_LOG_WARNING, MQTT_LOG_ERR, MQTT_LOG_DEBUG
from paho.mqtt import client as mqtt
import json
import random


# 设备证书（ProductKey、DeviceName和DeviceSecret），三元组
productKey = 'iuslKy1Y7Wv'
deviceName = 'RFbTIkYsmxz4AHYHr3KV'
deviceSecret = '57a3084b1c20b1641522a518406661fc'

# ClientId Username和 Password 签名模式下57a3084b1c20b1641522a518406661fc的设置方法，参考文档 https://help.aliyun.com/document_detail/73742.html?spm=a2c4g.11186623.6.614.c92e3d45d80aqG
# MQTT - 合成connect报文中使用的 ClientID、Username、Password
mqttClientId ='iuslKy1Y7Wv.RFbTIkYsmxz4AHYHr3KV|securemode=2,signmethod=hmacsha256,timestamp=1686299807850|'
mqttUsername = 'RFbTIkYsmxz4AHYHr3KV&iuslKy1Y7Wv'
content = 'clientId' + deviceName + 'deviceName' + deviceName + 'productKey' + productKey
mqttPassword = '6c2309f823591942c81fdee8d48b6411142fe9c826a67f7c03f95d851811b067'

# 接入的服务器地址
regionId = 'cn-shanghai'
# MQTT 接入点域名
brokerUrl = productKey + '.iot-as-mqtt.' + regionId + '.aliyuncs.com'

# Topic，post，客户端向服务器上报消息
topic_post = '/sys/' + productKey + '/' + deviceName + '/thing/event/property/post'
# Topic，set，服务器向客户端下发消息
topic_set = '/sys/' + productKey + '/' + deviceName + '/thing/service/property/set'

# 物模型名称的前缀（去除后缀的数字）
modelName = 'LightSwitch'

# 下发的设置报文示例：{"method":"thing.service.property.set","id":"1227667605","params":{"PowerSwitch_1":1},"version":"1.0.0"}
# json合成上报开关状态的报文
def json_switch_set(num, status):       #开关控制
    switch_info = {}
    switch_data = json.loads(json.dumps(switch_info))
    switch_data['method'] = '/thing/event/property/post'
    switch_data['id'] = random.randint(100000000,999999999) # 随机数即可，用于让服务器区分开报文
    switch_status = {modelName + num : status}
    switch_data['params'] = switch_status
    return json.dumps(switch_data, ensure_ascii=False)

# 开关的状态，0/1

# 建立mqtt连接对象
client = mqtt.Client(mqttClientId, protocol=mqtt.MQTTv311, clean_session=True)

def on_log(client, userdata, level, buf):
    if level == MQTT_LOG_INFO:
        head = 'INFO'
    elif level == MQTT_LOG_NOTICE:
        head = 'NOTICE'
    elif level == MQTT_LOG_WARNING:
        head = 'WARN'
    elif level == MQTT_LOG_ERR:
        head = 'ERR'
    elif level == MQTT_LOG_DEBUG:
        head = 'DEBUG'
    else:
        head = level
    print('%s: %s' % (head, buf))
# MQTT成功连接到服务器的回调处理函数
def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    # 与MQTT服务器连接成功，之后订阅主题
    client.subscribe(topic_post, qos=0)
    client.subscribe(topic_set, qos=0)
    # 向服务器发布测试消息
    client.publish(topic_post, payload='test msg', qos=0)
# MQTT接收到服务器消息的回调处理函数
def on_message(client, userdata, msg):
    print('recv:', msg.topic + ' ' + str(msg.payload))
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected disconnection %s' % rc)

def mqtt_connect_aliyun_iot_platform():
    client.on_log = on_log
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.username_pw_set(mqttUsername, mqttPassword)
    print('clientId:', mqttClientId)
    print('userName:', mqttUsername)
    print('password:', mqttPassword)
    print('brokerUrl:', brokerUrl)

    try:
        client.connect(brokerUrl, 1883, 60)
    except:
        print('阿里云物联网平台MQTT服务器连接错误，请检查设备证书三元组、及接入点的域名！')
    client.loop_forever()

def LED_On():
    switchPost = json_switch_set('1', 1)
    client.publish(topic_post, payload=switchPost, qos=0)
def LED_Off():
    switchPost = json_switch_set('1', 0)
    client.publish(topic_post, payload=switchPost, qos=0)

class thread_with_exception(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        try:
            while True:
                print('running ' + self.name)
        finally:
            print('ended')
    def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._actibe.items():
            if thread is self:
                return id
    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncEc(thread_id, ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
class controlpanelactions(control_panel.Ui_Form, QMainWindow):
    def __init__(self):
        super(control_panel.Ui_Form, self).__init__()
        super().__init__()
        self.setupUi(self)

        global t1
        t1 = threading.Thread(target=mqtt_connect_aliyun_iot_platform, )
        t1.start()


        self._exit_.clicked.connect(self.over)  #退出按钮
        self.ON.clicked.connect(self.turn_on)
        self.OFF.clicked.connect(self.turn_off)
    def over(self):
        t1 = thread_with_exception('Thread 1')
        t1.start()
        time.sleep(2)
        t1.raise_exception()
        t1.join()     #退出线程1
        self.close()

    def turn_on(self):
        t2 = threading.Thread(target=LED_On, )
        t2.start()
        t2.join()
    def turn_off(self):
        t2 = threading.Thread(target=LED_Off, )
        t2.start()
        t2.join()