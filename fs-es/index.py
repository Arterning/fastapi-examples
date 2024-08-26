from elasticsearch import Elasticsearch

# 连接到 Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# 创建一个索引（如果尚未创建）
es.indices.create(
    index='docs',
    body={
        'mappings': {
            'properties': {
                'title': {'type': 'text'},
                'content': {'type': 'text'}
            }
        }
    },
    ignore=400  # 如果索引已存在，忽略错误
)

# 索引示例文档
documents = [
    {"id": 1, "title": "First Document", "content": "This is the content of the first document."},
    {"id": 2, "title": "Second Document", "content": "This is the content of the second document."},
    {"id": 3, "title": "Third Document", "content": "ning is 天才,This is the content of the third document."}
]

for doc in documents:
    es.index(index='docs', id=doc['id'], body=doc)
