from tkinter import Tk


class BaseWindow(Tk):

    def __init__(self, master=None):
        super().__init__(master)

        self._create_variables()
        self._conf()
        self._create_widgets()
        self._create_layouts()
        self._create_bindings()

    def _create_variables(self):
        """
            function to create base variables for the window
        """
        self.height =500 if (self.winfo_screenheight() > 1000) else int(self.winfo_screenheight() / 3)
        self.width = 500 if (self.winfo_screenwidth() > 1000) else int(self.winfo_screenwidth() / 3)

    def _conf(self, *, title='window'):
        """
            function to set the base settings of the window
        """
        self.protocol('WM_DELETE_WINDOW', self.quit)
        self.resizable(False, False)
        self.config(bg='#000000')
        self.geometry('{}x{}'.format(self.width, self.height))

        self.title(title)

    def _create_widgets(self):
        """
            function to create base widgets for the window
        """
        pass

    def _create_layouts(self):
        """
            function to create base layouts for the window
        """
        pass

    def _create_bindings(self):
        """
            function to create base bindings for the window
        """
        pass
