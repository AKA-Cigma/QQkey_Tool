# -*- coding: utf-8 -*-

import time
import os
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from urlextract import URLExtract
from webbrowser import open as web_open

hint_flag = False

def get_file_path(name):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    file_path = os.path.join(basedir, name)
    return file_path

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.login_data = [
            {
                "proxy_url": "https://qzs.qq.com/qzone/v6/portal/proxy.html",
                "daid": "5",
                "hide_title_bar": "1",
                "low_login": "0",
                "qlogin_auto_login": "1",
                "no_verifyimg": "1",
                "link_target": "blank",
                "appid": "549000912",
                "style": "22",
                "target": "self",
                "s_url": "https://qzs.qq.com/qzone/v5/loginsucc.html?para=izone",
                "pt_qr_app": "手机QQ空间",
                "pt_qr_link": "https://z.qzone.com/download.html",
                "self_regurl": "https://qzs.qq.com/qzone/v6/reg/index.html",
                "pt_qr_help_link": "https://z.qzone.com/download.html",
                "pt_no_auth": "0"
            },
            {
                "pt_disable_pwd": "1",
                "appid": "715030901",
                "hide_close_icon": "1",
                "daid": "73",
                "pt_no_auth": "1",
                "s_url": "https://qun.qq.com/"
            },
            {"u1":"https://wx.mail.qq.com/list/readtemplate?name=login_page.html","s_url":None},
            {
                "appid": "8000201",
                "style": "20",
                "s_url": "https://vip.qq.com/loginsuccess.html",
                "maskOpacity": "60",
                "daid": "18",
                "target": "self"
            },
            {"u1":"https://www.weiyun.com/?adtag=ntqqmainpanel","s_url":None},
            {
                "style": "40",
                "appid": "1600001573",
                "s_url": "https://accounts.qq.com/homepage#/",
                "daid": "761",
                "hide_close_icon": "0"
            },
            {
                "appid": "10000101",
                "s_url": "https://qqshow.qq.com/manage/myCreation",
                "hide_close_icon": "1"
            },
            {
                "s_url": "https://huifu.qq.com/recovery/index.html?frag=1",
                "style": "20",
                "appid": "715021417",
                "daid": "768",
                "proxy_url": "https://huifu.qq.com/proxy.html"
            },
            {"u1": "https://docs.qq.com/desktop/?tdsourcetag=s_ntpcqq_panel_app", "s_url": None},
            {
                "daid": "377",
                "style": "11",
                "appid": "716027613",
                "target": "self",
                "pt_disable_pwd": "1",
                "s_url": "https://connect.qq.com/login_success.html",
                "t": str(time.time())
            },
            {
                "appid": "501038301",
                "target": "self",
                "s_url": "https://im.qq.com/loginSuccess"
            }
        ]
        Dialog.setObjectName("Dialog")
        Dialog.resize(442,72)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Dialog.setFont(font)
        Dialog.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        Dialog.setWindowIcon(QtGui.QIcon(get_file_path("./icon.ico")))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(41, 10, 91, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 35, 81, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 37, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(300, 10, 121, 22))
        self.comboBox.setObjectName("comboBox")
        for i in range(11):
            self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(233, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 40, 191, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Key解析器"))
        self.label.setText(_translate("Dialog", "QQ号:"))
        self.label_2.setText(_translate("Dialog", "Clientkey:"))
        self.comboBox.setItemText(0, _translate("Dialog", "QQ空间"))
        self.comboBox.setItemText(1, _translate("Dialog", "QQ群"))
        self.comboBox.setItemText(2, _translate("Dialog", "QQ邮箱"))
        self.comboBox.setItemText(3, _translate("Dialog", "QQ VIP"))
        self.comboBox.setItemText(4, _translate("Dialog", "微云"))
        self.comboBox.setItemText(5, _translate("Dialog", "QQ安全中心"))
        self.comboBox.setItemText(6, _translate("Dialog", "超级QQ秀"))
        self.comboBox.setItemText(7, _translate("Dialog", "QQ恢复系统"))
        self.comboBox.setItemText(8, _translate("Dialog", "腾讯文档"))
        self.comboBox.setItemText(9, _translate("Dialog", "QQ互联"))
        self.comboBox.setItemText(10, _translate("Dialog", "QQ官网"))
        self.label_3.setText(_translate("Dialog", "登录网站:"))
        self.pushButton.setText(_translate("Dialog", "登录"))

    def login(self):
        global hint_flag
        session = requests.session()
        uin = self.lineEdit.text()
        clientkey = self.lineEdit_2.text()
        login_data = self.login_data[self.comboBox.currentIndex()]
        if not hint_flag:
            QtWidgets.QMessageBox.information(Dialog, "提示", "部分网站在打开后可能出现白屏的情况,这时请手动打开对应官网才可正常使用")
            hint_flag = True
        if login_data['s_url']:
            login_htm = session.get(
                "https://xui.ptlogin2.qq.com/cgi-bin/xlogin",params=login_data)
            q_cookies = requests.utils.dict_from_cookiejar(login_htm.cookies)
            pt_local_token = q_cookies.get("pt_local_token")
            headers = {"Referer": "https://xui.ptlogin2.qq.com/",
                       "Host": "ssl.ptlogin2.qq.com",
                       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"}
            params = {
                "u1": login_data['s_url'],
                "clientuin": uin,
                "pt_aid": login_data['appid'],
                "keyindex": "19",
                "pt_local_tk": pt_local_token,
                "pt_3rd_aid": "0",
                "ptopt": "1",
                "style": "40"
            }
            if login_data.get("daid"): params['daid'] = login_data.get("daid")
            cookies = {
                "clientkey": clientkey,
                "clientuin": str(uin),
                "pt_local_token": pt_local_token
            }
            login_res = session.get("https://ssl.ptlogin2.qq.com/jump",params=params,cookies=cookies,headers=headers)
            extractor = URLExtract()
            login_url = extractor.find_urls(login_res.text)[0]
            web_open(login_url)
        else:
            web_open(f"https://ssl.ptlogin2.qq.com/jump?ptlang=1033&clientuin={uin}&clientkey={clientkey}&u1={login_data['u1']}&keyindex=19")
if __name__ == '__main__':
    # 获取UIC窗口操作权限
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    # 调自定义的界面（即刚转换的.py对象）
    Ui = Ui_Dialog()
    Ui.setupUi(Dialog)
    # 显示窗口并释放资源
    Dialog.show()
    sys.exit(app.exec_())