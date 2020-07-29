from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

upload_finish = None

class upload_file(object):
    def upload_f(self):
      try:
        gauth = GoogleAuth()
        # gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

        # Try to load saved client credentials
        gauth.LoadCredentialsFile("mycreds.txt")
        if gauth.credentials is None:
            # Authenticate if they're not there
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            # Refresh them if expired
            gauth.Refresh()
        else:
            # Initialize the saved creds
            gauth.Authorize()
        # Save the current credentials to a file
        gauth.SaveCredentialsFile("mycreds.txt")

        # Create GoogleDrive instance with authenticated GoogleAuth instance.
        drive = GoogleDrive(gauth)

        file1 = drive.CreateFile({'title': 'data_cp.db', "parents": [{"kind": "drive#fileLink","id": '1eQ-RN1QJfPNcP-J3ck7yxWLTNicLRK4x'}]})
        # Read file and set it as a content of this instance.
        file1.SetContentFile('data/data_cp.db')
        file1.Upload() # Upload the file.
        # print('title: %s, mimeType: %s, id: %s' % (file1['title'], file1['mimeType'], file1['id']))
        # print (file1)
          
        upload_finish = bool(1)
        return upload_finish

      except:
        upload_finish = bool(0)
        return upload_finish