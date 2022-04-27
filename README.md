# CS-491-Final-Project
Author: Jared Nelson
# Snake Game
Snake Game is a single player game where the snake is controlled by a player.  Without running into the walls or eating its own tail the snake must eat the randomly generated "Snacks" around the game arena.  Each snack increases the snake's size and adds to the player score.
## Manual Running Instructions
Below is a list of running instructions to clone and run Snake Game locally.

Clone Repository:
```bash
git clone https://github.com/JNelson0/CS-491-Final-Project.git
```
Install needed python dependencies:
```bash
pip install -r requirements.txt
```
Run Snake Game:
```bash
python main.py
```
Manually run test scripts:
```bash
coverage run testing.py
```
Run test coverage:
```bash
coverage report
```
## Docker Instructions
In order to use docker image for Snake Game you must have available running xserver or you will get an error.
> "pygame.error: No available video device"

Pull Docker Image:
```bash
docker pull jnelson1/cs491finalproject:latest
```
Run Docker Image:
```bash
docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix \ -e DISPLAY=unix$DISPLAY jnelson1/cs491finalproject:latest
```
