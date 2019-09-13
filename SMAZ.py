#!/expSW/SOFTWARE/python371/bin/python3.7
#!/expSW/SOFTWARE/python366/bin/python3.6
#!/usr/bin/env python3.6
#!/usr/bin/python3
#-*- coding: utf-8 -*-


# import os
# import re
# import fnmatch


# class Variant():
#     """Variant class"""

#     def __init__(self, fullpath):
#         self.fullpath = fullpath
#         self.name = os.path.basename(self.fullpath)  # SK3820EUK_2IB_004
#         self.root_folder = os.path.dirname(self.fullpath)  # /ST/SkodaAuto/.../2/
#         self.dsy_exists = True if self.dsy_fullpath else False

#     @property
#     def dsy_fullpath(self):
#         """Return DSY fullpath found recursively in variant directory. If not found, return None."""
#         dsy_files = []
#         for root, dirs, files in os.walk(self.fullpath, topdown=True):
#             for filename in fnmatch.filter(files, '*DSY*'):
#                 dsy_files.append(filename)
#         if len(dsy_files) > 1:
#             print("More than one *DSY* file found in variant: {}, returning only the first".format(self.name))
#             return dsy_files[0]
#         elif len(dsy_files) == 0:
#             # *DSY* file not found in variant
#             return None
#         else:
#             return dsy_files[0]


# def get_variants():
#     """Return list of Variant objects found in selected directory."""
#     variants = []
#     path = '/ST/SkodaAuto/STRUCT/PRJ/VYHODNOCENI/SK3820EUK/CRASH/INSURANCE/BACK/2/'
#     for item in os.listdir(path):
#         fullpath_item = os.path.join(path, item)
#         if not re.match(r'SK\d', item) or not os.path.isdir(fullpath_item):
#             continue
#         variant = Variant(fullpath_item)
#         variants.append(variant)
#     return variants


# variants = get_variants()
# for var in variants:
#     print(var.dsy_exists)


# import tarfile

# with tarfile.open('/ST/Evektor/UZIV/JVERNER/NEZALOHUJESE/SMAZ/SK3166EUB_1FO_995_2015.RESULTS.tgz') as tar:
#     out_files = []
#     for member in tar:
#         # Append .out files
#         if member.name.endswith('.out'):
#             out_files.append((member, member.size))

#     if out_files:
#         out_files.sort(key=lambda typ: typ[1], reverse=True)  # sort by largest size
#         out_file = out_files[0][0]
#         f = tar.extractfile(out_file)
#         out_lines = [line.decode('ISO-8859-1').strip() for line in f.readlines()]


# import numpy as np

# import matplotlib.animation as animation
# from matplotlib import pyplot

# fig, g = pyplot.subplots(figsize=(8, 6))  # (7,7)
# pyplot.subplots_adjust(left=0.05, right=0.95, top=0.94, bottom=0.06)
# z = "lightblue"  # lightblue
# pyplot.rcParams['axes.facecolor'] = z
# pyplot.rcParams['savefig.facecolor'] = z


# def square(Ymin, Xmin, v, cl):
#     a = 0.15  # 0.15
#     pyplot.plot(Xmin, Ymin, markersize=v, marker='s', alpha=a, markerfacecolor=cl, markeredgecolor=cl)
#     pyplot.grid(False)
#     pyplot.yticks([])
#     pyplot.xticks([])
#     pyplot.ylim(0.2, 0.8)
#     pyplot.axis("OFF")
#     pyplot.xlim(0.2, 0.8)
#     pyplot.show()
#     return


# fr = 28
# ct = 0
# cln = 0
# Fs = 70  # 80 , 16
# f = 5
# sample = 60
# x = np.arange(sample)
# z = np.sin(2.0 * np.pi * f * x / Fs) / 100
# z1 = np.cos(2.0 * np.pi * f * x / Fs) / 90


# def update(*args):
#     pyplot.clf()
#     global s, ct, fr, z, z1
#     c1 = "steelblue"
#     a = range(10, 370, 26)  # 26
#     d = np.linspace(0.01, 0, len(a))
#     c = 0
#     for n in a:
#         square(0.5 - z1[c], 0.5 - d[0] + z[c] + z1[c], n, c1)
#         c += 1
#     z = np.delete(z, 0)
#     z1 = np.delete(z1, 0)
#     return


# def init():
#     return


# anim = animation.FuncAnimation(fig, update, init_func=init, blit=True, frames=fr, repeat=False)

# # sf = "squares.gif"
# # Sname = "~/" + sf   # Change your directory
# # anim.save(Sname, writer="imagemagick", fps=20)  # 15
# import sys
# import requests
# import numpy as np
# import logging
# LOG_FORMAT = '%(asctime)s %(levelname)s - %(message)s'
# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
# log = logging.getLogger()

# results = np.array([])
# try:
#     for num in np.arange(-1, 1, 0.2):
#         num = num / 10
#         # page = requests.get("http://165.227.157.145:8080/api/do_measurement?x={}".format(num))
#         res = page.json().get('data')
#         np.append(results, [res.get('x'), res.get('y')])
# except Exception as e:
#     log.critical("chybka na radku: {}".format(sys.exc_info()[-1].tb_lineno))
#     log.error("Podrobnosti: {}".format(e))

# log.info(results)

#     # print(res.get('x'), res.get('y'))

#     # results = np.append(results, res)

# # from pprint import pprint
# # pprint(results)


# # ====================
# # Ansa MainProgressBar
# # ====================

# import os
# import ansa
# from ansa import base, utils, mesh

# parts = base.CollectEntities(0, None, "ANSAPART")
# utils.MainProgressBarSetVisible(1)
# i = 0
# for part in parts:
#     base.Or(part)
#     mesh.CreateFreeMesh()
#     i = i+1
#     utils.MainProgressBarSetText(" part(s) meshed...")
#     j = (100*i)/len(parts)
#     utils.MainProgressBarSetValue(j)

