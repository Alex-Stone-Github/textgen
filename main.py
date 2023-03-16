import torch
import os
import typing

# utils
def read_file(filepath: str) -> str:
    text = None
    with open(filepath, 'r') as f:
        text = f.read()
    return text
def char_to_scaler(letter: chr) -> float:
    return float(ord(letter) % 128) / 128.0
def scaler_to_char(scaler: float) -> chr:
    return chr(int(scaler*128))
def to_x_y_data(vector: typing.List[float], lookback: int) -> (torch.Tensor, torch.Tensor):
    y = []
    x = []
    for i, scalervalue in enumerate(vector[lookback:]):
        y.append(scalervalue)
        x.append(vector[i:i+lookback])
    return torch.Tensor(x), torch.Tensor(y)


lookback = 130
learning_rate = 0.005
epochs = 600
batch_size = 60

# train data
text = ""
for filename in os.listdir("data"):
    filepath = os.path.join("data", filename)
    text += read_file(filepath)
x,y = None, None
if True:
    vectorized = list(map(char_to_scaler, text))
    x,y = to_x_y_data(vectorized, lookback)
y = torch.reshape(y, (-1, 1))

# model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Linear(lookback, 100)
        self.layer2 = torch.nn.Linear(100, 100)
        self.layer3 = torch.nn.Linear(100, 60)
        self.layer4 = torch.nn.Linear(60, 1)
    def forward(self, x):
        output = self.layer1(x)
        output = torch.nn.functional.leaky_relu(output)
        output = self.layer2(output)
        output = torch.nn.functional.leaky_relu(output)
        output = self.layer3(output)
        output = torch.nn.functional.leaky_relu(output)
        output = self.layer4(output)
        return output

textgen = Model()
loss_function = torch.nn.MSELoss()
optimizer = torch.optim.SGD(textgen.parameters(), lr=learning_rate)


# training
print("starting")
for epoch in range(epochs):
    total_loss = 0
    for bx, by in zip(x.split(batch_size), y.split(batch_size)):
        outputs = textgen(bx)
        loss = loss_function(outputs, by)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.tolist()
    print(epoch, "/", epochs, "loss: ", total_loss)
# save
torch.save(textgen.state_dict(), "model")
    
print("--------------------------")
print("Generating")
print("--------------------------")


# generating
total = ""
current = """
I have also approved recommendations of the Secretary of Commerce [Luther H. Hodges] regarding standards for recording the Standard Code for Information Interchange on magnetic tapes and paper tapes when they are used in computer operations. All computers and related equipment configurations brought into the Federal Government inventory on and after July 1, 1969, must have the capability to use the Standard Code for Information Interchange and the formats prescribed by the magnetic tape and paper tape standards when these media are used.
"""[:lookback]
print(current)
for _ in range(30):
    inp = torch.Tensor(list(map(char_to_scaler, current)))
    inp = torch.reshape(inp, (1,lookback))
    output = textgen(inp).tolist()[0][0]
    new_letter = scaler_to_char(output)
    current += new_letter
    total += new_letter
    current = current[1:]
    print(total)
    

