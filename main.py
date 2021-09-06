import sys
from PyQt5.QtWidgets import QApplication
from controller import MountainExtract
from PyQt5.QtGui import QIcon, QPixmap

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mountainExtract = MountainExtract()
    mountainExtract.setWindowTitle('山脚线提取')
    # 设置程序图标
    icon = QIcon()
    icon.addPixmap(QPixmap('resource/glass.png'))
    mountainExtract.setWindowIcon(icon)
    # 主界面显示
    mountainExtract.show()
    sys.exit(app.exec_())