# utils.MainProgressBarSetVisible(0)


# ============================================================
# Sentdex - Asyncio - Asynchronous programming with coroutines
# ============================================================


# import asyncio


# # async def find_divisibles(inrange, div_by):
# @asyncio.coroutine
# def find_divisibles(inrange, div_by):
#     print("finding nums in range {} divisible by {}".format(inrange, div_by))
#     located = []
#     for i in range(inrange):
#         if i % div_by == 0:
#             located.append(i)
#         if i % 50000 == 0:
#             yield from asyncio.sleep(0.0001)

#     print("Done w/ nums in range {} divisible by {}".format(inrange, div_by))
#     return located


# # async def main():
# @asyncio.coroutine
# def main():
#     divs1 = loop.create_task(find_divisibles(4080000, 34113))
#     divs2 = loop.create_task(find_divisibles(2005002, 34110))
#     divs3 = loop.create_task(find_divisibles(505002, 34107))
#     yield from asyncio.wait([divs1, divs2, divs3])
#     return divs1, divs2, divs3

#     # await coroutine()
#     # yield from coroutine()


# if __name__ == '__main__':
#     try:
#         loop = asyncio.get_event_loop()
#         # loop.set_debug(1)
#         d1, d2, d3 = loop.run_until_complete(main())
#         print(d1.result())
#         print(d2.result())
#         print(d3.result())
#     except Exception as e:
#         pass
#     finally:
#         loop.close()


# ============================================================
# GUI - TKINTER - File Search pokus 1
# ============================================================


# # A GUI search program using tkinter
# # Created by David Briddock

# from tkinter import *
# import os

# # initialise main window


# def init(win):
#     win.title("File Search")

#     labelPath.grid(row=0, column=0, sticky="W")
#     entryPath.grid(row=1, column=0)
#     labelEnding.grid(row=2, column=0, sticky="W")
#     entryEnding.grid(row=3, column=0)
#     btnSearch.grid(row=4, column=0)
#     fileList.grid(row=0, column=1, rowspan=5)
#     yscroll.grid(row=0, column=2, rowspan=5, sticky="NS")

#     fileList.configure(yscrollcommand=yscroll.set)
#     yscroll.configure(command=fileList.yview)
#     entryPath.insert(INSERT, "/home")
#     entryEnding.insert(INSERT, ".py")

# # find button callback


# def search():
#     # get start directory and file ending
#     startDir = entryPath.get()
#     fileEnding = entryEnding.get()

#     # clear the listbox
#     fileList.delete(0, END)

#     # find matching file and fill listbox
#     for path, dirs, files in os.walk(startDir):
#         for fileName in files:
#             if (fileName.endswith(fileEnding)):
#                 fileList.insert(END, path + "/" + fileName)

# # create top-level window object
# win = Tk()

# # create widgets
# labelPath = Label(win, text="Starting Path")
# entryPath = Entry(win, width=12)
# labelEnding = Label(win, text="File Ending")
# entryEnding = Entry(win, width=12)
# fileList = Listbox(win, width=80)
# yscroll = Scrollbar(win, orient=VERTICAL)
# btnSearch = Button(win, text="Search", width=8, command=search)

# # initialise and run main loop
# init(win)
# mainloop()


# ============================================================
# GUI - TKINTER - File Search pokus 2
# ============================================================


# # Program to demonstrate list boxes in Python

# # Import the tkinter module for GUI components
# from tkinter import *

# # Create ListBoxDemo class based on the Frame class


# class ListBoxDemo(Frame):

#     def __init__(self, master):
#         super(ListBoxDemo, self).__init__(master)
#         # Link frame to grid manager
#         self.grid()
#         # Create a Label
#         Label(self, text="This is a list box demostration program.", font="Calibri 14").grid(row=1, sticky=N, columnspan=2)

#         # Empty row
#         Label(self).grid(row=2)

#         # Set up label for list box widget
#         Label(self, text="Click one or more of the operating systems below:", font="Calibri 12").grid(row=3, column=0, sticky=W)

#         # Create listbox itself
#         self.oslistbox = Listbox(self, height=10, selectmode=MULTIPLE)
#         self.oslistbox.grid(column=0, row=5, sticky=N)

#         # Fill the list box with operating systems
#         # Use for loop
#         for os in ["Ubunutu", "Mint", "Debian", "Redhat", "Fedora", "OpenSuse", "Xubuntu", "Puppy", "Kali"]:
#             self.oslistbox.insert(END, os)

#         # Create textbox to display chosen items
#         self.chosenos = Text(self, width=20, height=6, wrap=WORD)
#         self.chosenos.grid(row=10, column=0, sticky=N)

#         # Run poll() method to pick up chosen operating systems
#         self.poll()

#     def updatetextbox(self):
#         self.chosenos.delete(0.0, END)
#         self.chosenos.insert(0.0, self.selectedos)

#         # Define poll() method that was run above
#     def poll(self):
#         oslist = []
#         self.selectedos = []
#         # Run poll() method every 200 ms; can be any widget
#         self.oslistbox.after(200, self.poll)

#         # Create tuple of index of items chsen using curselection method
#         # Convert to an integer then convert to a list and place on "oslist"
#         oslist = list(map(int, self.oslistbox.curselection()))

#         # start for loop
#         for alpha in range(len(oslist)):
#             # take numbers from "oslist" and get selected items from "oslistbox"
#             # then append them to "selectedos"
#             self.selectedos.append(self.oslistbox.get(oslist[alpha]))

#         # update the text box with the selections
#         self.updatetextbox()
#         # end poll() method


# #Main program
# # Create a window; create an object called "root"
# root = Tk()

# # title of the GUI window
# root.title("List box demonstration.")

# # dimensions of the window
# root.geometry("400x400")

# # create ListBoxDemo object
# listbox1 = ListBoxDemo(root)

# # command that will launch the GUI application
# root.mainloop()


