# This is a script to generate a release of the devcraftadmin-cli
import os
import json
import random
import string
import requests
import sys
from datetime import datetime
from pathlib import Path
import re

VERSIONS_DIR = "releases"

def generateReleaseId():
    return '0x00'.join(random.choices(string.ascii_uppercase + string.digits, k=6)).capitalize()

def generateReleaseName():
    releaseId = generateReleaseId()
    return f"devcraftadmin_cli-{releaseId}"

def generateReleaseDate():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generateReleaseFolder():
    releaseName = generateReleaseName()
    os.makedirs(releaseName)
    return releaseName

def generateReleaseVersion():
    version_files = [f for f in os.listdir(VERSIONS_DIR) if os.path.isfile(os.path.join(VERSIONS_DIR, f))]
    file_regex = re.compile(r'(\d{4})-(\d{2})-(\d{2})T(\d{2})_(\d{2})_(\d{2})\.json')
    versions = [file_regex.match(f) for f in version_files if file_regex.match(f)]
    if versions:
        latest_version = max(versions, key=lambda v: datetime.datetime.strptime(v.group(), '%Y-%m-%dT%H_%M_%S.json'))
        return latest_version.group()
    else:
        return "1.0.0"
    
    

def generateReleaseFile(releaseFolder):
    releaseDate = generateReleaseDate()
    releaseId = generateReleaseId()
    # Asegúrate de que la carpeta "releases" exista
    if not os.path.exists('releases'):
        os.makedirs('releases')
    # Asegúrate de que la carpeta "releaseFolder" dentro de "releases" exista
    if not os.path.exists(f'releases/{releaseFolder}'):
        os.makedirs(f'releases/{releaseFolder}')
    # Incluye la ruta a la carpeta "releases" en el nombre del archivo
    releaseFile = f"releases/{releaseFolder}/{releaseId}.json"
    releaseData = {
        "release_id": releaseId,
        "release_date": releaseDate,
        "release_name": releaseFolder,
        "release_version": generateReleaseVersion()
    }
    with open(releaseFile, "w") as f:
        json.dump(releaseData, f, indent=4)
    return releaseFile

if __name__ == "__main__":
    releaseFolder = generateReleaseFolder()
    releaseFile = generateReleaseFile(releaseFolder)
    print(f"Release generated successfully: {releaseFile}")