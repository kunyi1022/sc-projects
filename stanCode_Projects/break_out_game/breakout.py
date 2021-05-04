"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

File: breakout.py
Name: 林坤毅 Jordan
-------------------------
This program will demo a Break Out game that player have three lives to lose if the ball fall below the paddle.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constant setting for the game
FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    """
    This program show the detail condition for break out game and could be divided to five steps:

    First, check the lives that player have.
    Second, check the total bricks left on the window.
    Third, set the collision condition with wall.
    Forth, set the collision condition with bricks and paddle.
    Finally, set the result that ball move below the paddle.
    """
    graphics = BreakoutGraphics()

    # Add animation loop here!
    lives = NUM_LIVES
    while True:
        if lives > 0:
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            if graphics.total_bricks > 0:

                # Collision with wall
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    graphics.set_dx(-graphics.get_dx())
                if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    graphics.set_dy(-graphics.get_dy())

                # Collision with bricks or paddle
                if graphics.check_for_collisions() is True:
                    # Collision with paddle
                    if graphics.check_object_type() is True:
                        graphics.set_dy(-graphics.get_dy())
                        # Promise the ball will not stuck in the paddle.
                        # I discuss this idea with classmate 李佳謙
                        if graphics.get_dy() > 0:
                            graphics.set_dy(-graphics.get_dy())

                    # Collision with bricks
                    elif graphics.check_object_type() is False:
                        graphics.window.remove(graphics.obj)
                        graphics.total_bricks -= 1
                        graphics.set_dx_collision(graphics.get_dx())
                        graphics.set_dy(-graphics.get_dy())

                # The condition that lives will decrease.
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    lives -= 1
                    graphics.window.remove(graphics.ball)
                    graphics.reset_ball()
                pause(FRAME_RATE)
            # Clear all bricks
            else:
                graphics.game_win()
                break
        # The lives is zero and player is lose.
        else:
            graphics.game_over()
            break


if __name__ == '__main__':
    main()
