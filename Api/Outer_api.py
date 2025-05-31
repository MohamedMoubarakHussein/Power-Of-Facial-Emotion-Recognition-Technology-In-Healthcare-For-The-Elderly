import warnings
from PIL import Image
from flask import Flask, request, jsonify
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import requests
import io
import base64
import os
import json
import random
from flask import Flask, request, jsonify
import openai

import Story


def chatGpt(emotion):
    openai.api_key = open("chatgpt-api-key.txt", "r").read().strip("\n")
    prom = Story.chatGpt(emotion)
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prom,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5
    )
    recommendation  = response.choices[0].text.strip(' ').replace('\n\n', '').replace("\n"," ")
    return recommendation

def SpotifiyToken():
    client_id = os.getenv("Client-id")
    client_secret = os.getenv("Client-secret")
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url, headers=headers, data=data)
    json_result = response.json()
    if "access_token" not in json_result:
        raise Exception("Authentication failed. No access token received.")
    token = json_result["access_token"]
    return  {"Authorization":"Bearer " + token}

def spotify():
    url = f"https://api.spotify.com/v1/playlists/{Story.spotify()[0]}"
    response = requests.get(url, headers=SpotifiyToken())
    return  response.json()["external_urls"]["spotify"]


def image():
    stability_api = client.StabilityInference(
    key="sk-OlYe9gFlr6BnO8YzmfzDkOJxbn0Xllxte5UjkdyD0OGLXfa3",
    verbose=True)
    resp = next(stability_api.generate(prompt=Story.image(), steps=20))
    for artifact in resp.artifacts:
        if artifact.type == generation.ARTIFACT_IMAGE:
            image_filename = f"{random.randint(1, 1000)}.jpg"
            image_path = os.path.join("E:/xampp/htdocs/client_final/public/assets/img/imageai", image_filename)
            with open(image_path, "wb") as f:
                f.write(artifact.binary)
            return image_filename
