class camera(object):
    zoom_in_factor = 1.2
    zoom_out_factor = 1 / zoom_in_factor

    def __init__(self, game):
        self.game = game
        self.left = 0
        self.right = self.game.width
        self.bottom = 0
        self.top = self.game.height
        self.zoom_level = 1
        self.zoomed_width = self.game.width
        self.zoomed_height = self.game.height

    def init_gl(self, width, height):
        self.width = width
        self.height = height
        glViewport(0, 0, self.width, self.height)

    def draw(self):
        glPushMatrix()
        glOrtho(self.left, self.right, self.bottom, self.top, 1, -1)
        glTranslatef(-self.game.player.sprite.x + self.width / 2, -self.game.player.sprite.y + self.height / 2, 0)
        self.game.clear()
        if self.game.runGame:
            for sprite in self.game.mapDraw_3:
                self.game.mapDraw_3[sprite].draw()
        glPopMatrix()
        print(self.game.player.sprite.x, self.game.player.sprite.y)

    def scroll(self, dy):
        f = self.zoom_in_factor if dy > 0 else self.zoom_out_factor if dy < 0 else 1
        if .1 < self.zoom_level * f < 2:
            self.zoom_level *= f

            vx = self.game.player.sprite.x / self.width
            vy = self.game.player.sprite.y / self.height

            vx_in_world = self.left + vx * self.zoomed_width
            vy_in_world = self.bottom + vy * self.zoomed_height

            self.zoomed_width *= f
            self.zoomed_height *= f

            self.left = vx_in_world - vx * self.zoomed_width
            self.right = vx_in_world + (1 - vx) * self.zoomed_width
            self.bottom = vy_in_world - vy * self.zoomed_height
            self.top = vy_in_world + (1 - vy) * self.zoomed_height