# ============================================================
# GUI - PYQT5 - FILE SEARCH
# ============================================================


# import sys
# from PyQt4.QtGui import *

# # Create an PyQT4 application object.
# a = QApplication(sys.argv)

# # The QWidget widget is the base class of all user interface objects in PyQt4.
# w = QWidget()

# # Set window size.
# w.resize(320, 240)

# # Set window title
# w.setWindowTitle("Hello World!")

# # Show window
# w.show()

# sys.exit(a.exec_())


# ============================================================
# GUI - PYSIDE - FILE SEARCH
# ============================================================

# def prepareGUI(self):
#     self.resize(320, 240)
#     self.setWindowTitle("Quit Button")
#     self.centerOnScreen()

# def centerOnScreen(self):
#     frameGm = self.frameGeometry()
#     screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
#     # centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
#     centerPoint = QtGui.QDesktopWidget().screenGeometry(screen).center()
#     frameGm.moveCenter(centerPoint)
#     self.move(frameGm.topLeft())


# #=======================================================================================================
# # TESTING WITH SUBPROCESS, REALTIME STDOUT and save to VARIABLE
# #=======================================================================================================

# # import os
# import sys
# import subprocess

# # subprocess.run(['{ echo "y" }', '/home/jverner/SMAZ.sh'])
# # command = '{ echo "y"; echo "y"; } | /home/jverner/SMAZ.sh'
# # print(command)

# # os.system(command)
# # subprocess.run(command.split(' '))

# # p = subprocess.Popen(['./SMAZ.sh'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, encoding='utf-8')
# # p = subprocess.Popen(['./SMAZME.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, encoding='utf-8')


# def myrun():
#     """from http://blog.kagesenshi.org/2008/02/teeing-python-subprocesspopen-output.html
#     """
#     p = subprocess.Popen(['./SMAZME.py'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8')
#     stdout = []
#     while True:
#         line = p.stdout.readline()
#         stdout.append(line)
#         print(line)
#         if line == '' and p.poll() == 0:
#             break
#     return ''.join(stdout)

# # while True:
# #     line = p.stdout.readline()
# #     if not line:
# #         break
# #     sys.stdout.write(line)

# res = myrun()

# # for line in iter(p.stdout.readline, ''):
# #     print(line)
# #     if 'Question' in line:
# #         p.stdin.write('y')

# # res = p.communicate('y')
# # print("DEBUG: res:", res)

# # stdout = ''.join(stdout)
# # print("DEBUG: stdout:", stdout)

# # res = p.communicate('y\ny')
# # print("DEBUG: res:", res)


# #=======================================================================================================
# # MANY get_directory RESULTS IN ONE TIME
# #=======================================================================================================


# import subprocess
# from pathlib import Path

# GET_DIRECTORY_SCRIPT = '/ST/SkodaAuto/STRUCT/PRJ/VYHODNOCENI/AGP/PRE/TOOLS/GET_DIRECTORY/get_directory.pl'

# with open('/home/jverner/PROJECTS.txt') as f:
#     lines = [Path(line.strip().replace('.md5', '')) for line in f.readlines()]

# projects = [(line.parts[0], line.stem.split('.')[0]) for line in lines if len(line.stem.split('.')[0].split('_')) >= 3]

# # print(projects)

# # exit()

# for idx, prj in enumerate(projects, 1):
#     p = subprocess.Popen([GET_DIRECTORY_SCRIPT, '_'.join(prj[1].split('_')[0:3])], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
#     (out, err) = p.communicate()
#     print("{}\t HOMER: {} \t PRJ: {} \t OUT: {}".format(idx, prj[0], prj[1], out.strip()))
#     # if idx > 200:
#     #     break


# #=======================================================================================================
# # TESTING PyQT5 with Python3.6
# #=======================================================================================================
# #!/usr/bin/env python3.6
# #!/expSW/SOFTWARE/python366/bin/python3.6

# import sys
# from PyQt5.QtWidgets import (QWidget, QToolTip,
#                              QPushButton, QApplication)
# from PyQt5.QtGui import QFont


# class Example(QWidget):

#     def __init__(self):
#         super().__init__()

#         self.initUI()


#     def initUI(self):

#         QToolTip.setFont(QFont('SansSerif', 10))

#         self.setToolTip('This is a <b>QWidget</b> widget')

#         btn = QPushButton('Button', self)
#         btn.setToolTip('This is a <b>QPushButton</b> widget')
#         btn.resize(btn.sizeHint())
#         btn.move(50, 50)

#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('Tooltips')
#         self.show()


# if __name__ == '__main__':

#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# # #=======================================================================================================
# # # NETWORK DATA - MATPLOTLIB EXTRACT PLOT
# # #=======================================================================================================

# import sys
# from collections import defaultdict
# from pathlib import Path
# from matplotlib import pyplot as plt
# from pprint import pprint
# from scipy.interpolate import interp1d
# import numpy as np
# import datetime


# class Const:
#     LOG_FOLDER = Path("/ST/Evektor/UZIV/JVERNER/PROJEKTY/GIT/jverner/utilities/network_load/")
#     VALID_INTERVALS = [60, 300, 3600, 43200, 86400]


# class Data:

#     def __init__(self, folder_path):
#         self.folder_path = folder_path
#         self.log_files = self._get_log_files()
#         self.files_by_username = defaultdict(list)
#         self.files_by_hostname = defaultdict(list)
#         self._fill_dictionaries()

#     def _get_log_files(self):
#         return [file for file in self.folder_path.iterdir()
#                 if file.suffix == '.log'
#                 if len(file.stem.split('_')) == 6]

#     def _fill_dictionaries(self):
#         for file in self.log_files:
#             _, host, user, location, department, timediff = file.stem.split('_')
#             self.files_by_hostname[host].append(file)
#             self.files_by_username[user].append(file)

#     def _interval_is_valid(self, interval):
#         if interval in Const.VALID_INTERVALS:
#             return True
#         print(f"Interval: {interval} is not a valid number.")
#         print(f"Please choose from: {Const.VALID_INTERVALS}")
#         return False

