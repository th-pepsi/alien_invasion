class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 3
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60

        self.bullets_allowed = 100

        # 外星人设置
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.alien_number = 12


    