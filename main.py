"""
Main Driver Code for SSGPlus
"""
# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 0.0.1
# ///////////////////////////////////////////////////////////////
# Developed by Leighton Brooks (enigmapr0ject)
import base64
import ntpath
import os
import platform
import sys
import time
import requests
import webbrowser
from threading import *
from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtWidgets import QMainWindow
from modules import *
from PySide6.QtCore import *
import traceback
from hashlib import sha256

# warnings.filterwarnings('ignore')
# os.environ['QT_DEBUG_PLUGINS'] = "1"
# FIX Problem for High DPI and Scale above 100%
# Check for High DPI or Scale above 100%, and set os.environ["QT_FONT_DPI"] accordingly
if platform.system() == "Windows":
    import ctypes

    if ctypes.windll.shcore.GetScaleFactorForDevice(0) > 100:
        os.environ["QT_FONT_DPI"] = str(ctypes.windll.shcore.GetScaleFactorForDevice(0) * 96 / 72)
    else:
        os.environ["QT_FONT_DPI"] = "96"
title = "SSGPlus"


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    '''
    finished = Signal()  # QtCore.Signal
    error = Signal(tuple)
    result = Signal(object)
    started = Signal()


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()  # QtCore.Slot
    def run(self):
        """
        Initialise the runner function with passed args, kwargs.
        """
        self.signals.started.emit()

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

class MyStream(QtCore.QObject):
    message = Signal(str)
    def __init__(self, parent=None):
        super(MyStream, self).__init__(parent)

    def write(self, message):
        self.message.emit(str(message))

    def flush(self):
        # Flush stdout
        pass

class MainWindow(QMainWindow):
    """
    Dashboard
    """
    predictionFinished = Signal()
    def __init__(self, model):
        # Call to QMainWindow as super
        super(MainWindow, self).__init__()
        self.__predictionThread = None
        self.predictionFinished.connect(self.predictionFinishedSlot)
        self.__predicted_image = None
        self.__mapname = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        widgets = self.ui
        self.__rt: RepeatedTimer | None = None
        self.dragPos = None
        self.__threadpool = QThreadPool()
        self.__model = model
        Settings.ENABLE_CUSTOM_TITLE_BAR = titleBarFlag
        # APPLY TEXTS
        self.setWindowTitle(title)
        self.ui.predict.setEnabled(False)
        self.ui.selectMap.clicked.connect(self.selectMap)
        self.ui.predict.clicked.connect(self.predictionThread)

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # BUTTONS CLICK
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.closeAppBtn.clicked.connect(self.buttonClick)

        self.leftMenuShadowLower = QtWidgets.QGraphicsDropShadowEffect()
        self.leftMenuShadowLower.setBlurRadius(5)
        self.leftMenuShadowLower.setXOffset(2)
        self.leftMenuShadowLower.setYOffset(0)
        self.leftMenuShadowLower.setColor(QtGui.QColor(0, 0, 0, 50))
        self.ui.leftMenuBg.setGraphicsEffect(self.leftMenuShadowLower)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            """
            Open/Close Extra Left Box
            :return:
            """
            UIFunctions.toggleLeftBox(self, True)

        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            """
            Open/Close Extra Right Box
            :return:
            """
            UIFunctions.toggleRightBox(self, True)

        # Theme hack
        theme = "themes/SSGPlus.qss"
        UIFunctions.theme(self, theme, True)

        # SHOW APP
        self.show()
        # widgets.btn_more.clicked.connect(self.buttonClick)
        self.ui.titleLeftDescription.setText("Dashboard")

        self.closeAppBtnShadow = QtWidgets.QGraphicsDropShadowEffect()
        self.closeAppBtnShadow.setBlurRadius(22)
        self.closeAppBtnShadow.setXOffset(0)
        self.closeAppBtnShadow.setYOffset(0)
        self.closeAppBtnShadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.ui.closeAppBtn.setGraphicsEffect(self.closeAppBtnShadow)

        self.maximizeRestoreAppBtnShadow = QtWidgets.QGraphicsDropShadowEffect()
        self.maximizeRestoreAppBtnShadow.setBlurRadius(22)
        self.maximizeRestoreAppBtnShadow.setXOffset(0)
        self.maximizeRestoreAppBtnShadow.setYOffset(0)
        self.maximizeRestoreAppBtnShadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.ui.maximizeRestoreAppBtn.setGraphicsEffect(self.maximizeRestoreAppBtnShadow)

        self.minimizeAppBtnShadow = QtWidgets.QGraphicsDropShadowEffect()
        self.minimizeAppBtnShadow.setBlurRadius(22)
        self.minimizeAppBtnShadow.setXOffset(0)
        self.minimizeAppBtnShadow.setYOffset(0)
        self.minimizeAppBtnShadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.ui.minimizeAppBtn.setGraphicsEffect(self.minimizeAppBtnShadow)

        self.authorLabelShadow = QtWidgets.QGraphicsDropShadowEffect()
        self.authorLabelShadow.setBlurRadius(22)
        self.authorLabelShadow.setXOffset(0)
        self.authorLabelShadow.setYOffset(0)
        self.authorLabelShadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.ui.creditsLabel.setGraphicsEffect(self.authorLabelShadow)

        self.versionLabelShadow = QtWidgets.QGraphicsDropShadowEffect()
        self.versionLabelShadow.setBlurRadius(22)
        self.versionLabelShadow.setXOffset(0)
        self.versionLabelShadow.setYOffset(0)
        self.versionLabelShadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.ui.version.setGraphicsEffect(self.versionLabelShadow)

        self.titleShadow = QtWidgets.QGraphicsDropShadowEffect()
        self.titleShadow.setBlurRadius(22)
        self.titleShadow.setXOffset(0)
        self.titleShadow.setYOffset(0)
        self.titleShadow.setColor(QtGui.QColor(0, 0, 0, 150))
        self.ui.dashboardTitle.setGraphicsEffect(self.titleShadow)


        self.titleLeftAppShadow = QtWidgets.QGraphicsDropShadowEffect()
        self.titleLeftAppShadow.setBlurRadius(22)
        self.titleLeftAppShadow.setXOffset(0)
        self.titleLeftAppShadow.setYOffset(0)
        self.titleLeftAppShadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.ui.titleLeftApp.setGraphicsEffect(self.titleLeftAppShadow)

        self.titleLeftDescriptionShadow = QtWidgets.QGraphicsDropShadowEffect()
        self.titleLeftDescriptionShadow.setBlurRadius(22)
        self.titleLeftDescriptionShadow.setXOffset(0)
        self.titleLeftDescriptionShadow.setYOffset(0)
        self.titleLeftDescriptionShadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.ui.titleLeftDescription.setGraphicsEffect(self.titleLeftDescriptionShadow)

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(
            UIFunctions.selectMenu(
                widgets.btn_home.styleSheet()))

        # Home Screen
        self.ui.credits.hide()
        self.ui.predictionstdout.hide()
        self.ui.predictionOutputTitle.hide()
        self.ui.selectMap_2.hide()

        self.ui.tensorflowVersion.setText(" " + str(tf.__version__))
        self.ui.cpuName.setText(f"CPU: {self.get_processor_name()}")
        self.ui.gpuName.setText(f"GPU: {GPUtil.getGPUs()[0].name}")


        def extract_release_version(output):
            pattern = r"release (\d+\.\d+)"
            match = re.search(pattern, output)
            if match:
                return match.group(1)
            return None

        # Run the `nvcc --version` command and capture the output
        cudaOutput = subprocess.check_output(["nvcc", "--version"], universal_newlines=True)

        # Extract the release version number
        cudaVersion = extract_release_version(cudaOutput)
        # If this is not a float or integer, then its not installed
        try:
            float(cudaVersion)
        except TypeError:
            cudaVersion = "Not Detected"
        self.ui.cudaDetected.setText(f"CUDA: {cudaVersion}")
        self.ui.cudnnDetected.setText(f"CUDNN: {self.getCUDNNversion()}")

        hash = sha256("dDhAI4aDx7tqJmqXwhLn".encode()).hexdigest()
        headers = {"Authorization": f"Bearer {hash}"}
        r2 = requests.get("https://api.enigmapr0ject.tech/ssgplus/modelVersion", headers=headers)
        if r2.status_code == 200:
            self.ui.modelVersion.setText(r2.json()['version'])
        else:
            self.ui.modelVersion.setText("Unknown")

        self.ui.selectMap_2.clicked.connect(self.openPredictionMap)


    def predictionThread(self):
        self.ui.predictionstdout.clear()
        self.ui.predictionstdout.show()
        self.ui.predictionOutputTitle.show()
        self.__predictionThread = Thread(target=self.predictNew, args=())
        self.__predictionThread.start()

    def predictionFinishedSlot(self):
        if self.__count != 0:
            self.ui.predictionOutput.setStyleSheet("color: #2aa14d;")
            self.ui.selectMap_2.setStyleSheet("""
            #selectMap_2{
                background-color: qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));
                font: 300 10pt "Inter Light";
                }
                #selectMap_2::pressed {
                background-color: qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 180), stop:1 rgba(170, 85, 255, 180));
                font: 300 10pt "Inter Light";
                }
            """)
            self.ui.selectMap_2.setEnabled(True)
            self.ui.selectMap_2.show()
        else:
            self.ui.predictionOutput.setStyleSheet("color: #ff0000;")
            self.ui.selectMap_2.setStyleSheet("""
            #selectMap_2{
            background-color: rgb(184, 184, 184);
            }
            """)
            self.ui.selectMap_2.setEnabled(False)
            self.ui.selectMap_2.hide()
        self.ui.predictionOutput.setText(f"{str(self.__count)} predictions.")
        self.ui.predictionstdout.appendPlainText(f"{str(self.__count)} predictions.\nMap: {self.__mapname}\nTime taken: {str(self.__time_taken)} seconds.\nTrained against {str(self.__number_of_datapoints)} datapoints.")
        # Show the final image with the matched area.

    def openPredictionMap(self):
        # Open a new window with just the image
        self.predictionMapWindow = QtWidgets.QMainWindow()
        centralImage = QtWidgets.QLabel(self.predictionMapWindow)
        # Predicted image is an RGB output from CV
        image = self.__predicted_image
        height, width, channels = image.shape
        bytes_per_line = channels * width
        qimage = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        qpixmap = QPixmap.fromImage(qimage)
        centralImage.setPixmap(QtGui.QPixmap(qpixmap))
        self.predictionMapWindow.setCentralWidget(centralImage)
        # Set title and icon
        self.predictionMapWindow.setWindowTitle("Prediction Map: " + self.__mapname)
        icon = QIcon()
        icon.addFile(u":/images/ssg+.png", QSize(), QIcon.Normal, QIcon.Off)
        self.predictionMapWindow.setWindowIcon(icon)
        self.predictionMapWindow.show()

    def getCUDNNversion(self):
        return torch.backends.cudnn.version()

    def get_processor_name(self):
        if platform.system() == "Windows":
            return platform.processor()
        elif platform.system() == "Darwin":
            os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
            command = "sysctl -n machdep.cpu.brand_string"
            return subprocess.check_output(command).strip()
        elif platform.system() == "Linux":
            command = "cat /proc/cpuinfo"
            all_info = subprocess.check_output(command, shell=True).decode().strip()
            for line in all_info.split("\n"):
                if "model name" in line:
                    return re.sub(".*model name.*:", "", line, 1)
        return ""

    def predictNew(self):
        # Instead of printing to console, dump to file
        stream = MyStream()
        stream.message.connect(self.ui.predictionstdout.appendPlainText)
        sys.stdout = stream
        start = time.time()
        test_dir = os.getcwd() + "/data/validation/"
        test_data = tf.keras.preprocessing.image_dataset_from_directory(test_dir, image_size=(224, 224), batch_size=12)
        # Get the number of images we are using for the test data
        self.__number_of_datapoints = test_data.cardinality().numpy()
        class_names = test_data.class_names
        img_rgb = cv2.imread(self.__mapname)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        signal_to_compare = os.getcwd() + "/templates/original.png"
        signal_to_compare_90_clockwise = os.getcwd() + "/templates/rotate_right.png"
        signal_to_compare_180_clockwise = os.getcwd() + "/templates/rotate_180.png"
        signal_to_compare_270_clockwise = os.getcwd() + "/templates/rotate_left.png"

        PC = os.getcwd() + "/templates/PC_original.png"
        PC_90_clockwise = os.getcwd() + "/templates/PC_rotate_right.png"
        PC_180_clockwise = os.getcwd() + "/templates/PC_rotate_180.png"
        PC_270_clockwise = os.getcwd() + "/templates/PC_rotate_left.png"

        # Initialize the list of templates and their corresponding labels
        templates = []
        labels = []

        # Load the 4 templates and their labels
        template_paths = [signal_to_compare, signal_to_compare_90_clockwise, signal_to_compare_180_clockwise,
                          signal_to_compare_270_clockwise
            , PC, PC_90_clockwise, PC_180_clockwise, PC_270_clockwise]
        template_labels = ["normal", "rotated 90 clockwise", "rotated 180 clockwise", "rotated 270 clockwise", "PC",
                           "PC rotated 90 clockwise", "PC rotated 180 clockwise", "PC rotated 270 clockwise"]
        for template_path, template_label in zip(template_paths, template_labels):
            template = cv2.cvtColor(cv2.imread(template_path), cv2.COLOR_BGR2GRAY)
            templates.append(template)
            labels.append(template_label)

        # Set the threshold for matching
        threshold = 0.8

        # Initialize the count of detected signals
        count = 0

        # Initialize the mask for marking already detected regions
        mask = np.zeros(img_rgb.shape[:2], np.uint8)

        # Loop over each template and match it with the image
        for template, label in zip(templates, labels):
            # Get the shape of the template
            w, h = template.shape[::-1]
            # Match the template with the image
            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            # Get the locations where the template matches the image with a confidence above the threshold
            loc = np.where(res >= threshold)
            # Loop over each location and draw a rectangle around the matched region
            for pt in zip(*loc[::-1]):
                # Check if the region has already been detected
                if mask[pt[1] + int(round(h / 2)), pt[0] + int(round(w / 2))] != 255:
                    # Mark the region as detected
                    mask[pt[1]:pt[1] + h, pt[0]:pt[0] + w] = 255
                    # Resize the matched region to 224x224 pixels
                    resized = cv2.resize(img_rgb[pt[1]:pt[1] + h, pt[0]:pt[0] + w], (224, 224))
                    # Check if the resized region has the correct dimensions
                    if resized.shape[0] != 224 or resized.shape[1] != 224:
                        continue
                    # Draw a rectangle around the matched region on the original image
                    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
                    # Save the resized image to a file
                    random = np.random.randint(0, 100000)
                    cv2.imwrite('Detected' + str(random) + '.png', resized)
                    # Load the image file and convert it to a numpy array
                    img = tf.keras.preprocessing.image.load_img(os.getcwd() + "/Detected" + str(random) + ".png",
                                                                target_size=(224, 224))
                    img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0
                    img_array = tf.expand_dims(img_array, 0)
                    # Predict the class of the image
                    predictions = self.__model.predict(img_array)
                    # Get the predicted class name
                    predicted_class = class_names[np.argmax(predictions[0])]
                    # Map the predicted class name to a shorthand label
                    match predicted_class:
                        case "danger":
                            label = "D"
                        case "preliminary_caution":
                            label = "PC"
                        case "caution":
                            label = "C"
                        case "proceed":
                            label = "P"
                    # Label it on the image
                    cv2.putText(img_rgb, label, (pt[0], pt[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                                (0, 255, 255), 2)
                    count += 1
                    os.remove(os.getcwd() + "/Detected" + str(random) + ".png")
                else:
                    continue
        end = time.time()
        self.__time_taken = round(end - start, 2)
        self.__count = count
        self.__predicted_image = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
        self.predictionFinished.emit()

    def selectMap(self):
        def path_leaf(path):
            head, tail = ntpath.split(path)
            # Return the file name, not the whole path
            return tail or ntpath.basename(head)
        # Open file browser
        filename = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.png)")
        if filename[0] != "":
            self.__mapname = filename[0]
            self.ui.mapSelected.setText("Map: " + path_leaf(filename[0]) if len(path_leaf(filename[0])) < 15 else path_leaf(filename[0])[:20] + "...")
            self.ui.mapSelected.setStyleSheet("color: #2aa14d;")
            self.ui.predict.setEnabled(True)
            self.ui.predict.setStyleSheet("""
            #predict {
                background-color: qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));
                font: 300 10pt "Inter Light";
                }
                #predict::pressed {
                background-color: qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 180), stop:1 rgba(170, 85, 255, 180));
                font: 300 10pt "Inter Light";
                }
            """)
            self.ui.predict.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        else:
            self.ui.mapSelected.setText("Map not selected.")
            self.ui.mapSelected.setStyleSheet("color: #ff0000;")
            self.ui.predict.setEnabled(False)
            self.ui.predict.setStyleSheet("""
            #predict {
                background-color: rgb(184, 184, 184);
                font: 300 10pt "Inter Light";
                }
            """)
            self.ui.predictionstdout.hide()
            self.ui.predictionOutputTitle.hide()
            self.ui.selectMap_2.hide()

    def result(self):  # Connector is blank, used solely for connecting from the Worker.
        pass

    # BUTTON CLICK
    def buttonClick(self):
        """
        Button Click event handler
        :return:
        """
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        match btnName:
            # SHOW NEW PAGE
            case "closeAppBtn":
                try:
                    self.__rt.stop()
                    self.close()
                    sys.exit(0)
                except AttributeError:
                    self.close()
                    sys.exit(0)
            case "btn_home":
                # self.ui.titleLeftDescription.setText("Dashboard")  # SET PAGE
                self.ui.stackedWidget.setCurrentWidget(
                    self.ui.home)  # RESET ANOTHERS BUTTONS SELECTED
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(
                    UIFunctions.selectMenu(
                        btn.styleSheet()))  # SELECT MENU
                self.ui.titleLeftDescription.setText("Dashboard")
            case "btn_credits":
                # Check if the credits are already showing
                if self.ui.credits.isHidden():
                    self.ui.credits.show()
                else:
                    self.ui.credits.hide()
            case "btn_help":
                webbrowser.get().open("https://enigmapr0ject.tech/ssgplus")
            case "btn_report":
                webbrowser.get().open("https://github.com/enigmapr0ject/SSGPlus/issues/new/choose")
            case "btn_more":
                webbrowser.get().open("https://enigmapr0ject.tech/")

    # RESIZE EVENTS
    def resizeEvent(self, event):
        """
        Resize event
        :param event:
        :return:
        """
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        """
        Mouse press event
        :param event:
        :return:
        """
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()


class SplashScreen(QMainWindow):
    startAnimation = Signal()
    openMain = Signal()
    failedToStartSignal = Signal()
    def __init__(self):
        QMainWindow.__init__(self)
        self.__decrypted_data = None
        self.__modelfile = None
        self.__modeltouse = None
        self.mainWindow = None
        self.__cipher = None
        self.__key = None
        self.__modelcheck = None
        self.mainThread = None
        self.threadpool = QThreadPool()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.counter = 0
        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        self.ui.progressBar.setValue(self.counter)
        self.fadeinEffect = QGraphicsOpacityEffect(self, opacity=0.99)
        self.ui.label_loading.setGraphicsEffect(self.fadeinEffect)
        # Disable the effect for now
        self.animation = QPropertyAnimation(self.fadeinEffect, b"opacity")
        self.animation.setDuration(1000)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(0.99)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO SSGPlus")

        self.ui.selectMap.hide()
        self.ui.selectMap.clicked.connect(lambda: sys.exit(-1))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

        ## ==> APP FUNCTIONS
        ########################################################################
        # App Loading with Progress bar after each step
        self.ui.label_loading.setText("<strong>Importing</strong> libraries...")
        # Import tensorflow on a separate thread, and then update progress bar once it completes
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: self.progress(self.loadModel))
        self.timer.start(35)
        self.import_thread = Thread(target=self.imports)
        self.import_thread.start()

    def failedToStart(self):
        self.ui.selectMap.show()

    def fadeIn(self):
        def loadMain():
            self.mainThread = Thread(target=self.triggerMainSignal)
            self.mainThread.start()
            self.close()
        self.ui.progressBar.hide()
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(0.99)
        self.animation.start()
        self.animation.finished.connect(loadMain)

    def openMainWindow(self):
        time.sleep(1)
        self.mainWindow = MainWindow(self.__modeltouse)
        self.mainWindow.show()
        self.close()

    def triggerMainSignal(self):
        self.openMain.emit()

    def progress(self, whereNext):
        self.ui.progressBar.setValue(self.counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if self.import_thread.is_alive() is False:
            # STOP TIMER
            self.timer.stop()
            self.counter = 0
            whereNext()
        else:
            self.counter += 1 if self.counter < 40 else 0

    def imports(self):
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
        import tensorflow as tf
        import numpy as np
        from Cryptodome.Cipher import AES
        from Cryptodome.Util.Padding import unpad
        import cv2
        import io
        import h5py
        import psutil
        import subprocess
        import re
        import torch
        import GPUtil
        global tf, np, AES, unpad, cv2, io, h5py, psutil, subprocess, re, torch, GPUtil

    def decrypt(self):
        self.__key = "2FNJh1Yyii88G0jNFKLJR9yNjVQn7nm6"
        self.__cipher = AES.new(self.__key.encode(), AES.MODE_ECB)
        contents = open("model.h5", "rb").read()
        encrypted_data = base64.b64decode(contents)
        # Unpad the data
        decrypted_data = unpad(self.__cipher.decrypt(encrypted_data), AES.block_size)
        self.__decrypted_data = decrypted_data
        for i in range(61, 70):
            self.ui.progressBar.setValue(i)
            time.sleep(0.1)
        # Write the decrypted data to the file
        self.__modelfile = io.BytesIO(decrypted_data)
        for i in range(71, 80):
            self.ui.progressBar.setValue(i)
            time.sleep(0.1)
        self.kerasLoadModel()

    def initializeModel(self):
        try:
            os.remove(os.getcwd() + '/model.h5')
            self.__modeltouse = tf.keras.models.load_model(h5py.File(self.__modelfile, 'r'))
            for i in range(81, 101):
                self.ui.progressBar.setValue(i)
                time.sleep(0.1)
            self.startup()
        except Exception as e:
            print(repr(e))

    def downloadModel(self):
        hash = sha256("dDhAI4aDx7tqJmqXwhLn".encode()).hexdigest()
        headers = {"Authorization": f"Bearer {hash}"}
        try:
            r = requests.get("https://api.enigmapr0ject.tech/ssgplus/model", headers=headers, stream=True)
            if r.status_code == 200:
                total_size = int(r.headers.get('content-length', 0))
                with open("model.h5", 'wb') as file:
                    for chunk in r.iter_content(chunk_size=131072):
                        if chunk:
                            file.write(chunk)
                            percentageProgress = int(100 * ((file.tell() / total_size) * 0.2)) + 40
                            self.ui.progressBar.setValue(percentageProgress)
                self.decryptModel()
        except ConnectionError:
            pass
        except TimeoutError:
            pass
        except requests.exceptions.RequestException:
            pass

    def loadModel(self):
        self.ui.label_loading.setText("<strong>Downloading</strong> model...")
        self.download_thread = Thread(target=self.downloadModel)
        self.download_thread.start()

    def decryptModel(self):
        self.ui.label_loading.setText("<strong>Decrypting</strong> model...")
        self.decrypt_thread = Thread(target=self.decrypt)
        self.decrypt_thread.start()

    def kerasLoadModel(self):
        self.ui.label_loading.setText("<strong>Initialising</strong> model...")
        self.initialize_thread = Thread(target=self.initializeModel)
        self.initialize_thread.start()

    def startup(self):
        # Compare the model to the original
        original_model_sum = "51bc6b3e27bf471bef6223c61d5f37fe5df4f628ac34a0537f05d08aab8d40a9"
        decrypted_model_sum = sha256(self.__decrypted_data).hexdigest()
        if original_model_sum == decrypted_model_sum:
            self.__modelcheck = True
            self.ui.label_loading.setText("<strong>Verified.</strong> Starting SSGPlus...")
            self.ui.label_loading.setStyleSheet("color: #00cc30; font: 300 10pt \"Inter Light\";")
            time.sleep(2)
            self.startAnimation.emit()
        else:
            self.__modelcheck = False
            self.ui.label_loading.setText("<strong>Error occurred.</strong> Could not start SSGPlus.")
            self.ui.label_loading.setStyleSheet("color: #cc0000; font: 300 10pt \"Inter Light\";")
            # Place an exit button udnerneath
            self.failedToStartSignal.emit()




if __name__ == "__main__":
    # faulthandler.enable()
    match platform.system():  # Check the OS
        case "Windows":  # If Windows
            import ctypes  # Windows exclusive library

            # arbitrary string, can be anything
            myappid = 'theenigmaproject.ai.ssgplus.001'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
                myappid)  # Set the AppID. Needed for
            # taskbar icon and window icons to work.
            # Variable holding the value for if we have a custom titlebar or
            # not. This is broken
            titleBarFlag = True
            # on any other OS.
        case other:
            titleBarFlag = False
    app = QApplication(sys.argv)
    window = SplashScreen()
    window.startAnimation.connect(window.fadeIn)
    window.openMain.connect(window.openMainWindow)
    window.failedToStartSignal.connect(window.failedToStart)
    sys.exit(app.exec())