#     def plot(self, mode='hostname', interval=86400):
#         """Plot graph.

#         Atributes
#         ---------
#             mode: 'username', 'hostname'
#             interval: 60, 300, 3600, 43200, 86400
#         """
#         if not self._interval_is_valid(interval):
#             return 1

#         print(f"Plotting mode/interval: {mode}/{interval}")

#         # PLOT
#         plt.title("Interval 1 DAY")
#         plt.style.use('ggplot')
#         plt.ylabel("DOWNLOAD [MB]")
#         plt.grid(linestyle='dashed', alpha=0.3)

#         curdict = self.files_by_hostname if mode == 'hostname' else self.files_by_username

#         all_gb_per_day = []
#         all_total_gb = []

#         lst_of_axes_y_max = []
#         for idx, (dict_key, log_files) in enumerate(curdict.items()):
#             # if idx < 10 or idx > 20:
#                 # continue
#             file = [file for file in log_files if file.stem.endswith(f'_{interval}')][0]

#             with open(file, 'r') as f:
#                 lines = [line.strip() for line in f.readlines()][1:]

#             x_vals, y_vals = [], []
#             for line in lines:
#                 datestamp, uptime, _, _, _, _, up, dl = line.split(';')
#                 dl, up = int(dl), int(up)
#                 date = datetime.datetime.strptime(datestamp.split('.')[0], '%Y-%m-%d %H:%M:%S')
#                 x_vals.append(date)
#                 y_vals.append(dl)
#                 lst_of_axes_y_max.append(dl)

#             gb_per_day = int(sum(y_vals) / 1000 / len(x_vals))
#             total_gb = int(sum(y_vals) / 1000)

#             all_gb_per_day.append(gb_per_day)
#             all_total_gb.append(total_gb)

#             plt.plot(x_vals, y_vals, '-o', label='{}: {} GB/day, Total: {} GB'.format(
#                 dict_key, gb_per_day, total_gb))

#             plt.legend()

#         print("GB per day:", sum(all_gb_per_day))
#         print("SUM GB", sum(all_total_gb))

#         plt.ylim(-50, max(lst_of_axes_y_max) + 100)

#         # Show plot
#         plt.show()


# def main():
#     """Docs."""
#     data = Data(folder_path=Const.LOG_FOLDER)

#     # interval = 3600
#     data.plot(mode='username')
#     # data.plot(mode='username', interval=3600)


# if __name__ == '__main__':
#     main()


# import os
# import shlex
# import subprocess as sp


# env = {
#     **os.environ,
#     'PAMSHARE': f'{os.environ["PAMHOME"]}/userlibs/vw_libuser/2015.04/Vdefault/compiled_on_default/Linux/em64t/SMP/SP/lib'
# }

# pamcrash_ver = '/expSW/SOFTWARE/PamCrash5up/pamcrash_safe/2015.04/pamcrash -fp 1 -nt 1'

# cmd = shlex.split(f'echo {env["PAMSHARE"]}')
# # p = sp.Popen('echo $PAMSHARE', env=dict(**os.environ))
# p = sp.Popen(cmd, env=dict(**env), stdout=sp.PIPE, stderr=sp.PIPE)
# res = p.communicate()
# print("DEBUG: res:", res)

# cmd = shlex.split('echo $PAMSHARE')
# res = sp.check_output('echo $PAMSHARE', env=dict(PAMSHARE="Hmm", **os.environ), shell=True)
# print("DEBUG: res2:", res)

# cmd = shlex.split(f'{pamcrash_ver} SMAZME.py')
# p = sp.Popen(cmd, env=env, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)
# # res = p.communicate()

# for line in p.stdout:
#     print(line.rstrip())


# import os
# from pathlib import Path

# CURDIR = Path('/home/jverner/NEWVAR')

# for file in CURDIR.rglob('*'):
#     depth = str(file.relative_to(CURDIR)).count('/')
#     if depth >= 3:
#         continue

#     if file.name.endswith(('_pam2xml.log', '_submit.sh')):
#         # os.remove(file)
#         file.unlink()
#         print("File removed... {}".format(file.resolve()))


# Week 2, 4. Functions, Power iter
# def iterPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0

#     returns: int or float, base^exp
#     '''
#     ret = 1
#     for _ in range(exp):
#         ret = ret * base

#     return ret


# def findMaxExp(base):
#     print("DEBUG: base:", base)
#     if base in (0, 1):
#         return 'base = 0 or 1'
#     end = False
#     exp = 0
#     while end != True:
#         # print("DEBUG: exp:", exp)
#         res = iterPower(base, exp)
#         if res == float('inf'):
#             end = True
#         else:
#             exp += 1
#         # else:
#         #     print(exp)
#     return exp

# for base in range(3, 10):
#     print("DEBUG: findMaxExp():", findMaxExp(base))


# import math


# def polysum(n, s):
#     area = (0.25 * n * s**2) / (math.tan(math.pi / n))
#     perimeter = (n * s)**2
#     return round(area + perimeter, 4)


# n = 6
# s = 40
# print("DEBUG: polysum(n, s):", polysum(n, s))
# assert polysum(n, s) == 61756.9219


# # PROBLEM SET 2 ............ Problem 1

# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04


# def calculate(balance):
#     """Docs."""
#     updated_balance = balance

#     # Monthly Interest Rate
#     monthly_interest_rate = annualInterestRate / 12

#     # Iterate over 12 months
#     for month_num in range(1, 13):

#         # Minimum monthly payment
#         min_monthly_payment = monthlyPaymentRate * updated_balance

#         # Monthly unpaid balance
#         monthly_unpaid_balance = updated_balance - min_monthly_payment

#         # Updated balance each month
#         updated_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)

#     # Updated balance after 12 months
#     new_balance = round(updated_balance, 2)

