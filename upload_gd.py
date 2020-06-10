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

# GoogleDriveFile({
#     'title': 'data_cp.db', 
#     'parents': [{
#         'kind': 'drive#parentReference', 
#         'id': '1eQ-RN1QJfPNcP-J3ck7yxWLTNicLRK4x', 
#         'selfLink': 'https://www.googleapis.com/drive/v2/files/10BF2zw-jGqDaEsRqwZvz_xHEByhgbvhd/parents/1eQ-RN1QJfPNcP-J3ck7yxWLTNicLRK4x', 
#         'parentLink': 'https://www.googleapis.com/drive/v2/files/1eQ-RN1QJfPNcP-J3ck7yxWLTNicLRK4x', 
#         'isRoot': False}], 
#     'mimeType': 'application/octet-stream', 
#     'kind': 'drive#file', 
#     'id': '10BF2zw-jGqDaEsRqwZvz_xHEByhgbvhd', 
#     'etag': '"MTU5MTcwNTQ5NjQxOA"', 
#     'selfLink': 'https://www.googleapis.com/drive/v2/files/10BF2zw-jGqDaEsRqwZvz_xHEByhgbvhd', 
#     'webContentLink': 'https://drive.google.com/uc?id=10BF2zw-jGqDaEsRqwZvz_xHEByhgbvhd&export=download', 
#     'alternateLink': 'https://drive.google.com/file/d/10BF2zw-jGqDaEsRqwZvz_xHEByhgbvhd/view?usp=drivesdk', 
#     'embedLink': 'https://drive.google.com/file/d/10BF2zw-jGqDaEsRqwZvz_xHEByhgbvhd/preview?usp=drivesdk', 
#     'iconLink': 'https://drive-thirdparty.googleusercontent.com/16/type/application/octet-stream', 
#     'labels': {'starred': False, 'hidden': False, 'trashed': False, 'restricted': False, 'viewed': True}, 
#     'copyRequiresWriterPermission': False, 
#     'createdDate': '2020-06-09T12:24:56.418Z', 
#     'modifiedDate': '2020-06-09T12:24:56.418Z', 
#     'modifiedByMeDate': '2020-06-09T12:24:56.418Z', 
#     'lastViewedByMeDate': '2020-06-09T12:24:56.418Z', 
#     'markedViewedByMeDate': '1970-01-01T00:00:00.000Z', 
#     'version': '1', 
#     'downloadUrl': 'https://www.googleapis.com/drive/v2/files/10BF2zw-jGqDaEsRqwZvz_xHEByhgbvhd?alt=media&source=downloadUrl', 
#     'userPermission': {
#         'kind': 'drive#permission', 
#     'fileExtension': 'db', 
#     'md5Checksum': '6dd1dadb562d25aeae1d3793154d1aa4', 
#     'fileSize': '81920', 
#     'quotaBytesUsed': '81920', 
#     'ownerNames': ['NRG'], 
#     'owners': [{
#         'kind': 'drive#user', 
#         'displayName': 'NRG', 
#         'picture': {'url': 'https://lh3.googleusercontent.com/a-/AOh14GhvSEWOTUkG8bDghKIm1OT3GHyPnbQnXrBY4RxG=s64'}, 
#         'isAuthenticatedUser': True, 
#         'permissionId': '07727582442218366665', 
#         'emailAddress': 'nikitaazov4@gmail.com'}], 
#         'lastModifyingUserName': 'NRG', 
#         'lastModifyingUser': {'kind': 'drive#user', 
#         'displayName': 'NRG', 
#         'picture': {'url': 'https://lh3.googleusercontent.com/a-/AOh14GhvSEWOTUkG8bDghKIm1OT3GHyPnbQnXrBY4RxG=s64'}, 
#         'isAuthenticatedUser': True, 'permissionId': '07727582442218366665', 'emailAddress': 'nikitaazov4@gmail.com'}, 
#         'capabilities': {
#             'canCopy': True, 
#             'canEdit': True}, 
#             'editable': True, 
#             'copyable': True, 
#             'writersCanShare': True, 
#             'shared': False, 
#             'explicitlyTrashed': False, 
#             'appDataContents': False, 
#             'headRevisionId': '0BxYM5ntjJSuQSHJ3U2Zib2dsc0d0RVNjOXF2Z2Y3MWRuVnFRPQ', 
#             'spaces': ['drive']})apis.com/drive/v2/files/10BF2zw-jGqDaEsRqwZvz_xHEByhgbvhd/permissions/me', 
#         'role': 'owner', 
#         'type': 'user'}, 
#     'originalFilename': 'data_cp.db', 
#     'fileExtension': 'db', 
#     'md5Checksum': '6dd1dadb562d25aeae1d3793154d1aa4', 
#     'fileSize': '81920', 
#     'quotaBytesUsed': '81920', 
#     'ownerNames': ['NRG'], 
#     'owners': [{
#         'kind': 'drive#user', 
#         'displayName': 'NRG', 
#         'picture': {'url': 'https://lh3.googleusercontent.com/a-/AOh14GhvSEWOTUkG8bDghKIm1OT3GHyPnbQnXrBY4RxG=s64'}, 
#         'isAuthenticatedUser': True, 
#         'permissionId': '07727582442218366665', 
#         'emailAddress': 'nikitaazov4@gmail.com'}], 
#         'lastModifyingUserName': 'NRG', 
#         'lastModifyingUser': {'kind': 'drive#user', 
#         'displayName': 'NRG', 
#         'picture': {'url': 'https://lh3.googleusercontent.com/a-/AOh14GhvSEWOTUkG8bDghKIm1OT3GHyPnbQnXrBY4RxG=s64'}, 
#         'isAuthenticatedUser': True, 'permissionId': '07727582442218366665', 'emailAddress': 'nikitaazov4@gmail.com'}, 
#         'capabilities': {
#             'canCopy': True, 
#             'canEdit': True}, 
#             'editable': True, 
#             'copyable': True, 
#             'writersCanShare': True, 
#             'shared': False, 
#             'explicitlyTrashed': False, 
#             'appDataContents': False, 
#             'headRevisionId': '0BxYM5ntjJSuQSHJ3U2Zib2dsc0d0RVNjOXF2Z2Y3MWRuVnFRPQ', 
#             'spaces': ['drive']})