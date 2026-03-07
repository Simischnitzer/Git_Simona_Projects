# Copyright (c) 2025 Simona Schnitzer.
# Licensed under the MIT License. See LICENSE file for details.
# I’m trying to create a Kanban Dashboard demo.

import turtle
import time

# Setup agents representing Kanban columns
backlog_item = turtle.Turtle("turtle")
in_progress_item = turtle.Turtle("turtle")
done_item = turtle.Turtle("turtle")

agents = [backlog_item, in_progress_item, done_item]
colors = ["blue", "red", "orange"]  # blue=backlog, red=in progress, orange=done

# Configure agents
for agent, color in zip(agents, colors):
    agent.color(color)
    agent.width(3)
    agent.speed(3)
    agent.penup()

# Positions for each Kanban column
positions = [(-250, 0), (0, 0), (250, 0)]

# Draw ležaté obdélníky (tickets) for each column
block_width = 120
block_height = 60

for agent, pos in zip(agents, positions):
    agent.goto(pos)
    agent.pendown()
    for _ in range(2):  # Draw horizontal rectangle
        agent.forward(block_width)
        agent.left(90)
        agent.forward(block_height)
        agent.left(90)
    agent.penup()
    time.sleep(0.5)  # pause to visualize drawing step by step

# Display dashboard title
done_item.goto(0, 150)
done_item.write("Dashboard Preview", font=("Arial", 20, "bold"), align="center")

# turtle.done()