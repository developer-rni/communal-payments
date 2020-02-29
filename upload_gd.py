import json
import requests

upload_finish = None

class upload_file(object):
    def upload_f(self):
        headers = {"Authorization": "Bearer ###your token###"} #put ur access token after the word 'Bearer '
        para = {
            "name": "data_cp.db", #file name to be uploaded
            "parents": ["###your folder ID###"] # make a folder on drive in which you want to upload files; then open that folder; the last thing in present url will be folder id
        }
        files = {
            'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
            'file': open("data/data_cp.db", "rb") # replace 'application/zip' by 'image/png' for png images; similarly 'image/jpeg' (also replace your file name)
        }
        r = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=headers,
            files=files
        )
        # print(r.text) #log upload
        r_str = str(r)


        if r_str == '<Response [200]>':
            upload_finish = bool(1)
        elif r_str == '<Response [401]>':
            upload_finish = bool(0)

        return upload_finish


