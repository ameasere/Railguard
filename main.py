"""
Main Driver Code for Railguard
"""
# ///////////////////////////////////////////////////////////////
#
# Template by WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 0.0.1
# ///////////////////////////////////////////////////////////////
# Developed by ameasere
import base64
import ntpath
import os
import platform
import random
import sys
import time
import requests
import webbrowser
from threading import *
from modules import *
import traceback
import sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import numpy as np
import cv2
import h5py
import psutil
import subprocess
import re
import GPUtil

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
title = "Railguard"


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
    finished = Signal()  # Signal
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

    @Slot()  # Slot
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


class MyStream(QObject):
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
        self.ui.titleLeftApp.setText("Railguard")
        self.__rt: RepeatedTimer = None
        self.dragPos = None
        self.__threadpool = QThreadPool()
        self.__model = model
        Settings.ENABLE_CUSTOM_TITLE_BAR = titleBarFlag
        # APPLY TEXTS
        self.setWindowTitle(title)
        #self.ui.predict.setEnabled(False)
        #self.ui.selectMap.clicked.connect(self.selectMap)
        #self.ui.predict.clicked.connect(self.predictionThread)
        self.setFixedSize(self.width(), self.height())

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # BUTTONS CLICK
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_dashboard.clicked.connect(self.buttonClick)
        widgets.btn_credits.clicked.connect(self.buttonClick)
        widgets.closeAppBtn.clicked.connect(self.buttonClick)

        self.leftMenuShadowLower = QGraphicsDropShadowEffect()
        self.leftMenuShadowLower.setBlurRadius(5)
        self.leftMenuShadowLower.setXOffset(2)
        self.leftMenuShadowLower.setYOffset(0)
        self.leftMenuShadowLower.setColor(QColor(0, 0, 0, 50))
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

        # SHOW APP
        self.show()
        # widgets.btn_more.clicked.connect(self.buttonClick)
        self.ui.titleLeftDescription.setText("Dashboard")

        self.closeAppBtnShadow = QGraphicsDropShadowEffect()
        self.closeAppBtnShadow.setBlurRadius(22)
        self.closeAppBtnShadow.setXOffset(0)
        self.closeAppBtnShadow.setYOffset(0)
        self.closeAppBtnShadow.setColor(QColor(255, 255, 255, 90))
        self.ui.closeAppBtn.setGraphicsEffect(self.closeAppBtnShadow)

        self.maximizeRestoreAppBtnShadow = QGraphicsDropShadowEffect()
        self.maximizeRestoreAppBtnShadow.setBlurRadius(22)
        self.maximizeRestoreAppBtnShadow.setXOffset(0)
        self.maximizeRestoreAppBtnShadow.setYOffset(0)
        self.maximizeRestoreAppBtnShadow.setColor(QColor(255, 255, 255, 90))
        self.ui.maximizeRestoreAppBtn.setGraphicsEffect(self.maximizeRestoreAppBtnShadow)

        self.minimizeAppBtnShadow = QGraphicsDropShadowEffect()
        self.minimizeAppBtnShadow.setBlurRadius(22)
        self.minimizeAppBtnShadow.setXOffset(0)
        self.minimizeAppBtnShadow.setYOffset(0)
        self.minimizeAppBtnShadow.setColor(QColor(255, 255, 255, 90))
        self.ui.minimizeAppBtn.setGraphicsEffect(self.minimizeAppBtnShadow)

        self.modelTitleShadow = QGraphicsDropShadowEffect()
        self.modelTitleShadow.setBlurRadius(22)
        self.modelTitleShadow.setXOffset(0)
        self.modelTitleShadow.setYOffset(0)
        self.modelTitleShadow.setColor(QColor(255, 255, 255, 90))
        self.ui.modeltitle.setGraphicsEffect(self.modelTitleShadow)

        self.titleLeftAppShadow = QGraphicsDropShadowEffect()
        self.titleLeftAppShadow.setBlurRadius(22)
        self.titleLeftAppShadow.setXOffset(0)
        self.titleLeftAppShadow.setYOffset(0)
        self.titleLeftAppShadow.setColor(QColor(0, 0, 0, 60))
        self.ui.titleLeftApp.setGraphicsEffect(self.titleLeftAppShadow)

        self.titleLeftDescriptionShadow = QGraphicsDropShadowEffect()
        self.titleLeftDescriptionShadow.setBlurRadius(22)
        self.titleLeftDescriptionShadow.setXOffset(0)
        self.titleLeftDescriptionShadow.setYOffset(0)
        self.titleLeftDescriptionShadow.setColor(QColor(0, 0, 0, 60))
        self.ui.titleLeftDescription.setGraphicsEffect(self.titleLeftDescriptionShadow)

        self.cudaTitleShadow = QGraphicsDropShadowEffect()
        self.cudaTitleShadow.setBlurRadius(22)
        self.cudaTitleShadow.setXOffset(0)
        self.cudaTitleShadow.setYOffset(0)
        self.cudaTitleShadow.setColor(QColor(255, 255, 255, 90))
        self.ui.cudatitle.setGraphicsEffect(self.cudaTitleShadow)

        self.cudnnTitleShadow = QGraphicsDropShadowEffect()
        self.cudnnTitleShadow.setBlurRadius(22)
        self.cudnnTitleShadow.setXOffset(0)
        self.cudnnTitleShadow.setYOffset(0)
        self.cudnnTitleShadow.setColor(QColor(255, 255, 255, 90))
        self.ui.cudnntitle.setGraphicsEffect(self.cudnnTitleShadow)

        self.cpuTitleShadow = QGraphicsDropShadowEffect()
        self.cpuTitleShadow.setBlurRadius(22)
        self.cpuTitleShadow.setXOffset(0)
        self.cpuTitleShadow.setYOffset(0)
        self.cpuTitleShadow.setColor(QColor(255, 255, 255, 90))
        self.ui.cputitle.setGraphicsEffect(self.cpuTitleShadow)

        self.gpuTitleShadow = QGraphicsDropShadowEffect()
        self.gpuTitleShadow.setBlurRadius(22)
        self.gpuTitleShadow.setXOffset(0)
        self.gpuTitleShadow.setYOffset(0)
        self.gpuTitleShadow.setColor(QColor(255, 255, 255, 90))
        self.ui.gputitle.setGraphicsEffect(self.gpuTitleShadow)

        self.ramTitleShadow = QGraphicsDropShadowEffect()
        self.ramTitleShadow.setBlurRadius(22)
        self.ramTitleShadow.setXOffset(0)
        self.ramTitleShadow.setYOffset(0)
        self.ramTitleShadow.setColor(QColor(255, 255, 255, 90))
        self.ui.ramtitle.setGraphicsEffect(self.ramTitleShadow)

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(
            UIFunctions.selectMenu(
                widgets.btn_home.styleSheet()))

        # Home Screen
        self.ui.credits.hide()
        self.ui.cpuName.setText(f"{self.get_processor_name()}")
        self.ui.gpuName.setText(f"{GPUtil.getGPUs()[0].name}")
        import wmi
        c = wmi.WMI()
        memory_info = c.Win32_PhysicalMemory()
        ram_speed = None
        for memory in memory_info:
            if memory.Speed:
                ram_speed = memory.Speed
        if ram_speed is None:
            ram_speed = "Unknown"
        memory_info = None
        c = None
        self.ui.ramName.setText(f"{str(round(psutil.virtual_memory().total / (1024.0 ** 3)))} GB @ {ram_speed} MHz")

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
        # End the subprocess
        cudaOutput = None
        # If this is not a float or integer, then its not installed
        try:
            float(cudaVersion)
        except TypeError:
            cudaVersion = "Not Detected"
        self.ui.cudaDetected.setText(f"{cudaVersion}")
        self.ui.cudnnDetected.setText(f"{self.getCUDNNversion()}")
        self.ui.modelVersion.setText("0.0.4")

    def predictionThread(self):
        self.__predictionThread = Thread(target=self.predictNew, args=())
        self.__predictionThread.start()

    def predictionFinishedSlot(self):
        if self.__count != 0:
            pass
        else:
            pass
            # appendPlainText(
            # f"{str(self.__count)} predictions.\nMap: {self.__mapname}\nTime taken: {str(self.__time_taken)} seconds.\nTrained against {str(self.__number_of_datapoints)} datapoints.")
        # Show the final image with the matched area.

    def openPredictionMap(self):
        pass

    def getCUDNNversion(self):
        return "Not Detected"

    def get_processor_name(self):
        if platform.system() == "Windows":
            import cpuinfo
            return cpuinfo.get_cpu_info()['brand_raw']
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

        normal_rotated_45 = os.getcwd() + "/templates/normal_rotated_45_degrees.jpg"
        normal_rotated_135 = os.getcwd() + "/templates/normal_rotated_135_degrees.jpg"
        normal_rotated_225 = os.getcwd() + "/templates/normal_rotated_225_degrees.jpg"
        normal_rotated_315 = os.getcwd() + "/templates/normal_rotated_315_degrees.jpg"

        pc_rotated_45 = os.getcwd() + "/templates/pc_rotated_45_degrees.jpg"
        pc_rotated_135 = os.getcwd() + "/templates/pc_rotated_135_degrees.jpg"
        pc_rotated_225 = os.getcwd() + "/templates/pc_rotated_225_degrees.jpg"
        pc_rotated_315 = os.getcwd() + "/templates/pc_rotated_315_degrees.jpg"

        # Initialize the list of templates and their corresponding labels
        templates = []
        labels = []

        # Load the 4 templates and their labels
        template_paths = [signal_to_compare, signal_to_compare_90_clockwise, signal_to_compare_180_clockwise,
                          signal_to_compare_270_clockwise
            , PC, PC_90_clockwise, PC_180_clockwise, PC_270_clockwise, normal_rotated_45, normal_rotated_135,
                          normal_rotated_225, normal_rotated_315, pc_rotated_45, pc_rotated_135, pc_rotated_225,
                          pc_rotated_315]
        template_labels = ["normal", "rotated 90 clockwise", "rotated 180 clockwise", "rotated 270 clockwise", "PC",
                           "PC rotated 90 clockwise", "PC rotated 180 clockwise", "PC rotated 270 clockwise",
                           "normal rotated 45 degrees",
                           "normal rotated 135 degrees", "normal rotated 225 degrees", "normal rotated 315 degrees",
                           "PC rotated 45 degrees",
                           "PC rotated 135 degrees", "PC rotated 225 degrees", "PC rotated 315 degrees"]
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
                    if predicted_class == "danger":
                        label = "D"
                    elif predicted_class == "preliminary_caution":
                        label = "PC"
                    elif predicted_class == "caution":
                        label = "C"
                    elif predicted_class == "proceed":
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
        pass

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
        if btnName == "closeAppBtn":
            try:
                self.__rt.stop()
                self.close()
                sys.exit(0)
            except AttributeError:
                self.close()
                sys.exit(0)
        elif btnName == "btn_home":
            # self.ui.titleLeftDescription.setText("Dashboard")  # SET PAGE
            self.ui.stackedWidget.setCurrentWidget(
                self.ui.home)  # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(
                UIFunctions.selectMenu(
                    btn.styleSheet()))  # SELECT MENU
            self.ui.titleLeftDescription.setText("Home")
        elif btnName == "btn_dashboard":
            self.ui.stackedWidget.setCurrentWidget(
                self.ui.dashboard)  # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(
                UIFunctions.selectMenu(
                    btn.styleSheet()))  # SELECT MENU
            self.ui.titleLeftDescription.setText("Dashboard")
        elif btnName == "btn_credits":
            # Check if the credits are already showing
            if self.ui.credits.isHidden():
                self.ui.credits.show()
            else:
                self.ui.credits.hide()
        elif btnName == "btn_help":
            webbrowser.get().open("https://ameasere.com/railguard")
        elif btnName == "btn_report":
            webbrowser.get().open("https://github.com/ameasere/Railguard/issues/new/choose")
        elif btnName == "btn_more":
            webbrowser.get().open("https://ameasere.com/")

    def resizeEvent(self, event):
        pass

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

    def __init__(self):
        QMainWindow.__init__(self)
        self.__modelfile = os.getcwd() + "/model.h5"
        self.__modeltouse = None
        self.mainWindow = None
        self.mainThread = None
        self.threadpool = QThreadPool()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.counter = 0
        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
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
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)

        # Animation for glowing title
        self.glowEffect = QGraphicsDropShadowEffect(self)
        self.glowEffect.setBlurRadius(20)
        self.glowEffect.setXOffset(0)
        self.glowEffect.setYOffset(0)
        self.glowEffect.setColor(QColor(255, 255, 255, 90))
        self.ui.label_title.setGraphicsEffect(self.glowEffect)

        # Initial Text
        self.ui.label_description.setText("WELCOME TO <strong>RAILGUARD</strong>")
        # Every 3 seconds, change the text
        self.scrolltimer = QTimer()
        self.scrolltimer.timeout.connect(self.updateText)
        self.scrolltimer.start(3000)
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
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.progress(self.kerasLoadModel))
        self.timer.start(20)
        self.import_thread = Thread(target=self.imports)
        self.import_thread.start()

    def updateText(self):
        import random
        random = random.randint(0, 6)
        if random == 0:
            self.ui.label_description.setText("WELCOME TO <strong>RAILGUARD</strong>")
        elif random == 1:
            self.ui.label_description.setText("<strong>SUPERVISED</strong> SIGNALLING")
        elif random == 2:
            self.ui.label_description.setText("POWERED BY <strong>AI</strong>")
        elif random == 3:
            self.ui.label_description.setText("MADE WITH <strong>CUDA & CUDNN</strong>")
        elif random == 4:
            self.ui.label_description.setText("MADE WITH <strong>TENSORFLOW</strong>")
        elif random == 5:
            self.ui.label_description.setText("CROSS-PLATFORM <strong>SUPPORTED</strong>")

    def failedToStart(self):
        self.ui.selectMap.show()

    def fadeIn(self):
        def loadMain():
            self.triggerMainSignal()

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
        pass

    def initializeModel(self):
        try:
            self.__modeltouse = tf.keras.models.load_model(h5py.File(self.__modelfile, 'r'))
            for i in range(40, 101):
                self.ui.progressBar.setValue(i)
                time.sleep(0.1)
            self.startup()
        except Exception as e:
            print(repr(e))

    def kerasLoadModel(self):
        self.ui.label_loading.setText("<strong>Initialising</strong> model...")
        self.initialize_thread = Thread(target=self.initializeModel)
        self.initialize_thread.start()

    def startup(self):
        self.ui.label_loading.setText("Starting Railguard...")
        self.scrolltimer.stop()
        self.scrolltimer.timeout.disconnect()
        self.scrolltimer = None
        self.ui.label_loading.setStyleSheet(
            "font: 450 10pt \"Inter Medium\"; background-color: transparent; color: #04b837;")
        time.sleep(2)
        self.startAnimation.emit()


if __name__ == "__main__":
    # faulthandler.enable()
    if platform.system() == "Windows":  # Check the OS
        import ctypes  # Windows exclusive library

        # arbitrary string, can be anything
        myappid = 'ameasere.ai.railguard.004'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            myappid)  # Set the AppID. Needed for
        # taskbar icon and window icons to work.
        # Variable holding the value for if we have a custom titlebar or
        # not. This is broken
        titleBarFlag = True
        # on any other OS.
    else:
        titleBarFlag = False
    app = QApplication(sys.argv)
    window = SplashScreen()
    window.startAnimation.connect(window.fadeIn)
    window.openMain.connect(window.openMainWindow)
    sys.exit(app.exec())
