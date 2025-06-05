#                                                                                                                             Toy Collector
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import pygame  # Imports the pygame module for game development
from random import randint  # Imports the randint function to generate random integers
from pygame import mixer  # Imports the mixer module for handling sound effects and music

pygame.init()  # Initializes all imported pygame modules
pygame.font.init()  # Initializes the font module separately for rendering text

pygame.display.set_caption("Toy Collector")  # Sets the title of the game window

ICON = pygame.image.load("C:\\Users\\15715\\OneDrive\\Toy Collector\\Icon\\toy_box.png")  # Loads the icon image for the window
pygame.display.set_icon(ICON)  # Sets the game window icon to the loaded image

mixer.music.load("C:\\Users\\15715\\OneDrive\\Toy Collector\\Music\\Run-Amok(chosic.com).mp3")  # Loads background music file
mixer.music.play(-1)  # Starts playing music in an infinite loop

WIDTH, HEIGHT = 900, 700  # Sets the screen width and height
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # Creates the game window with specified dimensions

FPS = 60  # Sets frames per second for the game
CLOCK = pygame.time.Clock()  # Creates a Clock object to manage game timing

SCORE_FONT = pygame.font.SysFont("arial", 50)  # Sets font for current score text
LIVES_FONT = pygame.font.SysFont("consolas", 40)  # Sets font for lives text
TITLE_FONT = pygame.font.SysFont("times new roman", 80)  # Sets font for game title
NAME_FONT = pygame.font.SysFont("wide latin", 30)  # Sets font for creator name
MAX_SCORE_FONT = pygame.font.SysFont("jungle fever", 40) # Sets font for max score
DIRECTIONS_FONT = pygame.font.SysFont("comicsans", 20)  # Sets font for direction instructions
EXTRA_FONT = pygame.font.SysFont("georgian", 30)  # Sets font for any extra text

BACKGROUND = pygame.transform.scale(pygame.image.load("C:\\Users\\15715\\OneDrive\\Toy Collector\\Background\\toy_room.png").convert(), (WIDTH, HEIGHT))  # Loads and scales background image to screen size

HIT_SOUND = pygame.mixer.Sound("C:\\Users\\15715\\OneDrive\\Toy Collector\\Music\\happy_toy_hit.wav")  # Loads sound effect for toy hit
LOSS_SOUND = pygame.mixer.Sound("C:\\Users\\15715\\OneDrive\\Toy Collector\\Music\\loss_sound.wav")  # Loads sound effect for losing the game

def box_movement(keys, box, box_vel):  # Function to handle horizontal movement of the box based on keyboard input
    if keys[pygame.K_LEFT] and box.x - box_vel + 40 >= 0:  # If left arrow is pressed and box won't go off screen after moving
        box.x -= box_vel  # Move the box to the left by box_vel units

    if keys[pygame.K_RIGHT] and box.x + box_vel + box.width - 35 <= WIDTH:  # If right arrow is pressed and box stays within screen
        box.x += box_vel  # Move the box to the right by box_vel units


def draw(box_img, box, dino_img, dino_list, car_img, car_list, robot_img, robot_list, sphere_img, sphere_list, tape_img, tape_list, score, lives):  # Draw all game elements to the screen
    SCREEN.blit(BACKGROUND, (0, 0))  # Draw background image at top-left corner of screen
    
    SCREEN.blit(box_img, box)  # Draw the player’s box on screen

    for d in dino_list:  # Loop through all dinosaurs
        SCREEN.blit(dino_img, d)  # Draw each dinosaur

    for c in car_list:  # Loop through all cars
        SCREEN.blit(car_img, c)  # Draw each car

    for r in robot_list:  # Loop through all robots
        SCREEN.blit(robot_img, r)  # Draw each robot

    for s in sphere_list:  # Loop through all spheres
        SCREEN.blit(sphere_img, s)  # Draw each sphere

    for t in tape_list:  # Loop through all tape objects (health)
        SCREEN.blit(tape_img, t)  # Draw each tape

    score_text = SCORE_FONT.render(f"Score: {score}", True, (134, 234, 199))  # Render the score text with custom color
    SCREEN.blit(score_text, (20, 10))  # Display score in top-left corner

    lives_text = LIVES_FONT.render(f"Lives: {lives}", True, (123, 199, 114))  # Render the lives text with greenish color
    SCREEN.blit(lives_text, (WIDTH - lives_text.get_width() - 30, 10))  # Display lives in top-right corner
    
    pygame.display.update()  # Refresh the screen with new drawings

    

