__VERSION__ = "0.1.8"


if __package__ is None or __package__ == '':
    import video 

else:
    from .video import *
