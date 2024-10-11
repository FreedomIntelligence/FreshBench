git clone https://github.com/Marker-Inc-Korea/RAGchain.git



cd /mntnfs/med_data5/zhuchenghao/Freshbench_release/rag/RAGchain/

pip install -e .


set env variable
<!-- GOOGLE_CSE_ID -->
bash
```
export  GOOGLE_CSE_ID=3117be5b9c51141d5
export  GOOGLE_API_KEY=AIzaSyAVn1rsapqbT7kyz3QUpmgizJIdH4UOJbM
export  LINKER_TYPE=json
export  JSON_LINKER_PATH=./json
pip install -U langchain-community -i https://pypi.doubanio.com/simple

```

<!-- pip install langchain -i https://pypi.douban.com/simple -->



<!-- pip install langsmith && conda install langchain -c conda-forge  -->
pip


pip install langchain -i https://pypi.doubanio.com/simple
有潜在冲突，但是不影响 在fastllm
pip install -U langchain_community -i https://pypi.doubanio.com/simple


python /mntnfs/med_data5/zhuchenghao/Freshbench_release/rag/RAGchain/tests/RAGchain/pipeline/test_search_pipeline.py

---

from datetime import datetime

query = "What is the capital of Korea?"
retrieval = BM25Retrieval('/path/to/your/bm25.pkl')
passages = retrieval.retrieve_with_filter(query, content_datetime_range=[
    (datetime(2021, 1, 1), datetime(2021, 1, 31)),
]) # only retrieve passages in January 2021
