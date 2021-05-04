"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

File: breakoutgraphics.py
Name: 林坤毅 Jordan
-------------------------
This python file will create a class named BreakoutGraphics for the break out game.
This class will contain the building block for creating that game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10       # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):
        """
        The basic parameters for building these breakout game.

        :param ball_radius: The radius of the ball.
        :param paddle_width: The width of the paddle.
        :param paddle_height: The height of the paddle.
        :param paddle_offset: The distance between paddle and the bottom of the window.
        :param brick_rows: The number of rows in bricks.
        :param brick_cols: The number of column in bricks.
        :param brick_width: The width of each brick.
        :param brick_height: The height of each brick.
        :param brick_offset: The distance between the first row of bricks and the top of the window.
        :param brick_spacing: The spacing between each brick.
        :param title: The name of this program.
        """

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window_width-paddle_width)/2, y=(self.window_height-paddle_offset))
        self.paddle.filled = True
        self.paddle.color = 'black'
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(self.window_width-ball_radius*2)/2, y=(self.window_height-ball_radius*2)/2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)
        self.ball_radius = ball_radius

        # Default initial velocity for the ball
        self.__dx = 0       # self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = 0       # self.__dy = INITIAL_Y_SPEED
                            # if random.random() > 0.5:
                            #     self.__dx = -self.__dx
                            # The above is the mistake I made during doing this homework.

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                # Crucial point! This can't be placed at the outside of for loop.
                brick = GRect(brick_width, brick_height)
                brick.x = (brick_width+brick_spacing)*i
                brick.y = brick_offset+(brick_height+brick_spacing)*j
                brick.filled = True
                if j < 2:
                    brick.fill_color = 'red'
                elif j < 4:
                    brick.fill_color = 'orange'
                elif j < 6:
                    brick.fill_color = 'yellow'
                elif j < 8:
                    brick.fill_color = 'green'
                elif j < 10:
                    brick.fill_color = 'blue'
                elif j < 12:
                    brick.fill_color = 'teal'
                elif j < 14:
                    brick.fill_color = 'chocolate'
                self.window.add(brick)

        # Initialize our mouse listeners
        onmouseclicked(self.is_start_game)
        onmousemoved(self.moving_paddle)

        # Total bricks
        self.total_bricks = brick_cols * brick_rows

    def is_start_game(self, event):  # Crucial point!!! Stuck here for three days! The initial velocity!
        """
        The check point of the game start.

        :param event: The information of the mouse, including (x,y) of it.
        :return: Set the __dx and __dy of the ball.
        """
        if event.x != -1 and event.y != -1 and self.__dx == 0 and self.__dy == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def check_for_collisions(self):
        """
        Four check points of the ball to check the collision with objects.

        :return: boolean value. Build the information of object that the ball collide with.
        """
        one = self.window.get_object_at(self.ball.x, self.ball.y)
        two = self.window.get_object_at(self.ball.x + 2*self.ball_radius, self.ball.y)
        three = self.window.get_object_at(self.ball.x, self.ball.y + 2*self.ball_radius)
        four = self.window.get_object_at(self.ball.x + 2*self.ball_radius, self.ball.y + 2*self.ball_radius)
        if one is not None:
            self.obj = self.window.get_object_at(self.ball.x, self.ball.y)
            return True
        elif two is not None:
            self.obj = self.window.get_object_at(self.ball.x + 2*self.ball_radius, self.ball.y)
            return True
        elif three is not None:
            self.obj = self.window.get_object_at(self.ball.x, self.ball.y + 2*self.ball_radius)
            return True
        elif four is not None:
            self.obj = self.window.get_object_at(self.ball.x + 2*self.ball_radius, self.ball.y + 2*self.ball_radius)
            return True

    def check_object_type(self):
        """
        The objects above the half of the window height are bricks and the object below the half of the window height is paddle.

        :return: boolean value. Bricks return True and paddle returns False.
        """
        if self.ball.y > self.window.height/2:
            return True
        else:
            return False

    def moving_ball(self):
        """
        The method for moving ball.

        :return: The moving result of the ball.
        """
        self.ball.move(self.__dx, self.__dy)

    def moving_paddle(self, event):
        """
        The method for moving paddle.

        :param event: The information of the mouse, including (x,y) of it.
        :return: The moving result of the paddle.
        """
        if event.x - self.paddle_width/2 >= 0 and event.x-self.paddle_width/2 <= self.window_width-self.paddle_width:
            self.paddle.x = event.x - self.paddle_width / 2

    def reset_ball(self):
        """
        As the ball falls below the paddle and the game hasn't overed, the ball will be reset to the original position.

        :return: The ball at the original position.
        """
        self.ball = GOval(self.ball_radius * 2, self.ball_radius * 2, x=(self.window_width - self.ball_radius * 2) / 2,
                          y=(self.window_height - self.ball_radius * 2) / 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)
        self.ball_radius = self.ball_radius
        self.__dx = 0
        self.__dy = 0

    def set_dx(self, new_dx):
        """
        Set the new __dx.

        :param new_dx: The new dx.
        :return: __dx.
        """
        self.__dx = new_dx

    def set_dy(self, new_dy):
        """
        Set the new __dy.

        :param new_dy: The new dy.
        :return: __dy.
        """
        self.__dy = new_dy

    def get_dx(self):
        """
        Get the information of __dx from class BreakoutGraphics.

        :return: The __dx for the ball.
        """
        return self.__dx

    def get_dy(self):
        """
        Get the information of __dy from class BreakoutGraphics.

        :return: The __dy for the ball.
        """
        return self.__dy

    def set_dx_collision(self, new_dx):
        """
        Set the new __dx for ball after colliding with bricks.

        :param new_dx: The new dx.
        :return: __dx.
        """
        if random.random() > 0.5:
            self.__dx = new_dx
        else:
            self.__dx = -new_dx

    def game_over(self):
        """
        The label for game over.

        :return: The label for game over.
        """
        label = GLabel('Game Over!!!')
        # The condition below is for 10*10 bricks.
        # If coder change the number of rows or columns, the size would probably not fit.
        label.font = '-40'
        self.window.add(label, x= self.window_width/2 - 100, y=self.window_height/2 + 100)

    def game_win(self):
        """
        The label for game win.

        :return: The label for game win.
        """
        label = GLabel('You Win!!!')
        # The condition below is for 10*10 bricks.
        # If coder change the number of rows or columns, the size would probably not fit.
        label.font = '-40'
        self.window.add(label, x=self.window_width / 2 - 100, y=self.window_height / 2 + 100)