def main():  # Main function to run the game logic
    run = True  # Control variable for game loop

    score = 0  # Start with zero score
    lives = 10  # Player begins with 10 lives
    max_score = score  # Track the highest score

    game_active = False  # Game starts in an inactive state (e.g. on title screen)
    
    box_width, box_height = 170, 170  # Dimensions for the player box
    box_img = pygame.transform.scale(pygame.image.load("C:\\Users\\15715\\OneDrive\\Toy Collector\\Box\\box.png").convert_alpha(), (box_width, box_height))  # Load and scale the box image
    box = box_img.get_rect(midbottom = (WIDTH//2 - box_width//2, HEIGHT - 130))  # Create a rectangle for the box and position it near bottom center

    box_vel = 15  # Speed at which the box moves

    dino_width, dino_height = 50, 50  # Dimensions for dinosaurs
    dino_img = pygame.transform.scale(pygame.image.load("C:\\Users\\15715\\OneDrive\\Toy Collector\\Toys\\dino.png").convert_alpha(), (dino_width, dino_height))  # Load and scale the dino image
    dino = dino_img.get_rect(midbottom = (randint(dino_width, WIDTH - dino_width), -dino_height))  # Random spawn position above the screen
    dino_time = 0  # Timer for when to spawn next dino
    dino_count_increment = randint(4000, 6000)  # Random interval for spawning dinos
    dino_list = []  # List to store all current dino objects
    dino_vel = 5  # Speed at which dinos fall


    car_width, car_height = 45, 45  # Dimensions for cars
    car_img = pygame.transform.scale(pygame.image.load("C:\\Users\\15715\\OneDrive\\Toy Collector\\Toys\\car.png").convert_alpha(), (car_width, car_height))  # Load and scale the car image
    car = car_img.get_rect(midbottom = (randint(car_width, WIDTH - car_width), -car_height))  # Random spawn position above the screen
    car_time = 0  # Timer for car spawning
    car_count_increment = randint(3000, 8000)  # Random interval for car spawning
    car_list = []  # List to hold car objects
    car_vel = 5  # Speed of falling cars


    robot_width, robot_height = 40, 40  # Dimensions for robots
    robot_img = pygame.transform.scale(pygame.image.load("C:\\Users\\15715\\OneDrive\\Toy Collector\\Toys\\robot.png").convert_alpha(), (robot_width, robot_height))  # Load and scale robot image
    robot = robot_img.get_rect(midbottom = (randint(robot_width, WIDTH - robot_width), -robot_height))  # Random spawn position above the screen
    robot_time = 0  # Timer for robot spawning
    robot_count_increment = randint(4000, 10000)  # Random interval for robot spawning
    robot_list = []  # List to store robots
    robot_vel = 6  # Speed of falling robots
    
    
    
    sphere_width, sphere_height = 35, 35  # Dimensions for spheres
    sphere_img = pygame.transform.scale(pygame.image.load("C:\\Users\\15715\\OneDrive\\Toy Collector\\Toys\\sphere.png").convert_alpha(), (sphere_width, sphere_height))  # Load and scale sphere image
    sphere = sphere_img.get_rect(midbottom = (randint(sphere_width, WIDTH - sphere_width), -sphere_height))  # Random spawn position
    sphere_time = 0  # Timer for sphere spawning
    sphere_count_increment = randint(5000, 7000)  # Random interval for spawning spheres
    sphere_list = []  # List for all spheres
    sphere_vel = 6  # Falling speed for spheres



    # Health
    tape_width, tape_height = 30, 30  # Dimensions for tape (health item)
    tape_img = pygame.transform.scale(  # Load and scale tape image
    pygame.image.load("C:\\Users\\15715\\OneDrive\\Toy Collector\\Toys\\tape.png").convert_alpha(), (tape_width, tape_height))  # Continue loading and scaling
    tape = tape_img.get_rect(midbottom = (randint(tape_width, WIDTH - tape_width), -tape_height))  # Spawn tape randomly above screen
    tape_time = 0  # Timer for spawning tape
    tape_count_increment = 15000  # Fixed interval to spawn tape
    tape_list = []  # List to store tape objects
    tape_vel = 7  # Falling speed for tape


    while run:  # Main game loop that keeps running until 'run' is set to False
        dt = CLOCK.tick(FPS)  # Controls the game's framerate and gets the time since the last tick
        dino_time += dt  # Increases the dinosaur spawn timer
        car_time += dt  # Increases the car spawn timer
        robot_time += dt  # Increases the robot spawn timer
        sphere_time += dt  # Increases the sphere spawn timer
        tape_time += dt  # Increases the tape spawn timer

        for event in pygame.event.get():  # Processes all incoming events (e.g., key presses, window close)
            if event.type == pygame.QUIT:  # Checks if the user clicked the window close button
                run = False  # Stops the game loop
                break  # Exits the event loop early if quitting

        if game_active:  # Only run game logic if the game is currently active
            box_hitbox = pygame.Rect(box.x + 50, box.y + 45, 60, 30)  # Defines the hitbox of the player's box for collision detection
            keys = pygame.key.get_pressed()  # Gets the current state of all keyboard keys
            
            # Dino spawn logic
            if dino_time > dino_count_increment:  # Checks if enough time has passed to spawn a dino
                for _ in range(1):  # Spawns one dino
                    dino = dino_img.get_rect(midbottom = (randint(dino_width, WIDTH - dino_width), -dino_width))  # Creates a new dino rect at a random X position off-screen
                    dino_list.append(dino)  # Adds the new dino to the list of dinos
                dino_time = 0  # Resets the dino timer
                dino_count_increment = randint(4000, 6000)  # Sets the next random time interval for spawning

            for d in dino_list[:]:  # Loops through a copy of the dino list to safely modify the original
                d.y += dino_vel  # Moves the dino down the screen
                if d.colliderect(box_hitbox):  # Checks for collision with the player hitbox
                    HIT_SOUND.play()  # Plays the hit sound
                    score += 1  # Increases score by 1
                    dino_list.remove(d)  # Removes the dino that was hit
                elif d.y > HEIGHT:  # If the dino falls off screen
                    dino_list.remove(d)  # Remove the missed dino
                    lives -= 1  # Player loses a life for missing the dino

            # Car spawn logic
            if car_time > car_count_increment:  # Time check for spawning cars
                for _ in range(1):  # Spawns one car
                    car = car_img.get_rect(midbottom=(randint(car_width, WIDTH - car_width), -car_width))  # Randomly positions car off-screen
                    car_list.append(car)  # Adds new car to list
                car_time = 0  # Resets the car timer
                car_count_increment = randint(3000, 8000)  # Random next spawn interval

            for c in car_list[:]:  # Iterates over cars
                c.y += car_vel  # Moves car down
                if c.colliderect(box_hitbox):  # Collision with box
                    HIT_SOUND.play()  # Play sound
                    score += 2  # Adds 2 to score
                    car_list.remove(c)  # Remove collected car
                elif c.y > HEIGHT:  # If car is missed
                    car_list.remove(c)  # Remove off-screen car
                    lives -= 1  # Lose a life

            # Robot spawn logic
            if robot_time > robot_count_increment:  # Checks if robot should spawn
                for _ in range(1):  # Spawn one robot
                    robot = robot_img.get_rect(midbottom=(randint(robot_width, WIDTH - robot_width), -robot_width))  # New robot position
                    robot_list.append(robot)  # Add robot
                robot_time = 0  # Reset timer
                robot_count_increment = randint(4000, 10000)  # Set next interval

            for r in robot_list[:]:  # Loop through robots
                r.y += robot_vel  # Move down
                if r.colliderect(box_hitbox):  # Check collision
                    HIT_SOUND.play()  # Play sound
                    score += 3  # Score += 3
                    robot_list.remove(r)  # Remove robot
                elif r.y > HEIGHT:  # Missed robot
                    robot_list.remove(r)  # Remove
                    lives -= 1  # Lose life

            # Sphere spawn logic
            if sphere_time > sphere_count_increment:  # Spawn check
                for _ in range(1):  # One sphere
                    sphere = sphere_img.get_rect(midbottom=(randint(sphere_width, WIDTH - sphere_width), -sphere_width))  # Random position
                    sphere_list.append(sphere)  # Add to list
                sphere_time = 0  # Reset
                sphere_count_increment = randint(4000, 7000)  # Random delay

            for s in sphere_list[:]:  # Loop through spheres
                s.y += sphere_vel  # Move down
                if s.colliderect(box_hitbox):  # If hit
                    HIT_SOUND.play()  # Sound
                    score += 4  # +4 points
                    sphere_list.remove(s)  # Remove
                elif s.y > HEIGHT:  # Missed
                    sphere_list.remove(s)  # Remove
                    lives -= 1  # Lose life

            # Tape spawn logic
            if tape_time > tape_count_increment:  # Time to spawn tape
                for _ in range(1):  # One tape
                    tape = tape_img.get_rect(midbottom=(randint(tape_width, WIDTH - tape_width), -tape_width))  # New tape
                    tape_list.append(tape)  # Add
                tape_time = 0  # Reset timer
                tape_count_increment = 15000  # Fixed interval

            for t in tape_list[:]:  # Loop tapes
                t.y += tape_vel  # Move
                if t.colliderect(box_hitbox):  # Collision
                    HIT_SOUND.play()  # Sound
                    if lives < 10:  # Only heal if lives < 10
                        lives += 1  # Gain life
                    tape_list.remove(t)  # Remove tape
                elif t.y > HEIGHT:  # Missed tape
                    tape_list.remove(t)  # Remove

            if lives == 0:  # Game over check
                LOSS_SOUND.play()  # Sound
                pygame.time.delay(3000)  # Delay 3 seconds
                game_active = False  # End game

            box_movement(keys, box, box_vel)  # Update box position
            draw(box_img, box, dino_img, dino_list, car_img, car_list, robot_img, robot_list, sphere_img, sphere_list, tape_img, tape_list, score, lives)  # Draw everything

        else:  # Game is not active
            keys = pygame.key.get_pressed()  # Get key states
            if keys[pygame.K_SPACE]:  # Restart if space is pressed
                game_active = True  # Resume game
                score = 0  # Reset score
                lives = 10  # Reset lives
                box.x, box.y = WIDTH // 2 - box_width // 2, HEIGHT - 130  # Reset box position
                dino_time = 0 # Reset dino timer
                car_time = 0 # Reset car timer
                robot_time = 0 # Reset robot timer
                sphere_time = 0 # Reset sphere timer
                tape_time = 0  # Reset tape timer

            if score == 0:  # Show menu screen
                SCREEN.fill((155, 133, 89))  # Background color
                
                name_text = NAME_FONT.render("Created by Hamza Khatib", True, (100, 100, 255))  # Credits
                SCREEN.blit(name_text, (WIDTH // 2 - name_text.get_width() // 2, name_text.get_height() // 2))  # Center credits

                directions_text = DIRECTIONS_FONT.render("Use left and right arrow keys to move. Goal is to keep getting the highest score.", True, (10, 222, 22))  # Instructions
                SCREEN.blit(directions_text, (WIDTH // 2 - directions_text.get_width() // 2, directions_text.get_height() // 2 + 100))  # Center instructions

                title_text = TITLE_FONT.render("Toy Collector", True, (188, 233, 121))  # Title
                SCREEN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - title_text.get_height() // 2))  # Center title

                extra_text = EXTRA_FONT.render("Points: Dinosaur -> 1; Car -> 2; Robot -> 3; Sphere -> 4//Health: Tape -> + 1", True, (200, 200, 200))  # Scoring info
                SCREEN.blit(extra_text, (WIDTH // 2 - extra_text.get_width() // 2, HEIGHT - extra_text.get_height() - 100))  # Position at bottom
            
            else:  # Show score screen if game over
                SCREEN.fill((133, 89, 155))  # Different background
                max_score = max(score, max_score)  # Update max score

                score_text = SCORE_FONT.render(f"Current Score: {score}", True, (53, 110, 160))  # Current score message
                SCREEN.blit(score_text, (WIDTH//2 - score_text.get_width()//2,  score_text.get_height()))  # Display current score

                dino_list.clear() # Clear all dino entities
                car_list.clear()  # Clear all car entities
                robot_list.clear() # Clear all robot entities
                sphere_list.clear()  # Clear all sphere entities
                tape_list.clear()  # Clear all tape entities
                max_score_text = MAX_SCORE_FONT.render(f"Max Score: {max_score}", True, (134, 234, 199))  # Display max score
                SCREEN.blit(max_score_text, (WIDTH // 2 - max_score_text.get_width() // 2, HEIGHT // 2 - max_score_text.get_height() // 2))  # Center max score

        pygame.display.update()  # Update the display with all drawn content

    pygame.quit()  # Properly shuts down pygame when loop ends

if __name__ == "__main__":  # Standard Python check to run main game
    main()  # Calls the main function to start the game
