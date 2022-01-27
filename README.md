# EpiGraphDB Drug Clustering Data
This repo contains scripts and data to extract a multipartite graph from EpiGraphDB to be embedded and clustered. ]

To recreate the data from raw:

1. From the base directory, run `scripts/process_raw.sh` to unzip and prepare raw data
2. Run `scripts/create_edgelist.py` to generate the edgelist 
3. (optional) To regenerate the schema image, install [graphviz](https://graphviz.org/) and run the following command `dot -Tpng scripts/schema.gv -o schema.png`