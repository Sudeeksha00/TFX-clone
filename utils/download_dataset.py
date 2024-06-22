import logging
import os
import shutil
import urllib3
from configurations.config import Config


def download_dataset(LOCAL_FILE_NAME, url):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # disabing warnings associated with potential security risks due to insecure connections. (not recommended for production use) 
    c = urllib3.PoolManager()
    # creating a connection pool to manage HTTP requests efficently.
    with c.request("GET", url, preload_content=False) as res, open(
        LOCAL_FILE_NAME, "wb"
    ) as out_file:
        shutil.copyfileobj(res, out_file)
    logging.info("Download completed.")
# GET request to specified URL and opens the file to write in binary mode. (wb)
# preload_content = FALSE: don't load entire content into memory at once. This will be useful for large datasets.
# shutil.... : copies the data into a local output file

# This function determines the root folder of the project.
# ARDHAMKAALE final ga em "path" return chestundhi ani...?
def get_folder():
    path = os.getcwd()
    while True:
        path, ref = os.path.split(path)
        if ref == Config.PROJECT_NAME:
            path = os.path.join(path, ref)
            break
        if path == '':
            raise Exception('Check Wheather project name set correctly')
    return path

# It checks whether current code is run as main script or if its being imported as a module from another script.
# This makes sure that this code is executed only when it is run as main script.
if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)
    logging.info("Started download script")

    path = get_folder()
    LOCAL_FILE_NAME = os.path.join(path, "data", 'dataset1', "consumer_complaints_with_narrative.csv")
    download_dataset(LOCAL_FILE_NAME, Config.DATASET_URL)

    logging.info("Finished download script")
