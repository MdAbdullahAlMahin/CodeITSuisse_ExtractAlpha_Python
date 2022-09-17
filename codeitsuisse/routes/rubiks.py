import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/rubiks', methods=['POST'])
def rubiks():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")
    ops = data["ops"]
    state = data["state"]
    ops = ops.split()
    for i in range(0,len(ops)):
        if ops[i] == "U":
            if i < len(ops) - 1 and ops[i+1]=="i":
                Ui(state)
            else:
                U(state)
        elif ops[i] == "F":
            if i < len(ops) - 1 and ops[i+1]=="i":
                Fi(state)
            else:
                F(state)
        elif ops[i] == "D":
            if i < len(ops) - 1 and ops[i+1]=="i":
                Di(state)
            else:
                D(state)
        elif ops[i] == "B":
            if i < len(ops) - 1 and ops[i+1]=="i":
                Bi(state)
            else:
                B(state)
        elif ops[i] == "L":
            if i < len(ops) - 1 and ops[i+1]=="i":
                Li(state)
            else:
                L(state)
        elif ops[i] == "R":
            if i < len(ops) - 1 and ops[i+1]=="i":
                Ri(state)
            else:
                R(state)
    return json.dumps(state)

def R(state):
    for i in range(0,3):
        state[f][i][2],state[u][i][2],state[b][i][2],state[d][i][2] = state[b][i][2],state[f][i][2],state[u][i][2],state[b][i][2]
    Rotate_Clockwise(state[r])

def Ri(state):
    for i in range(0,3):
        state[f][i][2],state[u][i][2],state[b][i][2],state[d][i][2] = state[u][i][2],state[b][i][2],state[d][i][2],state[f][i][2]
    Rotate_Anti_Clockwise(state[r])

def Li(state):
    for i in range(0,3):
        state[f][i][0],state[u][i][0],state[b][i][0],state[d][i][0] = state[b][i][0],state[f][i][0],state[u][i][0],state[b][i][0]
    Rotate_Clockwise(state[l])

def L(state):
    for i in range(0,3):
        state[f][i][0],state[u][i][0],state[b][i][0],state[d][i][0] = state[u][i][0],state[b][i][0],state[d][i][0],state[f][i][0]
    Rotate_Clockwise(state[l])

def U(state):
    state[f][0],state[l][0],state[b][0],state[r][0] = state[r][0], state[f][0], state[l][0], state[b][0]
    Rotate_Clockwise(state[u])

def Ui(state):
    state[f][0],state[l][0],state[b][0],state[r][0] = state[l][0], state[b][0], state[r][0], state[f][0]
    Rotate_Anti_Clockwise(state[u])

def Di(state):
    state[f][2],state[l][2],state[b][2],state[r][2] = state[r][2], state[f][2], state[l][2], state[b][2]
    Rotate_Anti_Clockwise(state[d])

def D(state):
    state[f][2],state[l][2],state[b][2],state[r][2] = state[l][0], state[b][0], state[r][0], state[f][0]
    Rotate_Clockwise(state[d])

def F(state):
    for i in range(0,3):
        state[u][2][i],state[r][i][0],state[b][0][i],state[l][i][2] = state[l][i][2],state[u][2][i],state[r][i][0],state[b][0][i]
    Rotate_Clockwise(state[f])

def Fi(state):
    for i in range(0,3):
        state[u][2][i],state[r][i][0],state[b][0][i],state[l][i][2] = state[r][i][0],state[b][0][i],state[l][i][2],state[u][2][i],
    Rotate_Anti_Clockwise(state[f])

def Bi(state):
    for i in range(0,3):
        state[u][0][i],state[r][i][2],state[b][2][i],state[l][i][0] = state[l][i][0],state[u][0][i],state[r][i][2],state[b][2][i]
    Rotate_Anti_Clockwise(state[b])

def B(state):
    for i in range(0,3):
        state[u][0][i],state[r][i][2],state[b][2][i],state[l][i][0] = state[r][i][2],state[b][2][i],state[l][i][0],state[u][0][i],
    Rotate_Clockwise(state[f])

def Rotate_Clockwise(m):
    m[0],m[1],m[2],m[3],m[5],m[6],m[7],m[8] = m[6],m[3],m[0],m[7],m[1],m[8],m[2],m[2]

def Rotate_Anti_Clockwise(m):
    m[0],m[1],m[2],m[3],m[5],m[6],m[7],m[8] = m[2],m[5],m[8],m[1],m[7],m[0],m[3],m[6]