import sys
sys.path.append("..")
from pandaeditor import *

class GridLayout():

    def __init__(self):
        self.entity = None

        self.origin = (0,0)
        self.overflow = True
        self.spacing = (.001,0)
        self.max_x = 3
        self.rows = 1
        self.limit = None

        # self.model = loader.loadModel('internal_models/' + 'quad' + '.egg')
        # self.model.reparentTo(self)

    def update_grid(self):
        if not self.entity:
            print('grid_layout is not attached to an Entity')
            return

        x = 0
        for i in range(len(self.entity.children)):
            c = self.entity.children[i]
            c.origin = self.origin
            prev_x = 0
            c.y = 0
            if i <= 0:
                c.x = 0
            else:
                c.x = (
                    (self.entity.children[i-1].x
                    + self.entity.children[i-1].scale_x
                    + self.spacing[0])
                    * 1)

            self.width = c.x


        for c in self.entity.children:
            c.x -= (self.origin[0] + .5) * self.width


    # def __setattr__(self, name, value):
    #     try:
    #         super().__setattr__(name, value)
    #     except:
    #         pass
    #
    #     # self.update_grid()
    #
    #
    #     # copied from entity
    #     if name == 'origin' and self.model:
    #         new_value = Vec3()
    #
    #         if len(value) % 2 == 0:
    #             for i in range(0, len(value), 2):
    #                 new_value.addX(value[i])
    #                 new_value.addY(value[i+1])
    #             new_value.addZ(self.model.getY())
    #
    #         if len(value) % 3 == 0:
    #             for i in range(0, len(value), 3):
    #                 new_value.addX(value[i])
    #                 new_value.addY(value[i+1])
    #                 new_value.addZ(value[i+2])
    #
    #         self.model.setPos(-new_value[0],
    #                             -new_value[2],
    #                             -new_value[1])
    #         object.__setattr__(self, name, new_value)