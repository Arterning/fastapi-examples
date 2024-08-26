docker run -d \
	--name elasticsearch \
    -e "ES_JAVA_OPTS=-Xms512m -Xmx512m" \
    -e "discovery.type=single-node" \
    -p 9200:9200 \
    -p 9300:9300 \
elasticsearch:7.12.1