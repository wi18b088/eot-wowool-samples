FROM eyeontext/ubuntu_20_04:2.0.2

# Prerequisites
RUN wget -O - https://debian.neo4j.com/neotechnology.gpg.key | apt-key add -
RUN echo 'deb https://debian.neo4j.com stable latest' | tee /etc/apt/sources.list.d/neo4j.list
RUN apt update
RUN apt install -y git

# Cloning our repository
RUN mkdir -p /share/neo4jgithub/eot-wowool-samples
RUN git clone https://github.com/wi18b088/eot-wowool-samples.git /share/neo4jgithub/eot-wowool-samples

# Install neo4j
RUN apt install -y neo4j
RUN neo4j-admin set-initial-password 12345
RUN sed -i 's/#dbms\.default_listen_address=0\.0\.0\.0/dbms\.default_listen_address=0\.0\.0\.0/' /etc/neo4j/neo4j.conf

# Create environment variables for our wrapper programmes
# Symlinks to /usr/local/bin; python3 shabang
RUN ln /share/neo4jgithub/eot-wowool-samples/CypherToNeo4j.py cypertoneo
RUN chmod +x /share/neo4jgithub/eot-wowool-samples/CypherToNeo4j.py

# Start neo4j when container starts
# startup_fix.sh still relevant?
# CMD ["neo4j","start"]
CMD neo4j start && bash