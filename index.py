import time
import sys
import configparser
from PyQt5.QtGui import QPixmap, QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QCheckBox, QHBoxLayout, QDialog, QRadioButton, QToolButton
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QSize, QTimer, QUrl
import datetime
import pygame

config = configparser.ConfigParser()
config.read('config.ini')
global LANG
LANG = config['App']['LANGUAGE']
global voice_set
voice_set = config['App']['voice_set']

class SearchThread(QThread):
    finished = pyqtSignal()

    def __init__(self, ds_cb, bc_cb, cc_cb, gi_cb, rd_cb, dk_cb, wr_cb, tdm_cb, kotr_cb, gd_cb, ww_cb, texts, cancel_button, save_button, current_lang):
        super().__init__()
        self.ds_cb = ds_cb
        self.bc_cb = bc_cb
        self.cc_cb = cc_cb
        self.gi_cb = gi_cb
        self.rd_cb = rd_cb
        self.dk_cb = dk_cb
        self.wr_cb = wr_cb
        self.tdm_cb = tdm_cb
        self.kotr_cb = kotr_cb
        self.gd_cb = gd_cb
        self.ww_cb = ww_cb
        self.cancel_button = cancel_button
        self.save_button = save_button
        self.texts = texts
        
        self.current_lang = current_lang
        pygame.mixer.init()
        self.running = True
        
        
    def stop(self):
        self.running = False
        
    def run(self):
        while self.running:
            time.sleep(1)
            current_time = datetime.datetime.now()
            time_string = current_time.strftime("%H:%M:%S")
            self.now = datetime.datetime.now()
            
            ds_time_str = ["01:54:00", "03:54:00", "05:54:00", "07:54:00", "09:54:00", "11:54:00", "13:54:00", "15:54:00", "17:54:00", "19:54:00", "21:54:00", "23:54:00"]
            ds_time = [datetime.datetime.strptime(t, "%H:%M:%S").time() for t in ds_time_str]
            bc_time_str = ["00:24:00", "01:24:00", "02:24:00", "03:24:00", "04:24:00", "05:24:00", 
               "06:24:00", "07:24:00", "08:24:00", "09:24:00", "10:24:00", "11:24:00", 
               "12:24:00", "13:24:00", "14:24:00", "15:24:00", "16:24:00", "17:24:00", 
               "18:24:00", "19:24:00", "20:24:00", "21:24:00", "22:24:00", "23:24:00"]
            bc_time = [datetime.datetime.strptime(t, "%H:%M:%S").time() for t in bc_time_str]

            cc_time_str = ["00:54:00", "02:54:00", "04:54:00", "06:54:00", "08:54:00", "10:54:00", 
               "12:54:00", "14:54:00", "16:54:00", "18:54:00", "20:54:00", "22:54:00"]
            cc_time = [datetime.datetime.strptime(t, "%H:%M:%S").time() for t in cc_time_str]

            gi_time_str = ["01:14:00", "03:14:00", "05:14:00", "07:14:00", "09:14:00", "11:14:00", 
               "13:14:00", "15:14:00", "17:14:00", "19:14:00", "21:14:00", "23:14:00"]
            gi_time = [datetime.datetime.strptime(t, "%H:%M:%S").time() for t in gi_time_str]

            rd_time_str = ["01:09:00", "03:09:00", "05:09:00", "07:09:00", "09:09:00", "11:09:00", 
               "13:09:00", "15:09:00", "17:09:00", "19:09:00", "21:09:00", "23:09:00"]
            rd_time = [datetime.datetime.strptime(t, "%H:%M:%S").time() for t in rd_time_str]

            dk_time_str = ["00:45:00", "04:45:00", "08:45:00", "12:45:00", "16:45:00", "20:45:00"]
            dk_time = [datetime.datetime.strptime(t, "%H:%M:%S").time() for t in dk_time_str]

            wr_time_str = ["13:46:00", "19:46:00"]
            wr_time = [datetime.datetime.strptime(t, "%H:%M:%S").time() for t in wr_time_str]

            tdm_time_str = ["13:54:50", "19:54:50"]
            tdm_time = [datetime.datetime.strptime(t, "%H:%M:%S").time() for t in tdm_time_str]

            kotr_time_str = ["13:08:00", "15:08:00", "17:08:00", "19:08:00", "21:08:00", "23:08:00"]
            kotr_time = [datetime.datetime.strptime(t, "%H:%M:%S").time() for t in kotr_time_str]

            gd_time_str = ["12:44:00", "18:44:00"]
            gd_time = [datetime.datetime.strptime(t, "%H:%M:%S").time() for t in gd_time_str]

            ww_time_str = ["00:45:00", "02:45:00", "04:45:00", "06:45:00", "08:45:00", "10:45:00", 
               "12:45:00", "14:45:00", "16:45:00", "18:45:00", "20:45:00", "22:45:00"]
            ww_time = [datetime.datetime.strptime(t, "%H:%M:%S").time() for t in ww_time_str]
            
            config = configparser.ConfigParser()
            config.read('config.ini')
            voice_language = config['App']['LANGUAGE']
            voice_gender = config['App']['voice_set']
            

            if self.ds_cb.isChecked(): # DS
                if any(t.hour == self.now.hour and t.minute == self.now.minute and t.second == self.now.second for t in ds_time):
                    if voice_language == 'en':
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male/ds.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female/ds.mp3")
                            pygame.mixer.music.play()
                    else:
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male_ru/ds.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female_ru/ds.mp3")
                            pygame.mixer.music.play()



            if self.bc_cb.isChecked(): # BC
                if any(t.hour == self.now.hour and t.minute == self.now.minute and t.second == self.now.second for t in bc_time):
                    if voice_language == 'en':
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male/bc.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female/bc.mp3")
                            pygame.mixer.music.play()
                    else:
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male_ru/bc.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female_ru/bc.mp3")
                            pygame.mixer.music.play()

            if self.cc_cb.isChecked(): # CC
                if any(t.hour == self.now.hour and t.minute == self.now.minute and t.second == self.now.second for t in cc_time):
                    if voice_language == 'en':
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male/cc.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female/cc.mp3")
                            pygame.mixer.music.play()
                    else:
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male_ru/cc.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female_ru/cc.mp3")
                            pygame.mixer.music.play()


            if self.gi_cb.isChecked(): # GI
                if any(t.hour == self.now.hour and t.minute == self.now.minute and t.second == self.now.second for t in gi_time):
                    if voice_language == 'en':
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male/gi.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female/gi.mp3")
                            pygame.mixer.music.play()
                    else:
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male_ru/gi.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female_ru/gi.mp3")
                            pygame.mixer.music.play()

            if self.rd_cb.isChecked(): # RD
                if any(t.hour == self.now.hour and t.minute == self.now.minute and t.second == self.now.second for t in rd_time):
                    if voice_language == 'en':
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male/rd.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female/rd.mp3")
                            pygame.mixer.music.play()
                    else:
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male_ru/rd.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female_ru/rd.mp3")
                            pygame.mixer.music.play()


            if self.dk_cb.isChecked(): # DK
                if any(t.hour == self.now.hour and t.minute == self.now.minute and t.second == self.now.second for t in dk_time):
                    if voice_language == 'en':
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male/dk.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female/dk.mp3")
                            pygame.mixer.music.play()
                    else:
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male_ru/dk.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female_ru/dk.mp3")
                            pygame.mixer.music.play()

            if self.wr_cb.isChecked(): # WR
                if any(t.hour == self.now.hour and t.minute == self.now.minute and t.second == self.now.second for t in wr_time):
                    if voice_language == 'en':
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male/wr.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female/wr.mp3")
                            pygame.mixer.music.play()
                    else:
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male_ru/wr.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female_ru/wr.mp3")
                            pygame.mixer.music.play()

            if self.tdm_cb.isChecked(): # TDM
                if any(t.hour == self.now.hour and t.minute == self.now.minute and t.second == self.now.second for t in tdm_time):
                    if voice_language == 'en':
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male/tdm.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female/tdm.mp3")
                            pygame.mixer.music.play()
                    else:
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male_ru/tdm.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female_ru/tdm.mp3")
                            pygame.mixer.music.play()

            if self.kotr_cb.isChecked(): # KOTR
                if any(t.hour == self.now.hour and t.minute == self.now.minute and t.second == self.now.second for t in kotr_time):
                    if voice_language == 'en':
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male/kotr.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female/kotr.mp3")
                            pygame.mixer.music.play()
                    else:
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male_ru/kotr.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female_ru/kotr.mp3")
                            pygame.mixer.music.play()

            if self.gd_cb.isChecked(): # GD
                if any(t.hour == self.now.hour and t.minute == self.now.minute and t.second == self.now.second for t in gd_time):
                    if voice_language == 'en':
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male/gd.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female/gd.mp3")
                            pygame.mixer.music.play()
                    else:
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male_ru/gd.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female_ru/gd.mp3")
                            pygame.mixer.music.play()


            if self.ww_cb.isChecked(): # WW
                if any(t.hour == self.now.hour and t.minute == self.now.minute and t.second == self.now.second for t in ww_time):
                    if voice_language == 'en':
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male/ww.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female/ww.mp3")
                            pygame.mixer.music.play()
                    else:
                        if voice_gender == 'male':
                            pygame.mixer.music.load("./sound/male_ru/ww.mp3")
                            pygame.mixer.music.play()
                        else:
                            pygame.mixer.music.load("./sound/female_ru/ww.mp3")
                            pygame.mixer.music.play()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.links = set() 
        self.current_lang = LANG
        self.current_voice = voice_set
        

        self.texts = {
            'ru': {
                'title': 'MU Bless Helper',
                'start_button': 'Начать',
                'switch_lang_button': 'Сменить язык',
                'start_button' : 'Начать',
                'stop_button' : 'Остановить',
                'settings_button' : 'Настройки',
                'voice_button' : 'Голос',
                'voice_male' : 'Мужской',
                'voice_female' : 'Женский',
                'save_button' : 'Сохранить',
                'cancel_button' : 'Отмена',
                'play_button' : 'Прослушать'
            },
            'en': {
                'title': 'MU Bless Helper',
                'start_button': 'Start',
                'switch_lang_button': 'Switch language',
                'start_button' : 'Start',
                'stop_button' : 'Stop',
                'settings_button' : 'Settings',
                'voice_button' : 'Voice',
                'voice_male' : 'Male',
                'voice_female' : 'Female',
                'save_button' : 'Save',
                'cancel_button' : 'Cancel',
                'play_button' : 'Test'
            }
        }
        # Apply style
        with open('style.css', 'r', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

        self.setWindowTitle(self.texts[self.current_lang]['title'])
        self.setGeometry(0, 0, 200, 100)
        self.move(500, 50)
        self.setWindowIcon(QIcon('./img/icon.png'))
        self.thread = None
        layout = QVBoxLayout()
        img_label = QLabel(self)
        img = QPixmap('./img/mulogo.png').scaled(500, 300)
        img_label.setPixmap(img)
        img_label.setScaledContents(True)
        layout.addWidget(img_label)

        global us_flag_icon
        us_flag_icon = QIcon('./img/us_flag.png')
        global ru_flag_icon
        ru_flag_icon = QIcon('./img/ru_flag.png')
        
        self.lang_selector = QComboBox(self)
        self.lang_selector.setIconSize(QSize(20, 20))
        if LANG == 'en':
            self.lang_selector.addItem(us_flag_icon, 'English')
            self.lang_selector.addItem(ru_flag_icon, 'Русский')
        elif LANG == 'ru':
            self.lang_selector.addItem(us_flag_icon, 'English')
            self.lang_selector.addItem(ru_flag_icon, 'Русский')
            self.lang_selector.setCurrentIndex(1)

        self.lang_selector.currentIndexChanged.connect(self.change_language)
        layout.addWidget(self.lang_selector)


        self.ds_cb = QCheckBox('Devil Square')
        self.bc_cb = QCheckBox('Blood Castle')
        self.cc_cb = QCheckBox('Chaos Castle')
        self.gi_cb = QCheckBox('Golden Invasion')
        self.rd_cb = QCheckBox('Red Dragon Invasion')
        self.dk_cb = QCheckBox('Death King')
        self.wr_cb = QCheckBox('White Rabbits')
        self.tdm_cb = QCheckBox('Team Deathmatch')
        self.kotr_cb = QCheckBox('King of the Ring')
        self.gd_cb = QCheckBox('Great Dragon')
        self.ww_cb = QCheckBox('White Wizard')

        # Telegram Button
        self.telegram_button = QToolButton(self)
        #self.contact_label = QLabel("Contact Us", self) 
        #self.contact_label.setFont(QFont("Arial", 16))
        #self.contact_label.setStyleSheet("background-color: transparent;")
        icon = QIcon("./img/telegram_logo.png") # путь к файлу с логотипом телеграма
        self.telegram_button.setIcon(icon)
        self.telegram_button.setIconSize(QSize(40, 40)) # размер иконки
        self.telegram_button.setToolTip("Contact me in Telegram") # всплывающая подсказка
        self.telegram_button.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://t.me/in_motion"))) 

        self.telegram_button.setStyleSheet("QToolButton { border: none; background: none; } \
QToolButton:hover { border: 2px solid #FFFFFF; }")
        self.telegram_button.setGeometry(470, 270, 40, 40)
        #self.contact_label.setGeometry(50, 215, 120, 20)
        

        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()
        layout1.addWidget(self.ds_cb)
        layout1.addWidget(self.bc_cb)
        layout1.addWidget(self.cc_cb) 
        layout1.addWidget(self.gi_cb)
        layout1.addWidget(self.rd_cb)
        layout1.addWidget(self.dk_cb) 


        layout2.addWidget(self.dk_cb) 
        layout2.addWidget(self.wr_cb)
        layout2.addWidget(self.tdm_cb)
        layout2.addWidget(self.kotr_cb)
        layout2.addWidget(self.gd_cb)    
        layout2.addWidget(self.ww_cb)


        main_layout = QHBoxLayout() 
        main_layout.addLayout(layout1) 
        main_layout.addLayout(layout2)
        layout.addLayout(main_layout)
        self.setLayout(layout)


        self.start_button = QPushButton(self.texts[self.current_lang]['start_button'])
        self.settings_button = QPushButton(self.texts[self.current_lang]['settings_button'], self)
        self.settings_button.clicked.connect(self.open_settings_window)
        layout.addWidget(self.settings_button)

    
        self.start_button.clicked.connect(self.search_clicked)
        layout.addWidget(self.start_button)


    def open_settings_window(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        voice_set = config.get('App', 'voice_set')
        settings_window = QDialog(self)
        settings_window.setWindowTitle(self.texts[self.current_lang]['settings_button'])
        settings_window.setGeometry(0, 0, 300, 200)
        settings_window.move(500, 350)

        voice_label = QLabel(self.texts[self.current_lang]['voice_button'], settings_window)
        voice_label.move(20, 10)

        self.voice_male_rb = QRadioButton(self.texts[self.current_lang]['voice_male'], settings_window)
        self.voice_male_rb.setStyleSheet("font-size: 16px;")
        self.voice_male_rb.move(20, 40)
        if voice_set == 'male':
            self.voice_male_rb.setChecked(True)
            
        play_button = QPushButton(self.texts[self.current_lang]['play_button'], settings_window)
        
        play_button.setGeometry(0, 0, 80, 30)
        play_button.move(125, 35)
        play_button.setStyleSheet("font-size: 10px;")
        play_button.clicked.connect(self.play_mp3)

        self.voice_female_rb = QRadioButton(self.texts[self.current_lang]['voice_female'], settings_window)
        self.voice_female_rb.setStyleSheet("font-size: 16px;")
        self.voice_female_rb.move(20, 100)
        if voice_set == 'female':
            self.voice_female_rb.setChecked(True)

        play_button = QPushButton(self.texts[self.current_lang]['play_button'], settings_window)
        
        play_button.setGeometry(0, 0, 80, 30)
        play_button.move(125, 100)
        play_button.setStyleSheet("font-size: 10px;")
        play_button.clicked.connect(self.play_mp3_female)

        save_button = QPushButton(self.texts[self.current_lang]['save_button'], settings_window)
        save_button.move(130, 160)
        save_button.clicked.connect(self.save_settings)
        save_button.clicked.connect(settings_window.accept)


        self.cancel_button = QPushButton(self.texts[self.current_lang]['cancel_button'], settings_window)
        self.cancel_button.move(50, 160)
        self.cancel_button.clicked.connect(settings_window.reject)

        settings_window.exec_()

    def save_settings(self):
        if self.voice_male_rb.isChecked():
            config = configparser.ConfigParser()
            config.read('config.ini')
            config.set('App', 'voice_set', 'male')
            with open('config.ini', 'w') as config_file:
                config.write(config_file)
        else:
            config = configparser.ConfigParser()
            config.read('config.ini')
            config.set('App', 'voice_set', 'female')
            with open('config.ini', 'w') as config_file:
                config.write(config_file)
        

    def play_mp3(self):
        pygame.init()
        
        config = configparser.ConfigParser()
        config.read('config.ini')
        voice_language = config['App']['LANGUAGE']
        if voice_language == 'en':
            pygame.mixer.music.load("./sound/test_msg_male.mp3")
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load("./sound/test_msg_male_ru.mp3")
            pygame.mixer.music.play()

    def play_mp3_female(self):
        pygame.init()
        config = configparser.ConfigParser()
        config.read('config.ini')
        voice_language = config['App']['LANGUAGE']
        if voice_language == 'en':
            pygame.mixer.music.load("./sound/test_msg_female.mp3")
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.load("./sound/test_msg_female_ru.mp3")
            pygame.mixer.music.play()


    def change_language(self, index):
        if index == 0:
            self.current_lang = 'en'
        elif index == 1:
            self.current_lang = 'ru'

        self.update_texts()

    def switch_language(self):
        langs = list(self.texts.keys())
        current_index = langs.index(self.current_lang)
        next_index = (current_index + 1) % len(langs)
        self.current_lang = langs[next_index]

        if self.current_lang == 'en':
            self.lang_selector.setItemText(0, 'English')
            self.lang_selector.setItemText(1, 'Русский')
        elif self.current_lang == 'ru':
            self.lang_selector.setItemText(0, 'English')
            self.lang_selector.setItemText(1, 'Русский')

        self.lang_selector.setCurrentIndex(next_index)
        self.update_texts()

    


    def update_texts(self):
        self.setWindowTitle(self.texts[self.current_lang]['title'])
        if self.current_lang == 'en':
            self.lang_selector.setItemText(0, 'English')
            self.lang_selector.setItemText(1, 'Русский')
        elif self.current_lang == 'ru':
            self.lang_selector.setItemText(0, 'English')
            self.lang_selector.setItemText(1, 'Русский')

        self.start_button.setText(self.texts[self.current_lang]['start_button'])
        self.settings_button.setText(self.texts[self.current_lang]['settings_button'])

        config = configparser.ConfigParser()
        config.read('config.ini')
        config.set('App', 'LANGUAGE', self.current_lang)
        with open('config.ini', 'w') as config_file:
            config.write(config_file)
        self.setWindowTitle("MU Bless Helper")


    def set_button_text(self, text):
        self.start_button.setText(text)

    def animate_button(self):
        text = self.start_button.text()
        if text.endswith('...'):
            text = text[:-3]
        else:
            text += '.'
        self.set_button_text(text)


    @pyqtSlot()
    def search_clicked(self):
        
        if self.thread is None or not self.thread.isRunning():       
                
            self.thread = SearchThread(self.ds_cb, self.bc_cb, self.cc_cb, self.rd_cb, self.gi_cb, self.dk_cb, self.wr_cb, self.tdm_cb, self.kotr_cb, self.gd_cb, self.ww_cb, self.texts, self.current_lang, current_lang=None, save_button=None)
            self.thread.finished.connect(self.thread_finished)

            self.start_button.setText(self.texts[self.current_lang]['stop_button'])
            self.thread.start()


            config = configparser.ConfigParser()
            config.read('config.ini')
            voice_language = config['App']['LANGUAGE']
            voice_gender = config['App']['voice_set']
            if voice_language == 'en':
                if voice_gender == 'male':
                    pygame.mixer.music.load("./sound/male/started.mp3")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("./sound/female/started.mp3")
                    pygame.mixer.music.play()
            else:
                if voice_gender == 'male':
                    pygame.mixer.music.load("./sound/male_ru/started.mp3")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("./sound/female_ru/started.mp3")
                    pygame.mixer.music.play()

            self.set_button_text(self.texts[self.current_lang]['stop_button'] + '...')

            self.animation_timer = QTimer()
            self.animation_timer.timeout.connect(self.animate_button)
            self.animation_timer.start(700)

        else:
            self.thread.stop()
            config = configparser.ConfigParser()
            config.read('config.ini')
            voice_language = config['App']['LANGUAGE']
            voice_gender = config['App']['voice_set']
            if voice_language == 'en':
                if voice_gender == 'male':
                    pygame.mixer.music.load("./sound/male/stop.mp3")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("./sound/female/stop.mp3")
                    pygame.mixer.music.play()
            else:
                if voice_gender == 'male':
                    pygame.mixer.music.load("./sound/male_ru/stop.mp3")
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("./sound/female_ru/stop.mp3")
                    pygame.mixer.music.play()

            self.animation_timer.stop()
            self.start_button.setText(self.texts[self.current_lang]['stop_button'])
            self.start_button.setText(self.texts[self.current_lang]['start_button'])
            


    @pyqtSlot()
    def thread_finished(self):
        self.start_button.setText(self.texts[self.current_lang]['start_button'])
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())