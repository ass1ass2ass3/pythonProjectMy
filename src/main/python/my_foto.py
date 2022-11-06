"""Usage: view-image <image>"""
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPixmap


class ImageViewer(QWidget):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)

        label = QLabel(self)
        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap)

        self.resize(pixmap.width(), pixmap.height())  # fit window to the image
        self.setWindowTitle('PyQt5 Image Viewer')


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from fbs_runtime.application_context.PyQt5 import ApplicationContext
    apptxt = ApplicationContext()
    im = apptxt.get_resource('images/i.jpg')
    #im = str(input('Введите название файла изображения: '))
    app = QApplication(sys.argv)
    image_viewer = ImageViewer(im)
    image_viewer.show()
    sys.exit(app.exec_())