#     return "Remaining balance: {}".format(new_balance)


# print(calculate(balance))


# def oddTuples(aTup):
#     '''
#     aTup: a tuple

#     returns: tuple, every other element of aTup.
#     '''
#     # ls = []
#     # for idx, item in enumerate(aTup):
#     #     if idx % 2 != 0:
#     #         continue
#     #     ls.append(item)

#     # new_tuple = tuple(ls)
#     # return new_tuple

#     return tuple((item for idx, item in enumerate(aTup) if idx % 2 == 0))

# print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))


# listA = [1, 4, 3, 0]
# listB = ['x', 'z', 't', 'q']

# print("DEBUG: listA.sort:", listA.sort)
# print("DEBUG: listA.sort():", listA.sort())
# print("DEBUG: listA:", listA)
# print("DEBUG: listA.insert(0, 100):", listA.insert(0, 100))
# print("DEBUG: listA.remove(3):", listA.remove(3))
# print("DEBUG: listA.append(7):", listA.append(7))
# print("DEBUG: listA:", listA)
# print("DEBUG: listA + listB:", listA + listB)
# print("DEBUG: listB.sort():", listB.sort())
# print("DEBUG: listB.pop():", listB.pop())
# print("DEBUG: listB.count('a'):", listB.count('a'))
# # print("DEBUG: listB.remove('a'):", listB.remove('a'))
# print("DEBUG: listA.extend([4, 1, 6, 3, 5]):", listA.extend([4, 1, 6, 3, 5]))
# print("DEBUG: listA.count(4):", listA.count(4))
# print("DEBUG: listA.index(1):", listA.index(1))
# print("DEBUG: listA.pop(4):", listA.pop(4))
# print("DEBUG: listA.reverse():", listA.reverse())
# print("DEBUG: listA:", listA)


# # ==========================================================================================================
# # NamedTuple > 3.7
# # ==========================================================================================================
# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height', 'ears', 'eyes'], defaults=(2, 2,))
# milton = Person('Milton', 25, 172)
# print(milton)  #

# # ==========================================================================================================
# # NamedTuple < 3.7
# # ==========================================================================================================
# from collections import namedtuple
# Person = namedtuple('Person', ['name', 'age', 'height', 'ears', 'eyes'])
# Person.__new__.__defaults__ = (2, 2,)
# milton = Person('Milton', 25, 172)
# milton = Person('Milton', 25, 172, ears=1, eyes=1)
# print(milton)  #

# # ==========================================================================================================
# # typing - NamedTuple
# # ==========================================================================================================
# from typing import NamedTuple
# class Person(NamedTuple):
#     name: str
#     age: int
#     height: int
#     ears: int = 2
#     eyes: int = 2


# milton = Person('Milton', 25, 172)
# print(milton)  # Person(name='Milton', age=25, height=172, ears=2, eyes=2)


# # ==========================================================================================================
# # CLASS
# # ==========================================================================================================
# class Person:
#     def __init__(self, name: str, age: int, height: int, ears: int=2, eyes: int=2):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.ears = ears
#         self.eyes = eyes

#     # def __str__(self):
#     #     return "{}(name='{}', age={}, height={}, ears={}, eyes={})".format(
#     #         Person.__name__, self.name, self.age, self.height, self.ears, self.eyes)

#     def __str__(self):
#         return f"{Person.__name__}(name='{self.name}', age={self.age}, height={self.height}, ears={self.ears}, eyes={self.eyes})"


# milton = Person('Milton', 25, 172)
# print(milton)  # <__main__.Person at 0x7fd5ec4c25c0>


# import requests
# # r = requests.get('http://intranet/attendance/User/AttendanceList.asp?Year=2019&Month=2&IDPerson=2174&Print=0&CloseMonth=0')
# # print(r.status_code)
# # print(r.content)
# from requests_kerberos import HTTPKerberosAuth
# ##########r = requests.get('http://intranet/attendance/User/AttendanceList.asp?Year=2019&Month=2&IDPerson=2174&Print=0&CloseMonth=0', auth=HTTPKerberosAuth())
# # print(r.status_code)
# # print(r.content)
# # print(r.content.decode('windows-1250'))
# from bs4 import BeautifulSoup
# # soup = BeautifulSoup(r.content, 'html.parser')
# # print(soup)
# # print(soup.prettify())
# ##########soup2 = BeautifulSoup(r.content, 'html5lib')
# # print(soup2)
# # print(soup2.prettify())
# ##########with open("/home/jverner/BS.html", "w") as f:
# ##########    f.write(str(soup2))

# url = "/home/jverner/BS.html"
# # response = requests.get(url)
# with open("/home/jverner/BS.html", 'r') as page:
#     soup = BeautifulSoup(page.read(), features='html5lib')

# print(soup)

# # uid = 794
# # url = "http://dochna/test/phonebook/image.asp?ec={}".format(uid)
# # response = requests.get(url, auth=HTTPKerberosAuth())
# # content = response.content
# # soup = BeautifulSoup(content, 'html5lib')

# # print(soup)


# import sys
# from pathlib import Path
# import xml.etree.ElementTree as ET


# class Point:
#     """Cartesian Point."""

#     def __init__(self, point_id, coords_list):
#         super(Point, self).__init__()
#         self.coords = coords_list
#         self.point_id = point_id

#     @property
#     def id(self):
#         return self.point_id

#     @property
#     def id_num(self):
#         return self.point_id.split('_')[-1]

#     @property
#     def x(self):
#         return round(float(self.coords[0]), 4)

#     @property
#     def y(self):
#         return round(float(self.coords[1]), 4)

#     @property
#     def z(self):
#         return round(float(self.coords[2]), 4)


# def main():
#     DEBUG = False
#     if DEBUG:
#         filepath = '/ST/Evektor/UZIV/JVERNER/PROJEKTY/UZIV/DKRUTILEK/2019-03-28_KBL2NAS/190305-export.10mm.kbl'
#         filepath = Path(filepath).resolve()
#     else:
#         filepath = Path(sys.argv[1]).resolve()
#     outfile = f'{filepath.parent}/{filepath.stem}.nas'

