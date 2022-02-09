import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from models import DataFrameModel
from funcs import get_total, get_prices, get_df



class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(600, 300, 300, 400)
        self.setWindowTitle("Crypto-GUI")
        self.totals = {
            'Binance US': None, 
            'Coinbase': None, 
            'Coinbase Pro': None,
            'KuCoin': None
        }
        self.initUI()
        self.refresh()


    def initUI(self):
        self.label_CryptoGUI = QtWidgets.QLabel(self)
        self.label_CryptoGUI.setGeometry(30, 10, 160, 40)
        self.label_CryptoGUI.setText("Crypto-GUI")

        self.button_Refresh = QtWidgets.QPushButton(self)
        self.button_Refresh.setGeometry(30, 60, 150, 50)
        self.button_Refresh.setText("Refresh")
        self.button_Refresh.clicked.connect(self.refresh)

        self.checkBox_Binance = QtWidgets.QCheckBox(self)
        self.checkBox_Binance.setGeometry(30, 130, 90, 20)
        self.checkBox_Binance.setText("Binance US")

        self.checkBox_Coinbase = QtWidgets.QCheckBox(self)
        self.checkBox_Coinbase.setGeometry(30, 160, 80, 20)
        self.checkBox_Coinbase.setText("Coinbase")

        self.checkBox_CoinbasePro = QtWidgets.QCheckBox(self)
        self.checkBox_CoinbasePro.setGeometry(30, 190, 110, 20)
        self.checkBox_CoinbasePro.setText("Coinbase Pro")

        self.checkBox_KuCoin = QtWidgets.QCheckBox(self)
        self.checkBox_KuCoin.setGeometry(30, 220, 80, 20)
        self.checkBox_KuCoin.setText("KuCoin")

        self.checkBox_Voyager = QtWidgets.QCheckBox(self)
        self.checkBox_Voyager.setGeometry(30, 250, 80, 20)
        self.checkBox_Voyager.setText("Voyager")

        self.checkBox_MetaMask = QtWidgets.QCheckBox(self)
        self.checkBox_MetaMask.setGeometry(30, 280, 80, 20)
        self.checkBox_MetaMask.setText("MetaMask")
        

        self.label_Amount = QtWidgets.QLabel(self)
        self.label_Amount.setGeometry(10, 330, 200, 50)

    def refresh(self):
        total_balance, all_holdings = get_total()
        prices = get_prices(total_balance)
        for exchange, totals in all_holdings.items():
            df, total_value = get_df(totals, prices, form=False)
            self.totals[exchange] = total_value

    def update_amount(self):
        


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()