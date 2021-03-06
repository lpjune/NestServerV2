from importlib import import_module
import os
import threading
import StringConstants
from flask import Flask
from flasklocal import init_gui
from dotenv import load_dotenv
load_dotenv('.flaskenv')

# Setting up cameras
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera
    
# Creating flask application
videoApp = Flask(__name__)
from videoAppRoutes import * # This has to be here, it can't be moved up to the top
imageApp = Flask(__name__)
from imageAppRoutes import *

# Running application
if __name__ == '__main__':
    init_gui(videoApp, imageApp, ip=StringConstants.SERVER_IP_ADDRESS, port=StringConstants.VIDEO_COMMAND_PORT, port2=StringConstants.IMAGE_PORT, width=700, height=500, window_title="Nest Server", icon="images/appicon.jpg", argv=None)