#     # Load ETREE
#     with open(filepath, 'rt') as f:
#         tree = ET.parse(f)
#         root = tree.getroot()

#     # Get nodes that will be added to existing 'Control points' (start, end)
#     nodes_dict = {node.get('id'): node.find('Cartesian_point').text for node in root.findall('Node')}

#     # Here will be appended all future lines
#     lines = []

#     points = [Point(point.get('id'), [coord.text for coord in point.findall('Coordinates')])
#               for point in root.findall('Cartesian_point')]

#     for point in points:
#         print(f"{'GRID': <8}{point.id_num: >8}{point.x: >16}{point.y: >8}{point.z: >8}")
#         lines.append(f"{'GRID': <8}{point.id_num: >8}{point.x: >16}{point.y: >8}{point.z: >8}\n")

#     cidx = 1
#     for idx, segment in enumerate(root.findall('Segment'), 1):
#         start_node = segment.find('Start_node').text
#         end_node = segment.find('End_node').text

#         control_points = segment.find('Center_curve').find('Control_points').text.split()
#         control_points = [nodes_dict.get(start_node), *control_points, nodes_dict.get(end_node)]

#         for point_start, point_end in zip(control_points[0:-1], control_points[1:]):
#             point_start_num = point_start.split('_')[-1]
#             point_end_num = point_end.split('_')[-1]
#             print(f"{'CROD': <8}{cidx: >8}{idx: >8}{point_start_num: >8}{point_end_num: >8}")
#             lines.append(f"{'CROD': <8}{cidx: >8}{idx: >8}{point_start_num: >8}{point_end_num: >8}\n")

#             cidx += 1

#     for idx, control_points in enumerate(root.findall('Segment/Center_curve/Control_points'), 1):
#         print(f"{'PROD': <8}{idx: >8}{idx: >8}{'50.': >8}{'0.': >8}")
#         lines.append(f"{'PROD': <8}{idx: >8}{idx: >8}{'50.': >8}{'0.': >8}\n")

#     for idx, center_curve in enumerate(root.findall('Segment/Center_curve'), 1):
#         print(f"$ANSA_NAME_COMMENT;{idx};PROD;{center_curve.get('id')};;NO;NO;NO;")
#         lines.append(f"$ANSA_NAME_COMMENT;{idx};PROD;{center_curve.get('id')};;NO;NO;NO;\n")

#     # Write into a file
#     with open(outfile, 'w') as f:
#         f.writelines(lines)


# if __name__ == '__main__':
#     main()


# def restricted(ls, sums=0):
#     if len(ls) == 0:
#         return sums
#     else:
#         num = ls.pop()
#         sums += num
#         return restricted(ls, sums)


# print(restricted([1, 2, 3]))
# print(restricted([2, 2, 2, 2, 2, 2]))


# ==================================
# =           STATISTIKY           =
# ==================================


# import os
# import sys
# import redis
# import getpass
# from pathlib import Path
# from pprint import pprint
# from datetime import datetime

# redis_host = "avalon"
# redis_port = 6379
# redis_password = ""


# def db_server_up():
#     ret = os.system(f"timeout 0.2 ping -c1 {redis_host} 2>&1 > /dev/null")
#     print("DEBUG: ret:", ret)
#     return True if ret == 0 else False


# def add_redis_count():
#     if not db_server_up():
#         print(f"pocitadlo: {redis_host} not up")
#         return 0

#     try:
#         r = redis.StrictRedis(host=redis_host,
#                               port=redis_port,
#                               password=redis_password,
#                               decode_responses=True)

#         # r.incr(f'prg:{prg_name}:count')
#         # r.incr(f'prg:{prg_name}:{username}')
#         # r.incr(f'prg:{prg_name}:{username}:{dt_day}')
#         levels = [list(), list(), list()]
#         keys = r.keys()
#         for key in keys:
#             if key.count(":") == 1:
#                 levels[0].append(key)
#             elif key.count(":") == 2:
#                 levels[1].append(key)
#             elif key.count(":") == 3:
#                 levels[2].append(key)
#             else:
#                 print("WTF? More than 3 ':' in 'key'???")

#         print("\n=== PROGRAMS ===")
#         for key in sorted(levels[0]):
#             print("{:<3} ... {}".format(r.get(key), key))

#         print("\n=== BY USERS ===")
#         for key in sorted(levels[1]):
#             print("{:<3} ... {}".format(r.get(key), key))

#         print("\n=== BY DATES ===")
#         for key in sorted(levels[2]):
#             print("{:<3} ... {}".format(r.get(key), key))

#     except Exception as e:
#         print(f"pocitadlo: {redis_host} up, but r...")


# if __name__ == '__main__':
#     add_redis_count()


# =====================================================
# =           Multiprocessing - Testing CPU           =
# =====================================================


# #!/usr/bin/env python
# """
# Produces load on all available CPU cores
# """
# from multiprocessing import Pool
# from multiprocessing import cpu_count


# def f(x):
#     while x < 100 000 000:
#         x = x + 1


# if __name__ == '__main__':
#     processes = cpu_count()
#     print('-' * 20)
#     print('Running load on CPU')
#     print('Utilizing %d cores' % processes)
#     print('-' * 20)
#     pool = Pool(processes)
#     pool.map(f, range(processes))


# ===========================================================
# =           Multiprocessing = TESTING SOMETHING           =
# ===========================================================


# ''' listing 6: pi_mp.py
# Multiprocessing based code to estimate the value of PI
# using monte carlo sampling
# Ref: http://math.fullerton.edu/mathews/n2003/montecarlopimod.html
# Uses workers:
# http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool
# '''

# import random
# import multiprocessing
# from multiprocessing import Pool


# #caculate the number of points in the unit circle
# #out of n points
# def monte_carlo_pi_part(n):

