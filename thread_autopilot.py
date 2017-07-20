import threading
from PyQt5 import QtGui
from PIL import ImageGrab
import tensorflow as tf
import numpy as np
import scipy.misc
import pygame
import cv2
from database import Settings, Data
import model
import functions


class AutopilotThread(threading.Thread):
    print_lock = threading.Lock()
    running = True

    def __init__(self, controller_thread, steering_wheel, image_front):
        threading.Thread.__init__(self)

        with AutopilotThread.print_lock:
            AutopilotThread.running = True

        pygame.init()
        pygame.joystick.init()

        self.controller_thread = controller_thread
        self.steering_wheel = steering_wheel
        self.image_front = image_front

        self.running = True
        self.country_code = Settings().get_value(Settings.COUNTRY_DEFAULT)
        self.b_autopilot = Settings().get_value(Settings.AUTOPILOT)
        self.steering_axis = Settings().get_value(Settings.STEERING_AXIS)
        self.joystick = pygame.joystick.Joystick(Settings().get_value(Settings.CONTROLLER))
        self.joystick.init()

        self.sess = tf.InteractiveSession()
        saver = tf.train.Saver()
        saver.restore(self.sess, "save/model_%s.ckpt" % self.country_code)

    def stop(self):
        with AutopilotThread.print_lock:
            AutopilotThread.running = False

    def run(self):
        # Settings instance
        s = Settings()
        # State of autopilot
        autopilot = False
        # Previous state of the autopilot button
        autopilot_button_prev = 0
        # Previous value of steering (gamepad)
        manual_steering_prev = 0

        img = cv2.imread('steering_wheel_image.jpg', 0)
        rows, cols = img.shape

        while AutopilotThread.running:
            pygame.event.pump()

            # Button to activate/deactivate autopilot
            autopilot_button_act = self.joystick.get_button(self.b_autopilot)
            # Button was pressed
            if autopilot_button_act != autopilot_button_prev and autopilot_button_act == 1:
                autopilot = not autopilot
                #if autopilot and settings.AUTOPILOT_SOUND_ACTIVATE:
                #    autopilot_engage.play()
            autopilot_button_prev = autopilot_button_act

            # Read the steering value of joystick
            axis = round((self.joystick.get_axis(self.steering_axis) + 1) * 32768 / 2)
            # Interrupt autopilot if manual steering was detected
            if abs(manual_steering_prev - axis) > 1000:
                autopilot = False
            manual_steering_prev = axis

            self.controller_thread.set_autopilot(autopilot)

            # Get frame of game
            frame_raw = ImageGrab.grab(bbox=functions.get_screen_bbox())
            frame = np.uint8(frame_raw)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Relevant image region for steering angle prediction
            main = frame[s.get_value(Settings.IMAGE_FRONT_BORDER_TOP):s.get_value(Settings.IMAGE_FRONT_BORDER_BOTTOM),
                         s.get_value(Settings.IMAGE_FRONT_BORDER_LEFT):s.get_value(Settings.IMAGE_FRONT_BORDER_RIGHT)]
            # Resize the image to the size of the neural network input layer
            image = scipy.misc.imresize(main, [66, 200]) / 255.0
            # Let the neural network predict the new steering angle
            y_eval = model.y.eval(session=self.sess, feed_dict={model.x: [image], model.keep_prob: 1.0})[0][0]
            degrees = y_eval * 180 / scipy.pi
            steering = int(round((degrees + 180) / 180 * 32768 / 2))  # Value for vjoy controller

            # Set the value of the vjoy joystick to the predicted steering angle
            if autopilot:
                self.controller_thread.set_angle(steering)

            M = cv2.getRotationMatrix2D((cols / 2, rows / 2), -degrees, 1)
            dst = cv2.warpAffine(img, M, (cols, rows))
            functions.set_image(dst.copy(), self.steering_wheel)

            functions.set_image(main.copy(), self.image_front)
