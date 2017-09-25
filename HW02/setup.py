import os

def create_dir_if_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def download_data():
    filenames = ["train.csv", "test.csv", "enhanced_train.csv"]
    download_url = "https://rhdzmota-cloud-storage.herokuapp.com/temporal-link/dropbox-files?file_name={}&file_path={}"
    for file in filenames:
        if os.path.isfile("data/" + file):
            continue
        r = requests.get(download_url.format(file, "/kaggle/nyc-taxi"))
        f = requests.get(r.json().get("url"))
        with open("data/"+file, "wb") as code:
            code.write(f.content)


if __name__ == '__main__':
    create_dir_if_exists('data')
    create_dir_if_exists('output')
    download_data()
