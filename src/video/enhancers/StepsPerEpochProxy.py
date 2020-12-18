

class StepsPerEpochProxy():

    def __init__(self,src,steps_per_epoch = 300):

        self.src = src
        self.steps_per_epoch = steps_per_epoch

    def __getattr__(self, item):
        return getattr(self.src,item)

    def __getitem__(self, item):
        return self.src.__getitem__(item)

    def __len__(self):
        return self.steps_per_epoch