from StartWindow import StartWindow


class Navigation (object):
    def __init__(self):

        self.current_window= "StartWindow"

        self.props= None

        self.windows= {

            "StartWindow":StartWindow
        }