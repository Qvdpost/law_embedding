class MLP(nn.module):
    def __init__(self):
        self.fc1 = torch.nn.Linear(25,10)
        self.fc2 = torch.nn.Linear(10,2)

    def forward(x):
        x = nn.ReLU(self.fc1(x))
        return nn.softmax(self.fc2(x))
