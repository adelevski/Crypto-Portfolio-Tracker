import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from funcs import get_total, get_prices, get_df


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(600, 300, 300, 300)
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))
        self.setWindowTitle("Crypto-GUI")
        self.initUI()
        

    def initUI(self):
        self.label_CryptoGUI = QtWidgets.QLabel(self)
        self.label_CryptoGUI.setGeometry(30, 10, 160, 40)
        self.label_CryptoGUI.setText("Crypto-GUI")

        self.label_timer = QtWidgets.QLabel(self)
        self.label_timer.setGeometry(180, 10, 100, 40)

        self.checkbox_freeze = QtWidgets.QCheckBox(self)
        self.checkbox_freeze.setGeometry(180, 30, 100, 40)
        self.checkbox_freeze.setText("Freeze")
        self.checkbox_freeze.clicked.connect(self.freeze)

        self.binance = QtWidgets.QLabel(self)
        self.binance.setGeometry(30, 70, 150, 20)

        self.coinbase = QtWidgets.QLabel(self)
        self.coinbase.setGeometry(30, 100, 150, 20)

        self.coinbasepro = QtWidgets.QLabel(self)
        self.coinbasepro.setGeometry(30, 130, 150, 20)

        self.kucoin = QtWidgets.QLabel(self)
        self.kucoin.setGeometry(30, 160, 150, 20)

        self.voyager = QtWidgets.QLabel(self)
        self.voyager.setGeometry(30, 190, 150, 20)

        self.metamask = QtWidgets.QLabel(self)
        self.metamask.setGeometry(30, 220, 150, 20)

        self.label_total = QtWidgets.QLabel(self)
        self.label_total.setGeometry(30, 250, 200, 50)

        self.accounts = {
            'Binance US': [self.binance, 0], 
            'Coinbase': [self.coinbase, 0], 
            'Coinbase Pro': [self.coinbasepro, 0],
            'KuCoin': [self.kucoin, 0],
            'Voyager': [self.voyager, 0],
            'MetaMask': [self.metamask, 0]
        }
        self.total_balance, self.all_holdings = get_total()

        self.refresh()
        self.timer_start()


    def timer_start(self):
        now = QtCore.QTime.currentTime()
        next_update = QtCore.QTime(now.hour(), now.minute(), 14).addSecs(60)
        self.time_left_int = now.secsTo(next_update)
        self.my_qtimer = QtCore.QTimer(self)
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)
        # self.update_timer()


    def timer_timeout(self):
        self.time_left_int -= 1
        if self.time_left_int == -1:
            self.time_left_int = 60
            self.refresh()
        self.update_timer()


    def update_timer(self):
        self.label_timer.setText("Next Update: " + str(self.time_left_int))


    def refresh(self):
        prices = get_prices(self.total_balance)
        for exchange, totals in self.all_holdings.items():
            df, total_value = get_df(totals, prices, form=False)
            self.accounts[exchange][1] = total_value
        if not self.checkbox_freeze.isChecked():
            self.update_labels()
            

    def update_labels(self):
        for name, (label, amount) in self.accounts.items():
            label.setText(f"{name} - ${round(amount, 2)}")
            label.adjustSize()
        self.label_total.setText(f"Total: ${round(sum(n for _, n in self.accounts.values()), 2)}")
        self.label_total.adjustSize()

    
    def freeze(self):
        if self.checkbox_freeze.isChecked(): pass
        else: self.update_labels()


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()