#!/bin/bash

tmux new-session -d -s KeyWordio

# backend window
tmux rename-window -t KeyWordio:1 'backend'
tmux send-keys -t KeyWordio:1 'cd backend' C-m
tmux send-keys -t KeyWordio:1 'activate_env' C-m
tmux send-keys -t KeyWordio:1 'cd Library_Management' C-m
tmux send-keys -t KeyWordio:1 'nvim' C-m

# frontend window
tmux new-window -t KeyWordio
tmux rename-window -t KeyWordio:2 -n 'frontend'
tmux send-keys -t KeyWordio:2 'cd frontend/Library' C-m
tmux send-keys -t KeyWordio:2 'nvim' C-m

## Running script window
tmux new-window -t KeyWordio
tmux renamenew-window -t KeyWordio:3 'dev'

# split panes
tmux split-window -h -t KeyWordio:3 # split horizontally
tmux split-window -v -t KeyWordio:3.1 # split vertically

# Run commands in each pane
# pane 3.1
tmux send-keys -t KeyWordio:3.1 'cd backend' C-m
tmux send-keys -t KeyWordio:3.1 'activate_env' C-m
tmux send-keys -t KeyWordio:3.1 'cd Library_Management' C-m
tmux send-keys -t KeyWordio:3.1 'python manage.py runserver' C-m

# pane 3.2
tmux send-keys -t KeyWordio:3.2 'cd frontend/Library' C-m
tmux send-keys -t KeyWordio:3.2 'npm run dev' C-m

# Attach to the session
tmux attach -t KeyWordio
