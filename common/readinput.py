import requests
import base64
import zipfile
import io
import pandas as pd
import os

def load_data_alps():
    #1: Preparing the URL.
    base_url = "https://www.kaggle.com/api/v1"
    owner_slug = "jorgealdapd"
    dataset_slug = "belleii-alp-fit"
    dataset_version = "2"

    url = f"{base_url}/datasets/download/{owner_slug}/{dataset_slug}?datasetVersionNumber={dataset_version}"

    #2: Encoding the credentials and preparing the request header.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(current_dir, "../.secret/username"), "r") as f:
        username = f.read().strip()
    with open(os.path.join(current_dir, "../.secret/token"), "r") as f:
        key = f.read().strip()
    creds = base64.b64encode(bytes(f"{username}:{key}", "ISO-8859-1")).decode("ascii")
    headers = {
    "Authorization": f"Basic {creds}"
    }

    #3: Sending a GET request to the URL with the encoded credentials.
    response = requests.get(url, headers=headers)
    response = requests.get(url, headers=headers)

    #4: Loading the response as a file via io and opening it via zipfile.
    zf = zipfile.ZipFile(io.BytesIO(response.content))

    #5: Reading the CSV from the zip file and converting it to a dataframe.
    file_name = "belleII_alps.csv"
    df = pd.read_csv(zf.open(file_name))
    return df

def prepare_sample(df, n_samples=1000, seed=None):
    sample_df = df.sample(n=n_samples, random_state=seed, ignore_index=True)
    return sample_df
