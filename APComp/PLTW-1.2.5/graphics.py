import turtle
import math
import game

#Game window object
class GameWindow:
    #Make window, scene renderer, game, and bind functions
    def __init__(self, size_x, size_y, game_tick=50):
        self.window = turtle.Screen()
        self.window.tracer(False)
        self.window.setup(width=800, height=600)

        self.scene = Scene(self.window)
        self.game = game.Game(game_tick)
        self.game_tick = game_tick

        self.game.set_times_up(self.times_up)
        self.game.set_missed(self.missed)
        self.game.set_scored(lambda: None)
        self.game.gen_goal()
        self.state = "selection" 

    #Start the main and game loops
    def start_main(self, frame_rate=40):
        self.reset()
        self.window.onkeypress(lambda: self.reset(), 'r')
        self.window.ontimer(lambda: self.main_loop(frame_rate), int(1000/frame_rate))
        self.window.ontimer(lambda: self.game_loop(self.game_tick), int(1000/self.game_tick))

    #Main loop handles drawing everything to the screen
    def main_loop(self, frame_rate):
        if self.state == "selection" or self.state == "game_over": 
            self.window.update()
            self.window.ontimer(lambda: self.main_loop(frame_rate), int(1000/frame_rate))
            return
        
        self.scene.draw_goal(self.game.get_goal())
        self.scene.draw_launch(self.game.get_angle())
        self.scene.draw_score_time(self.game.get_score(), self.game.get_time_elapsed())

        self.window.update()
        self.window.ontimer(lambda: self.main_loop(frame_rate), int(1000/frame_rate))

    #Game loop handles game steps
    def game_loop(self, game_tick):
        if self.state == 'game':
            self.game.update_step()
            self.scene.move_ball(self.game.get_ball_pos())
        self.window.ontimer(lambda: self.game_loop(game_tick), int(1000/game_tick))

    #Times up function binding
    def times_up(self):
        self.state = "game_over"
        self.scene.draw_game_over_scene(self.game.get_score())

    #Poll user for input for selected game mode
    def get_selection(self):
        self.window.onkeypress(self.timed_selected, "t")
        self.window.onkeypress(self.consecutive_selected, "c")
        self.window.listen()
   
    #Configure game for timed mode
    def timed_selected(self):
        self.window.onkeypress(None, "t")
        self.window.onkeypress(None, "c")
        self.scene.set_game_mode('timed')
        self.game.set_game_mode('timed')
        self.scene.draw_game_scene()
        self.state = "game"
        self.game.start_timer()
        self.window.onkeypress(self.game.start_launch, 'space')

    #Configure game for consecutive mode
    def consecutive_selected(self):
        self.window.onkeypress(None, "t")
        self.window.onkeypress(None, "c")
        self.scene.set_game_mode('consecutive')
        self.game.set_game_mode('consecutive')
        self.scene.draw_game_scene()
        self.state = "game"
        self.game.start_timer()
        self.window.onkeypress(self.game.start_launch, 'space')

    #Missed shot binding
    def missed(self):
        if self.game.get_game_mode() == 'consecutive':
            self.state = "game_over"
            self.scene.draw_game_over_scene(self.game.get_score())

    #Reset the game to the selection screen
    def reset(self):
        self.scene.clear()
        self.game.reset()
        self.game.goals = 0
        self.state = "selection"
        self.scene.draw_selection_scene()
        self.get_selection()

#Draws everything 
class Scene:
    #COnfigure window, text turtle, player, ball, and game drawer
    def __init__(self, window):
        self.window = window
        self.window.register_shape("player.gif")
        self.font = ('Arial', 30, 'normal')
        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()

        self.player = turtle.Turtle(shape="player.gif") 
        self.player.hideturtle()
        self.player.penup()
        self.player.goto(-380, -220)

        self.scene_drawer = turtle.Turtle()
        self.scene_drawer.hideturtle()
        self.scene_drawer.penup()

        self.game_mode = 'timed'

        self.window = window
        self.font = ('Arial', 30, 'normal')
        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()

        self.goal_drawer = turtle.Turtle()
        self.goal_drawer.hideturtle()
        self.goal_drawer.penup()
        self.goal_drawer.pensize(20)
        self.goal_drawer.pencolor('red')

        self.launch_drawer = turtle.Turtle()
        self.launch_drawer.hideturtle()

        self.window.register_shape("basketball.gif")
        self.ball = turtle.Turtle(shape='basketball.gif')
        self.ball.hideturtle()
        self.ball.turtlesize(30,30)
        self.ball.penup()
        self.ball.goto(-300,-210)

    #Draw a simple selection screen with text instructions
    def draw_selection_scene(self):
        self.window.bgcolor("Black")
        self.clear()
        self.player.hideturtle()
        self.ball.hideturtle()
        self.writer.goto(0,0)
        self.writer.color("White")
        self.writer.write("Press t to select Timed Game Mode\nPress c to select Consecutive Game Mode\nPress r to restart at any time", font=self.font, align='center')

    #Draw a simple game over scene with the final score and instructions
    def draw_game_over_scene(self, goals):
        self.window.bgcolor("Black")
        self.clear()
        self.player.hideturtle()
        self.ball.hideturtle()
        self.writer.goto(0,0)
        self.writer.color("White")
        self.writer.write(f"Game Over\nGoals scored: {goals}\nPress r to restart", font=self.font, align='center')

    #Draw the game scene
    def draw_game_scene(self):
        self.clear()
        self.player.showturtle()
        self.ball.showturtle()
        self.window.bgcolor('#91d1ff')
        self.scene_drawer.goto(-400, -300 + 50)
        self.scene_drawer.fillcolor('green')
        self.scene_drawer.begin_fill()
        self.scene_drawer.goto(400, -300 + 50)
        self.scene_drawer.goto(400, -300)
        self.scene_drawer.goto(-400, -300)
        self.scene_drawer.goto(-400, -300 + 50)
        self.scene_drawer.end_fill()
        
    #Configure the game mode
    def set_game_mode(self, mode):
        self.game_mode = mode

    #Draw the score and time over the screen
    def draw_score_time(self, score, time):
        self.writer.clear()
        self.writer.goto(-380,230)
        self.writer.color('black')
        self.writer.write(f"Goals: {score}   Time: {time}", font=self.font)

    #Draw a goal at the specified height on the right side
    def draw_goal(self, height):
        self.goal_drawer.clear()
        self.goal_drawer.penup()
        self.goal_drawer.goto(400-30, height - 300)
        self.goal_drawer.seth(90)
        self.goal_drawer.pendown()
        self.goal_drawer.forward(140)
        self.goal_drawer.penup()

    #Clear all turtles
    def clear(self):
        self.writer.clear()
        self.scene_drawer.clear()
        self.goal_drawer.clear()
        self.launch_drawer.clear()

    #Draw launch angle line (dashed)
    def draw_launch(self, angle):
        self.launch_drawer.clear()
        self.launch_drawer.penup()
        self.launch_drawer.goto(-360, -220)
        self.launch_drawer.seth(angle)
        self.launch_drawer.forward(40)
        for x in range(10):
            self.launch_drawer.pendown()
            self.launch_drawer.forward(10)
            self.launch_drawer.penup()
            self.launch_drawer.forward(10)

    #Move the ball to a new position
    def move_ball(self, ball_pos):
        self.ball.goto(ball_pos)