#     count = 0
#     for i in range(n):
#         x = random.random()
#         y = random.random()

#         # if it is within the unit circle
#         if x * x + y * y <= 1:
#             count = count + 1

#     #return
#     return count


# if __name__ == '__main__':

#     np = multiprocessing.cpu_count()
#     np = 1
#     print('You have {0:1d} CPUs'.format(np))

#     # Nummber of points to use for the Pi estimation
#     n = 500000000

#     # iterable with a list of points to generate in each worker
#     # each worker process gets n/np number of points to calculate Pi from

#     part_count = [n // np for i in range(np)]

#     #Create the worker pool
#     # http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool
#     pool = Pool(processes=np)

#     # parallel map
#     count = pool.map(monte_carlo_pi_part, part_count)

#     print("Estimated value of Pi:: ", sum(count) / n * 4)


# ===============================================================
# =           SUBPROCESS tests and tries and examples           =
# ===============================================================


# import subprocess as sp

# sp.run('ls')
# sp.run('ls -ltr', shell=True)  # Security hazard when using untrusted input. Only for COMMANDS.
# sp.run(['ls', '-ltr'])  # Without security risk
# We ar not capturing OUTPUT, it goes into STDOUT - console

# Save into a VARIABLE
# p1 = sp.run(['ls', '-ltr'])  # p1: CompletedProcess(args=['ls', '-ltr'], returncode=0)
# print(help(p1))  # what is CompletedProcess

# Some useful things
# print(p1.args)  # ['ls', '-ltr']
# print(p1.returncode)  # 0
# print(p1.stdout)  # None (suprising???) Because it's sending stdout to console...

# p1 = sp.run(['ls', '-ltr'], capture_output=True)  # caputure_output python3.7++
# print(p1.stdout)  # in BYTES format...
# print(p1.stdout.decode('UTF-8'))  # now showing nice and pretty

# If we don't want use DECODE, then pass argument TEXT
# p1 = sp.run(['ls', '-ltr'], capture_output=True, text=True)

# WITHOUT capture_output=True
# p1 = sp.run(['ls', '-ltr'], stdout=sp.PIPE, text=True)  # capture_output=True in the background. stderr in stdout too
# print(p1.stdout)

# Redirect stdout to FILE
# with open('output.txt', 'w') as f:
#     p1 = sp.run(['ls', '-ltr'], stdout=f, text=True)

# What about errors
# p1 = sp.run(['ls', '-ltr', 'sldkfjsd'], capture_output=True, text=True)  # python does not throw exception...
# print(p1.returncode)  # 2
# print(p1.stdout)  # ''
# print(p1.stderr)  # ls: cannot access sldkfjsd: No such file or directory

# If I want python to raise an ERROR,
# p1 = sp.run(['ls', '-ltr', 'sldkfjsd'], capture_output=True, text=True, check=True)  # throws exception

# ## Redirecting errors
# p1 = sp.run(['ls', '-ltr', 'sldkfjsd'], stdout=sp.PIPE, stderr=sp.DEVNULL, text=True)  # redirected error
# print(p1.stdout)  # ''
# print(p1.stderr)  # None

# ## Output from 1 command as input from the other
# ## Cat file | grep something
# p1 = sp.run(['cat', 'output.txt'], capture_output=True, text=True)
# print(p1.stdout)
# p2 = sp.run(['grep', '-n', 'out'], capture_output=True, text=True, input=p1.stdout)  # -n linenumber
# print(p2.stdout)  # 3:-rw-rw-r--. 1 jverner statikau     0 Jul 25 10:39 output.txt

# ## The SAME thing BUT more vulnerable
# p3 = sp.run('cat output.txt | grep -n out', capture_output=True, text=True, shell=True)
# print(p3.stdout)


# ======================================================
# =           PyQT5 - Very simpleappliaction           =
# ======================================================


# from PyQt5 import QtWidgets, uic

# app = QtWidgets.QApplication([])
# dlg = uic.loadUi("./designer.ui")

# def Convert():
#     dlg.txtTo.setText(str(float(dlg.txtFrom.text()) * 2))

# dlg.cmdConvert.clicked.connect(Convert)

# dlg.show()
# app.exec()


# # Authors: Clemens Brunner <clemens.brunner@gmail.com>
# #
# # License: BSD (3-clause)
# import sys
# from PyQt5.QtWidgets import QDialog, QVBoxLayout, QListWidget, QDialogButtonBox
# from PyQt5.QtCore import pyqtSlot
# from PyQt5 import QtWidgets, uic

# class PickChannelsDialog(QDialog):
#     def __init__(self, parent=None, channels=['jedna', 'dva'], selected=None, title="Pick channels"):
#         super().__init__(parent)
#         self.setWindowTitle(title)
#         if selected is None:
#             selected = []
#         self.initial_selection = selected
#         vbox = QVBoxLayout(self)
#         self.channels = QListWidget()
#         self.channels.insertItems(0, channels)
#         self.channels.setSelectionMode(QListWidget.ExtendedSelection)
#         for i in range(self.channels.count()):
#             if self.channels.item(i).data(0) in selected:
#                 self.channels.item(i).setSelected(True)
#         vbox.addWidget(self.channels)
#         self.buttonbox = QDialogButtonBox(QDialogButtonBox.Ok |
#                                           QDialogButtonBox.Cancel)
#         vbox.addWidget(self.buttonbox)
#         self.buttonbox.accepted.connect(self.accept)
#         self.buttonbox.rejected.connect(self.reject)
#         self.channels.itemSelectionChanged.connect(self.toggle_buttons)
#         self.toggle_buttons()  # initialize OK button state

#     @pyqtSlot()
#     def toggle_buttons(self):
#         """Toggle OK button.
#         """
#         selected = [item.data(0) for item in self.channels.selectedItems()]
#         if selected != self.initial_selection:
#             self.buttonbox.button(QDialogButtonBox.Ok).setEnabled(True)
#         else:
#             self.buttonbox.button(QDialogButtonBox.Ok).setEnabled(False)


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     w = PickChannelsDialog()
#     w.show()
#     sys.exit(app.exec_())


