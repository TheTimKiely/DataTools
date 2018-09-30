import pandas as pd
import urllib
import tempfile
import shutil
import zipfile


class HttpProvider(object):

    def download_data(self, url):
        temp_dir = tempfile.mkdtemp()
        zipname = temp_dir + '/Bike-Sharing-Dataset.zip'
        urllib.request.urlretrieve(url, zipname)

        zip_ref = zipfile.ZipFile(zipname, 'r')
        zip_ref.extractall(temp_dir)
        zip_ref.close()

        daily_path = temp_dir + '/day.csv'
        daily_data = pd.read_csv(daily_path)
        daily_data['dteday'] = pd.to_datetime(daily_data['dteday'])
        drop_list = ['instant', 'season', 'yr', 'mnth', 'holiday', 'workingday', 'weathersit', 'atemp', 'hum']
        daily_data.drop(drop_list, inplace = True, axis = 1)

        shutil.rmtree(temp_dir)

        return daily_data