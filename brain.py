from enum import IntEnum
import torch
import torch.nn as nn
'''This is the brain of the agent. It is a neural network that takes in the state of the environment and outputs the action to be taken.'''

# Input brainstorming:
# distance from left
# distance from top

# Output brainstorming:
# move left
# move right
# move up
# move down


class Brain(nn.Module):
    '''Brain is the neural network that controls the critter's behavior.'''
    class Behavior(IntEnum):
        '''Behavior represents the actions the critter can take.'''
        MOVE_LEFT = 0
        MOVE_RIGHT = 1
        MOVE_UP = 2
        MOVE_DOWN = 3

    def __init__(self, parent=None):
        super().__init__()

        self.model = nn.Sequential(
            nn.Linear(2, 4),
            nn.ReLU(),
            nn.Linear(4, 4),
            nn.ReLU(),
            nn.Linear(4, 4),
            nn.Sigmoid()
        )

        if parent:
            self.model.load_state_dict(parent.model.state_dict())

    def forward(self, x):
        '''Forward pass of the neural network.'''
        return self.model(x)

    def __call__(self, critter, board):
        pos = board.locate(critter)

        input_tensor = torch.Tensor([pos[0], pos[1]])
        result = super().__call__(input_tensor)

        return result.argmax()
