FROM eyeontext/ubuntu_20_04:2.0.2

# Prerequisites
RUN wget -O - https://debian.neo4j.com/neotechnology.gpg.key | apt-key add -
RUN echo 'deb https://debian.neo4j.com stable latest' | tee /etc/apt/sources.list.d/neo4j.list
RUN apt update
RUN apt install -y git

# Cloning our repository
# RUN mkdir -p /share/neo4jgithub/eot-wowool-samples
# RUN git clone https://github.com/wi18b088/eot-wowool-samples.git /share/neo4jgithub/eot-wowool-samples

# Get the files for hef-scraper
RUN mkdir -p /share/hef-scraper
RUN git clone https://github.com/wi18b088/HEFscraper.git /share/hef-scraper/HEFscraper

# Install python3 requirements
RUN pip install -r /share/hef-scraper/HEFscraper/requirements.txt
# RUN pip install -r /share/neo4jgithub/eot-wowool-samples/requirements.txt

# Install neo4j
RUN apt install -y neo4j
RUN neo4j-admin set-initial-password 12345
RUN sed -i 's/#dbms\.default_listen_address=0\.0\.0\.0/dbms\.default_listen_address=0\.0\.0\.0/' /etc/neo4j/neo4j.conf

# Create environment variables for our wrapper programmes
# Symlinks don't work, python working directories get messed up -> .bash_aliases
# scrape - /scraping repository?/ (scrape files from the defined sources with provided parameters)
RUN echo "alias scrape-springerlink=\"python3 /share/hef-scraper/HEFscraper/src/springerlink.py\"" >> /root/.bash_aliases
RUN echo "alias scrape-springerlink-pdf=\"python3 /share/hef-scraper/HEFscraper/src/pdf-downloader.py\"" >> /root/.bash_aliases
# UNIVERSAL SCRAPER

# createcyper - hef-graph-cypher.py (run wowool engine and create cypher output)
RUN echo "alias create-cyper=\"python3 /share/neo4jgithub/eot-wowool-samples/eot/wowool/samples/hef-graph-cypher.py\"" >> /root/.bash_aliases

# cyphertoneo - CypherToNeo4j.py (Feeds cypher into neo4j database)
RUN echo "alias cypher-to-neo4j=\"python3 /share/neo4jgithub/eot-wowool-samples/eot/wowool/samples/CypherToNeo4j.py\"" >> /root/.bash_aliases

# Create mount point for inout folder to be mounted when starting the docker
RUN mkdir /mnt/inout/

# Start neo4j when container starts
CMD neo4j start && bash