from tkinter import *

from Window.BaseWindow import BaseWindow


class MainWindow(BaseWindow):
    """
        main window with buttons 'start' and 'cancel', and text-widget for the information about performance of the task
        inherit BaseWindow object
    """

    def __init__(self, master=None):
        super().__init__(master)

    def _conf(self, **kwargs):
        """
            function to create settings to the window
        """
        super()._conf(title='spotu')

    def _create_variables(self):
        """
            function to create variables for the window
        """
        super()._create_variables()

    def _create_widgets(self):
        """
            function to create widgets for the window
        """
        super()._create_widgets()

        # label where where basic widgets are located
        self.__main_label = Label(self,
                                   bg=self['bg'],
                                  width=self.width,
                                  height=self.height,
                                  )

        # perform button
        self.__start_btn = Button(self.__main_label,
                                  width=20 if (self.width >= 300) else int(self.width / 15),
                                  text='start',
                                  bg='#003647',
                                  font=10 if (self.width >= 300) else int(self.width / 30),
                                  foreground='#FFFFFF',
                                  activebackground='#006587',
                                  )

        # widgets for the displaying of the process
        self.console = Text(self.__main_label,
                            width=50 if (self.width >= 300) else int(self.width / 6),
                            height=20 if (self.height >= 300) else int(self.width / 15),
                            background='#7A7A7A',
                            foreground='#FFFFFF',
                            )

    def _create_layouts(self):
        """
            function to create layouts for the window
        """
        super()._create_layouts()

        self.__main_label.pack(anchor=CENTER)

        self.__start_btn.grid(row=0, column=0,
                              pady=50 if (self.width >= 300) else int(self.width / 6)
                              )

        self.console.grid(row=1, column=0)

    def _create_bindings(self):
        """
            function to create bindings for the window
        """
        super()._create_bindings()

        self.__start_btn.bind('<Button-1>', self._perform)

    def _perform(self, event=None):
        """
            function to perform the preassigned task
        """
        print('PERFORM')