# ===================================================================
# =           PyQT5 - Password application with 2 windows           =
# ===================================================================


# import sys
# from PyQt5 import QtWidgets, QtCore


# class LoginWindow(QtWidgets.QWidget):

#     got_password = QtCore.pyqtSignal(str)

#     def __init__(self):
#         super(LoginWindow, self).__init__()

#         self.password = QtWidgets.QLineEdit()
#         self.password.setEchoMode(QtWidgets.QLineEdit.Password)
#         send_button = QtWidgets.QPushButton("Send")
#         close_button = QtWidgets.QPushButton("Close")

#         send_button.clicked.connect(self.send_clicked)
#         close_button.clicked.connect(self.close)

#         layout = QtWidgets.QHBoxLayout()
#         layout.addWidget(self.password)
#         layout.addWidget(send_button)
#         layout.addWidget(close_button)

#         self.setLayout(layout)
#         self.setWindowTitle("Login")
#         self.setMinimumWidth(350)

#     def send_clicked(self):
#         self.got_password.emit(self.password.text())


# class MyWindow(QtWidgets.QWidget):

#     def __init__(self):
#         super(MyWindow, self).__init__()

#         self.login = LoginWindow()
#         self.login.got_password.connect(self.show_it)

#         self.edit = QtWidgets.QLineEdit()
#         button = QtWidgets.QPushButton("Get input from window")
#         button.clicked.connect(self.get_login)
#         layout = QtWidgets.QVBoxLayout()
#         layout.addWidget(self.edit)
#         layout.addWidget(button)
#         self.setLayout(layout)

#     def get_login(self):
#         self.login.show()

#     def show_it(self, the_password):
#         self.edit.setText(the_password)


# if __name__ == '__main__':

#     app = QtWidgets.QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec_())


# ===============================================
# =           HOW TO RESOLVE ENCODING           =
# ===============================================


# import chardet
# Get the text format:
# with open(filepath, 'rb') as f:
#     rawdata = f.read()
#     result = chardet.detect(rawdata)
#     charenc = result['encoding']
#     print("DEBUG: charenc:", charenc)
#     sys.exit()


# ====================================================================
# =           PyQT5 - SYSTEM TRAY ICON with EXIT and so on           =
# ====================================================================


# import os
# import sys
# from PyQt5 import QtWidgets, QtGui


# class SystemTraiIcon(QtWidgets.QSystemTrayIcon):
#     def __init__(self, icon, parent=None):
#         QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
#         self.setToolTip(f"Hmm tooltip verze...")

#         menu = QtWidgets.QMenu(parent)

#         open_app = menu.addAction("Open Terminal")
#         open_app.triggered.connect(self.open_notepad)
#         open_app.setIcon(QtGui.QIcon("icon.png"))

#         open_sth = menu.addAction("Open something")
#         open_sth.triggered.connect(self.open_something)
#         open_sth.setIcon(QtGui.QIcon("warn.png"))

#         menu.addSeparator()

#         exit_ = menu.addAction("Exit")
#         exit_.triggered.connect(lambda: sys.exit())
#         exit_.setIcon(QtGui.QIcon("Hmm"))

#         self.setContextMenu(menu)
#         self.activated.connect(self.onTrayIconActivated)

#     def onTrayIconActivated(self, reason):
#         if reason == self.DoubleClick():
#         # if reason == self.Trigger:
#             self.open_notepad()

#     def open_notepad(self):
#         os.system('konsole')

#     def open_something(self):
#         os.system('konsole')


# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     w = QtWidgets.QWidget()
#     tray_icon = SystemTraiIcon(QtGui.QIcon("icon.png"), w)
#     tray_icon.show()
#     tray_icon.showMessage("Tiitle of the win", "Yo there, message")
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()





# =====================================================
# =           PyQT5 - Simple treeView model           =
# =====================================================


# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

# tree_data = [
#     ("Alice", [
#         ("Keys", []),
#         ("Purse", [
#             ("Cellphone", [])
#         ])
#     ]),
#     ("Bob", [
#         ("Wallet", [
#             ("Credit card", []),
#             ("Money", [])
#         ])
#     ])
# ]


# class Window(QWidget):

#     def __init__(self):

#         QWidget.__init__(self)

#         self.treeView = QTreeView()
#         self.tableView = QTableView()
#         self.tableView.horizontalHeader().setStretchLastSection(True)

#         self.model = QStandardItemModel()
#         self.addTreeItems(self.model, tree_data)
#         self.treeView.setModel(self.model)

#         treeSelectionModel = self.treeView.selectionModel()
#         treeSelectionModel.selectionChanged.connect(self.addTableItems)

#         layout = QHBoxLayout(self)
#         layout.addWidget(self.treeView)
#         layout.addWidget(self.tableView)

#     def addTreeItems(self, parent, elements):

#         for text, children in elements:
#             item = QStandardItem(text)
#             parent.appendRow(item)
#             if children:
#                 self.addTreeItems(item, children)

#     def addTableItems(self, selected, deselected):

#         # Find the top-level item in the tree.
#         treeIndex = selected.indexes()[0]

#         parent = treeIndex.parent()
#         while parent.isValid():
#             treeIndex = parent
#             parent = parent.parent()

#         # treeIndex is now a model index corresponding to a top-level item

#         self.tableModel = QStandardItemModel()

#         for row in range(self.model.rowCount(treeIndex)):
#             items = []
#             for column in range(self.model.columnCount(treeIndex)):
#                 text = self.model.index(row, column, treeIndex).data().toString()
#                 items.append(QStandardItem(text))

#             self.tableModel.appendRow(items)

#         self.tableView.setModel(self.tableModel)


# if __name__ == "__main__":

#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())




