import boto3
from datetime import datetime

BUCKET = 'atividades3' 
CONTAINER_MOVIE_PATH = '/s3/movies.csv'
CONTAINER_SERIES_PATH = '/s3/series.csv'

S3_PATH_MOVIE = f'Raw/Local/CSV/Movie/{datetime.now().strftime("%Y/%m/%d")}'
S3_PATH_SERIE = f'Raw/Local/CSV/Serie/{datetime.now().strftime("%Y/%m/%d")}'

boto3.DEFAULT_SESSION = boto3.Session(aws_access_key_id = "ASI",
    aws_secret_access_key = "/g/NkQNiVqB+V1Eo",
    aws_session_token = "IQoJbGgw3MjYxMTg4NTA2NTkiDDedO0avEwNfwoj6PSr8AoMCmOhjXlN2GccJIXDdjFUiYxXNB8FVsAPh5gS0hDFjl9Tte5KbyUZ5AJ+HtCT/R92HqhUrhtRiXGGu3bcZhtf4Ps8S322EfVQ2b//g9ZmaiT4ZV0FSqBiHH1KWEN7ymo+L62UkHNtT2SvrqkLG1fvzlE0rQ5CMX1OCuZcFh988v7jt0xXAcnierLuhhSO1R7g+tB2q1jJ2rw2Uiv6lP2/11RyhbBMvom6JAyYtt4vnsEHACSjJzRIJHIAgf1BX0yIKkibgWbhWJHlehBqqLOx2XEusSou+BH+Qx97btRm/XP6kSN979dcN6qK68J3RLjGOjRNFwDyT/h5spOP79QgfabuHZ5612C5xQW8F+Net4kY+HRhPfxBo+yhTpZCdTNpT4XuJse2J0ZsquyRoiYmnIEoLfa5FjWZ5fuf2j/b8UxMWsbAiuPa/I17v3WD2zxpHq6ThYDA0F8D4f1g3Nf5bYCi6Rcu1M8fXyK5Vh5PkljnXIvDEmnafcjYxMLuFqq0GOqYB8MWGHB+GsaYNtIT+6riIUV36c4vF2bRfuC8kSqyHrC5We4QuK9KbenFXSeeFVTM1EzxcdhRKRu4kjB7v7hQTysckpCn/KsYQL5+OSvviMK8goGUNlE2Wp/aI8Df1GTxkoEJ4rJnP7HumrPFwwooKv/bwKEVcRurxIIVx+0diH8x1ki/j+60M2WV7KxKGtKlSFw+1LGKRWZsj4Q45qqjVZsQLnwGX6Q==")
    

def upload_file_to_s3(path_local, bucket, path_s3):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(path_local, bucket, path_s3)
        print(f"arquivo {path_local} enviado para {path_s3}")
    except Exception as e:
        print(f"Erro ao enviar {path_local}: {str(e)}")


def main():
    upload_file_to_s3(CONTAINER_MOVIE_PATH, BUCKET, S3_PATH_MOVIE + "/movies.csv")
    upload_file_to_s3(CONTAINER_SERIES_PATH, BUCKET, S3_PATH_SERIE + "/series.csv")


if '__main__' == __name__:
    main()