import sys
from pathlib import Path
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLabel, QFileDialog,
                             QMessageBox, QFrame, QDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QPalette, QColor, QIcon
from PyQt5.QtWidgets import QStyleFactory
import qrcode
import io

class QRCodeDialog(QDialog):
    def __init__(self, qr_image, file_name, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"QR-код для {file_name}")
        self.setModal(True)
        self.setFixedSize(500, 500)

        icon_path = Path(__file__).parent / 'icon' / 'icon.ico'
        if icon_path.exists():
            self.setWindowIcon(QIcon(str(icon_path)))

        self.setStyle(QStyleFactory.create('Fusion'))

        layout = QVBoxLayout()

        self.qr_label = QLabel()
        self.qr_label.setAlignment(Qt.AlignCenter)
        self.qr_label.setFrameStyle(QFrame.Box)
        self.qr_label.setLineWidth(1)

        img_byte_arr = io.BytesIO()
        qr_image.save(img_byte_arr, format='PNG')
        pixmap = QPixmap()
        pixmap.loadFromData(img_byte_arr.getvalue())

        scaled_pixmap = pixmap.scaled(
            450, 450,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.qr_label.setPixmap(scaled_pixmap)

        layout.addWidget(self.qr_label)

        close_btn = QPushButton("Закрыть")
        close_btn.clicked.connect(self.accept)
        close_btn.setMinimumHeight(35)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        layout.addWidget(close_btn)

        self.setLayout(layout)

class AmneziaWGConfigurator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.conf_file = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("AmneziaWG Configuration QR Generator")
        self.setFixedSize(450, 280)

        icon_path = Path(__file__).parent / 'icon' / 'icon.ico'
        if icon_path.exists():
            self.setWindowIcon(QIcon(str(icon_path)))

        QApplication.setStyle(QStyleFactory.create('Fusion'))

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(240, 240, 240))
        palette.setColor(QPalette.Highlight, QColor(33, 150, 243))
        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        self.setPalette(palette)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(25, 15, 25, 15)

        image_label = QLabel()
        image_label.setAlignment(Qt.AlignCenter)

        image_path = Path(__file__).parent / "logo" / "logo.png"
        if image_path.exists():
            pixmap = QPixmap(str(image_path))
            available_width = 450 - 50
            scaled_pixmap = pixmap.scaledToWidth(
                available_width,
                Qt.SmoothTransformation
            )
            image_label.setPixmap(scaled_pixmap)

        layout.addWidget(image_label)

        subtitle_label = QLabel("Генератор QR-кода из конфигураций созданных в формате AmneziaWG")
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet("color: #666; margin-bottom: 5px; font-size: 11px;")
        subtitle_label.setWordWrap(True)
        layout.addWidget(subtitle_label)

        info_layout = QHBoxLayout()
        info_layout.setAlignment(Qt.AlignCenter)

        self.info_btn = QPushButton("О программе")
        self.info_btn.setFixedSize(100, 25)
        self.info_btn.setCursor(Qt.PointingHandCursor)
        self.info_btn.setStyleSheet("""
            QPushButton {
                background-color: #607D8B;
                color: white;
                border: none;
                border-radius: 4px;
                font-size: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #546E7A;
            }
        """)
        self.info_btn.clicked.connect(self.show_info)
        info_layout.addWidget(self.info_btn)

        layout.addLayout(info_layout)
        layout.addSpacing(5)

        self.info_label = QLabel("")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setStyleSheet("color: #666; margin-top: 5px; font-size: 10px;")
        self.info_label.setWordWrap(True)
        self.info_label.setMinimumHeight(40)
        self.info_label.setVisible(False)
        layout.addWidget(self.info_label)

        file_layout = QHBoxLayout()
        file_layout.setSpacing(5)

        self.file_label = QLabel("")
        self.file_label.setMinimumHeight(28)
        self.file_label.setStyleSheet("""
            QLabel {
                border: 1px solid #ccc;
                padding: 5px 8px;
                border-radius: 4px;
                background-color: white;
                font-size: 11px;
            }
        """)
        file_layout.addWidget(self.file_label, 1)

        self.select_btn = QPushButton("Обзор")
        self.select_btn.setFixedSize(65, 28)
        self.select_btn.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 11px;
                padding: 0px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """)
        self.select_btn.clicked.connect(self.select_conf_file)
        file_layout.addWidget(self.select_btn)

        layout.addLayout(file_layout)

        self.generate_btn = QPushButton("Показать QR-код")
        self.generate_btn.setMinimumHeight(35)
        self.generate_btn.setEnabled(False)
        self.generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
        """)
        self.generate_btn.clicked.connect(self.generate_qr_code)
        layout.addWidget(self.generate_btn)

        central_widget.setLayout(layout)

    def select_conf_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите файл конфигурации AmneziaWG",
            "",
            "Конфигурационные файлы (*.conf);;Все файлы (*)"
        )

        if file_path:
            self.conf_file = Path(file_path)
            filename = self.conf_file.name
            if len(filename) > 30:
                filename = filename[:27] + "..."
            self.file_label.setText(filename)
            self.generate_btn.setEnabled(True)

    def generate_qr_code(self):
        if not self.conf_file or not self.conf_file.exists():
            QMessageBox.warning(self, "Ошибка", "Файл конфигурации не найден!")
            return

        try:
            with open(self.conf_file, 'r', encoding='utf-8') as file:
                config_content = file.read()

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(config_content)
            qr.make(fit=True)

            qr_image = qr.make_image(fill_color="black", back_color="white")

            dialog = QRCodeDialog(qr_image, self.conf_file.name, self)
            dialog.exec_()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось создать QR-код: {str(e)}")

    def show_info(self):
        info_text = """
        <div style='text-align: left; margin-left: 0px;'>
            <div style='margin: 0 0 10px 0;'>
                <p style='margin: 0; font-size: 14px;'><b>Назначение:</b></p>
                <p style='margin: 5px 0 0 0; font-size: 12px;'>Генератор QR-кодов для переноса конфигураций<br>
                AmneziaWG 1.0 / 1.5 / 2.0 на мобильные устройства.</p>
            </div>

            <div style='margin: 20px 0 15px 0;'>
                <p style='margin: 0; font-size: 14px;'><b>Поддерживаемые параметры мусорных пакетов:</b></p>
                <p style='margin: 5px 0 0 0; font-size: 12px;'>
                • Jc - Количество "мусорных" пакетов, которые будут отправлены сразу после основной последовательности пакетов маскировки.<br>
                • Jmin - Минимальный размер (в байтах) "мусорных" пакетов.<br>
                • Jmax - Максимальный размер (в байтах) "мусорных" пакетов.<br>
                • S1 - Максимальная длина (в байтах) для пакетов инициализации (Init).<br>
                • S2 - Максимальная длина (в байтах) для пакетов ответа (Response).<br>
                • S3 - Максимальная длина (в байтах) для "cookie" пакетов (защита от DoS-атак).<br>
                • S4 - Максимальная длина (в байтах) для пакетов с данными (Data).<br>
                • H1 - Динамический заголовок (32 бит) для пакетов инициализации (Init).<br>
                • H2 - Динамический заголовок (32 бит) для пакетов ответа (Response).<br>
                • H3 - Динамический заголовок (32 бит) для "cookie" пакетов (защита от DoS-атак).<br>
                • H4 - Динамический заголовок (32 бит) для пакетов с данными (Data).<br>
                • I1 - Сформированный UDP-пакет. Синтаксис CPS.<br>
                • I2 - Сформированный UDP-пакет. Синтаксис CPS.<br>
                • I3 - Сформированный UDP-пакет. Синтаксис CPS.<br>
                • I4 - Сформированный UDP-пакет. Синтаксис CPS.<br>  
                • I5 - Сформированный UDP-пакет. Синтаксис CPS.<br>              
                </p>
            </div>

            <div style='margin: 20px 0 15px 0;'>
                <p style='margin: 0; font-size: 14px;'><b>Использование:</b></p>
                <p style='margin: 5px 0 0 10; text-align: left; font-size: 12px;'>
                1. Нажмите "Обзор"<br>
                2. Выберите .conf файл<br>
                3. Нажмите "Показать QR-код"<br>
                4. Отсканируйте код</p>
            </div>

            <div style='margin-top: 25px;'>
                <table style='margin: 0 0 20px 0; text-align: left; border-spacing: 0; border-collapse: collapse;'>
                    <tr>
                        <td style='padding: 1px 3px 1px 0;'><b>Версия:</b></td>
                        <td style='padding: 1px 15;'>1.4</td>
                    </tr>
                    <tr>
                        <td style='padding: 1px 3px 1px 0;'><b>Автор:</b></td>
                        <td style='padding: 1px 15;'>MacTep Yoba</td>
                    </tr>
                    <tr>
                        <td style='padding: 1px 3px 1px 0;'><b>Год:</b></td>
                        <td style='padding: 1px 15;'>2026</td>
                    </tr>
                </table>
            </div>
        </div>
        """

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("О программе")
        msg_box.setTextFormat(Qt.RichText)
        msg_box.setText(info_text)
        msg_box.setIcon(QMessageBox.NoIcon)
        msg_box.setStandardButtons(QMessageBox.Ok)

        msg_box.setMinimumSize(800, 800)

        icon_path = Path(__file__).parent / 'icon' / 'icon.ico'
        if icon_path.exists():
            msg_box.setWindowIcon(QIcon(str(icon_path)))

        msg_box.exec_()

def main():
    app = QApplication(sys.argv)
    window = AmneziaWGConfigurator()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()