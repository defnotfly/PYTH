import tkinter as tk
import random


root = tk.Tk()
root.title("Catch the Target Game")
root.geometry("400x400")

# Create the game canvas
canvas = tk.Canvas(root, width=400, height=400, bg="lightblue")
canvas.pack()

# Create the player and target circles
player = canvas.create_oval(10, 10, 30, 30, fill="blue")
target = canvas.create_oval(50, 50, 70, 70, fill="red")

# Initial positions of the player and target
player_x, player_y = 20, 20
target_x, target_y = random.randint(0, 380), random.randint(0, 380)

# Dictionary to track which keys are pressed
keys_pressed = {
    'Up': False,
    'Down': False,
    'Left': False,
    'Right': False
}

step_size = 10

# Function to move the player based on keys pressed
def move_player():
    global player_x, player_y

    if keys_pressed['Up'] and keys_pressed['Left']:
        if player_y > 0 and player_x > 0:
            player_y -= step_size
            player_x -= step_size
    elif keys_pressed['Up'] and keys_pressed['Right']:
        if player_y > 0 and player_x < 380:
            player_y -= step_size
            player_x += step_size
    elif keys_pressed['Down'] and keys_pressed['Left']:
        if player_y < 380 and player_x > 0:
            player_y += step_size
            player_x -= step_size
    elif keys_pressed['Down'] and keys_pressed['Right']:
        if player_y < 380 and player_x < 380:
            player_y += step_size
            player_x += step_size
    elif keys_pressed['Up']:
        if player_y > 0:
            player_y -= step_size
    elif keys_pressed['Down']:
        if player_y < 380:
            player_y += step_size
    elif keys_pressed['Left']:
        if player_x > 0:
            player_x -= step_size
    elif keys_pressed['Right']:
        if player_x < 380:
            player_x += step_size

    # Update the player position on the canvas
    canvas.coords(player, player_x, player_y, player_x+20, player_y+20)

    # Continuously call move_player every 50 milliseconds
    root.after(50, move_player)

    # Check for collision with the target
    check_collision()

# Move the target randomly every second
def move_target():
    global target_x, target_y
    
    target_x = random.randint(0, 380)
    target_y = random.randint(0, 380)
    
    canvas.coords(target, target_x, target_y, target_x+20, target_y+20)
    
    root.after(1000, move_target)

# Check if the player caught the target
def check_collision():
    player_coords = canvas.coords(player)
    target_coords = canvas.coords(target)

    if (player_coords[0] < target_coords[2] and player_coords[2] > target_coords[0] and
        player_coords[1] < target_coords[3] and player_coords[3] > target_coords[1]):
        
        canvas.create_text(200, 200, text="NAHULI MO PARE", font=("League Spartan", 20), fill="green")
        move_target()

# Handle key press events
def on_key_press(event):
    if event.keysym in keys_pressed:
        keys_pressed[event.keysym] = True

# Handle key release events
def on_key_release(event):
    if event.keysym in keys_pressed:
        keys_pressed[event.keysym] = False

# Bind key press and key release events
root.bind("<KeyPress>", on_key_press)
root.bind("<KeyRelease>", on_key_release)

# Start the game
move_player()
move_target()
root.mainloop()