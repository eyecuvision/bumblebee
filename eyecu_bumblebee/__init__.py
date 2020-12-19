
if __package__ is None or __package__ == '':
    import video 
    import image

else:
    from . import video
    from . import image
