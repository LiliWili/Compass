import urllib3
import json
import pandas as pd
from datetime import datetime
import boto3

def lambda_handler(event, context):
    api_key = 'minha_chave'
    base_url = 'https://api.themoviedb.org/3'
    endpoint_actor = '/movie/'
    endpoint_movie = '/discover/movie'
    data_processamento = datetime.utcnow().strftime('%Y/%m/%d')
    path = f'raw/tmdb/json/{data_processamento}/'
    http = urllib3.PoolManager()
    total_pages = 1
    current_pages = 1
    lista_atores = []

    while current_pages <= total_pages:
        response = http.request('GET', base_url + endpoint_movie + f'?api_key={api_key}&page={current_pages}')
        response_data = json.loads(response.data.decode('utf-8'))

        if 'total_pages' in response_data:
            total_pages = response_data['total_pages']
        else:
            print("Error: 'total_pages' key not found in API response.")
            break

        lista_ids = [val['id'] for val in response_data['results']]

        for movie_id in lista_ids:
            response_atores = http.request('GET', base_url + f'{endpoint_actor}{movie_id}/credits' + f'?api_key={api_key}&with_genres=828|14')
            lista_atores.append(json.loads(response_atores.data.decode('utf-8')))

        current_pages += 1

    df = pd.DataFrame(lista_atores)
    chunks = [df[i:i + 200].to_json(orient='records') for i in range(0, df.shape[0], 100)]


    s3 = boto3.client('s3')
    bucket_name = 'atividades3'

    for i, chunk in enumerate(chunks):
        file_key = f'{path}tmdb_data{i + 1}.json'
        s3.put_object(Body=chunk, Bucket=bucket_name, Key=file_key)

    return {
        'statusCode': 200,
        'body': 'dados gravados no S3 com sucesso'
    }
