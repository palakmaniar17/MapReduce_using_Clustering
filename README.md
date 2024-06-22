# MapReduce_using_Clustering
The following is the application of Map Reduce using KMeans Clustering in Hadoop using the fundamentals of Map and Reduce with the help of AWS. 

This repository contains the project which includes implementing k-means clustering and a BloomFilter-based 2-way map-side join using Python and Hadoop.

## Project Structure

- **data/**: Contains the data files used in the project.
- **src/**: Source code for generating data, k-means clustering, and BloomFilter join.
- **results/**: Output files after processing.
- **docs/**: Documentation and screenshots.
- **README.md**: Project overview and instructions.
- **LICENSE**: License information for the project.
- **.gitignore**: Specifies files and directories to be ignored by Git.

## Getting Started

### Prerequisites

- Python 3.x
- Hadoop cluster setup (optional for single-node execution)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Install required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Project

#### 1. K-means Clustering

1. Generate initial centers and data:
    ```sh
    python src/gen_centers.py
    python src/gen_kmeans_data.py
    ```

2. Run k-means clustering (4 iterations):
    ```sh
    cat data/kmeans_data.csv | python3 src/mapper_kmeans.py | sort -n | python3 src/reducer_kmeans.py > data/centers.txt
    # Repeat the process for 4 iterations, updating centers.txt each time
    ```

#### 2. BloomFilter-based 2-way Join

1. Download the required tables:
    ```sh
    wget http://cdmgcsarprd01.dpu.depaul.edu/CSC555/SSBM1/dwdate.tbl
    wget http://cdmgcsarprd01.dpu.depaul.edu/CSC555/SSBM1/lineorder.tbl
    ```

2. Run the map-side join:
    ```sh
    cat dwdate.tbl | python3 src/BFmapper.py | sort -n | python3 src/BRreducer.py
    ```

## Results

- The final centers after 4 iterations are in `results/centers.txt`.
- The join results are in `results/output_bloom_joined.txt`.

## Screenshots

Screenshots of the Hadoop cluster running the tasks are available in the `docs/screenshots/` directory.

## Contributing

Please read `CONTRIBUTING.md` for details on the code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
