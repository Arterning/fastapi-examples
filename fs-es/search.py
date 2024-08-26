from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# 执行 Elasticsearch 搜索
response = es.search(
    index='docs',
    body={
        'query': {
            'match': {
                'content': "天才"
            }
        }
    }
)

print(response)

# 处理 Elasticsearch 搜索结果
hits = response['hits']['hits']
results = [
    {
        'id': hit['_id'],
        'title': hit['_source']['title'],
        'content': hit['_source']['content']
    }
    for hit in hits
]

print(results)