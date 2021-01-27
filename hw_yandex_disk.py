import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.headers = {'Authorization': self.token}

    def upload(self, file_path: str):
        print(file_path)
        file_name = file_path.split("\\")[-1]
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                params={'path': file_name, 'overwrite': 'true'},
                                headers=self.headers
                                )
        response.raise_for_status()

        upload_link = response.json()['href']

        with open(file_path, 'rb') as f:
            response = requests.put(upload_link, headers=self.headers, files={'file': f})
            response.raise_for_status()
        status = response.status_code
        return status


if __name__ == '__main__':
    uploader = YaUploader('ТОКЕН ПРЕПОДАВАТЕЛЯ')
    result = uploader.upload(r'C:\какой-нибудь путь\image.jpg')
    print(f'Статус ответа о загрузке файла: {result}')
