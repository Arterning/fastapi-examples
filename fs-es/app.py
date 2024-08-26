from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional
from elasticsearch import Elasticsearch

app = FastAPI()
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

class SearchResponse(BaseModel):
    id: int
    title: str
    content: str

@app.get("/search", response_model=List[SearchResponse])
async def search(
    query: str = Query(..., description="Search query")
):
    # 执行 Elasticsearch 搜索
    response = es.search(
        index='docs',
        body={
            'query': {
                'match': {
                    'content': query
                }
            }
        }
    )
    
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
    
    return results
