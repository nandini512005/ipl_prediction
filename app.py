from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import os
import random
import threading
import time
from datetime import datetime

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Complete IPL player database WITH STATS (fixes template crashes)
IPL_DATABASE = [
    {
        "name": "Hardik Pandya", 
        "team": "MI", 
        "vs": "CSK", 
        "img": "hardik.jpg",
        "stats": {
            "total_runs": 2525, "matches": 137, "wickets": 64,
            "avg": 33.59, "strike_rate": 145.6, "fifties": 10, "sixes": 136
        }
    },
    {
        "name": "Virat Kohli", 
        "team": "RCB", 
        "vs": "KKR", 
        "img": "kohli.jpg",
        "stats": {
            "total_runs": 8019, "matches": 267, "wickets": 0,
            "avg": 38.11, "strike_rate": 131.97, "fifties": 66, "sixes": 358
        }
    },
    {
        "name": "MS Dhoni", 
        "team": "CSK", 
        "vs": "MI", 
        "img": "dhoni.jpg",
        "stats": {
            "total_runs": 5119, "matches": 253, "wickets": 0,
            "avg": 39.08, "strike_rate": 136.32, "fifties": 24, "sixes": 242
        }
    },
    {
        "name": "Rishabh Pant", 
        "team": "DC", 
        "vs": "PBKS", 
        "img": "pant.jpg",
        "stats": {
            "total_runs": 1688, "matches": 111, "wickets": 0,
            "avg": 20.10, "strike_rate": 148.46, "fifties": 8, "sixes": 87
        }
    },
    {
        "name": "Shubman Gill", 
        "team": "GT", 
        "vs": "RR", 
        "img": "gill.jpg",
        "stats": {
            "total_runs": 3132, "matches": 100, "wickets": 0,
            "avg": 34.80, "strike_rate": 156.21, "fifties": 21, "sixes": 112
        }
    },
    {
        "name": "Sanju Samson", 
        "team": "RR", 
        "vs": "LSG", 
        "img": "samson.jpg",
        "stats": {
            "total_runs": 2942, "matches": 145, "wickets": 0,
            "avg": 23.06, "strike_rate": 148.95, "fifties": 17, "sixes": 143
        }
    },
    {
        "name": "KL Rahul", 
        "team": "LSG", 
        "vs": "RCB", 
        "img": "rahul.jpg",
        "stats": {
            "total_runs": 4680, "matches": 153, "wickets": 3,
            "avg": 32.55, "strike_rate": 133.70, "fifties": 36, "sixes": 166
        }
    },
    {
        "name": "Shreyas Iyer", 
        "team": "KKR", 
        "vs": "SRH", 
        "img": "iyer.jpg",
        "stats": {
            "total_runs": 2878, "matches": 101, "wickets": 0,
            "avg": 31.28, "strike_rate": 134.13, "fifties": 18, "sixes": 95
        }
    },
    {
        "name": "Pat Cummins", 
        "team": "SRH", 
        "vs": "GT", 
        "img": "cummins.jpg",
        "stats": {
            "total_runs": 414, "matches": 52, "wickets": 56,
            "avg": 21.78, "strike_rate": 141.37, "fifties": 0, "sixes": 22
        }
    },
    {
        "name": "Sam Curran", 
        "team": "PBKS", 
        "vs": "DC", 
        "img": "curran.jpg",
        "stats": {
            "total_runs": 738, "matches": 47, "wickets": 44,
            "avg": 19.94, "strike_rate": 139.92, "fifties": 2, "sixes": 32
        }
    }
]

def generate_live_stats():
    """Simulates live Kafka/PyFlink processing"""
    while True:
        player_update = random.choice(IPL_DATABASE)
        new_rating = random.ran
