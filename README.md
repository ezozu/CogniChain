# CogniChain: Decentralized Federated Learning with Verifiable AI Provenance

CogniChain provides a secure and transparent platform for decentralized federated learning. By leveraging homomorphic encryption and blockchain technology, it allows for collaborative model training across disparate data sources without compromising data privacy. Furthermore, the system anchors verifiable AI model provenance information within an immutable directed acyclic graph (DAG), providing a robust audit trail for model development and deployment.

This project addresses the growing need for privacy-preserving and trustworthy AI. In traditional federated learning, while data remains on local devices, model updates are still transmitted and could potentially leak sensitive information. CogniChain mitigates this risk by employing homomorphic encryption, allowing model updates to be aggregated in an encrypted state. The resulting aggregated model is then decrypted and forms the basis for subsequent training rounds. Beyond privacy, CogniChain tackles the challenge of AI model provenance. By recording model training parameters, data source information, and cryptographic hashes within a blockchain-based DAG, the system creates an immutable record of the model's lineage, enabling verification and accountability.

CogniChain aims to democratize access to AI training while ensuring data privacy and model integrity. It can be used in various applications, including healthcare, finance, and supply chain management, where data privacy and regulatory compliance are paramount. The project provides a modular and extensible architecture, allowing developers to customize and integrate it into existing systems. By providing a verifiable record of model training, CogniChain helps to build trust in AI systems and promotes responsible AI development practices. The system's decentralized nature also enhances resilience and reduces the risk of single points of failure.

## Key Features

*   **Homomorphic Encryption for Privacy-Preserving Aggregation:** Implements a Paillier cryptosystem based homomorphic encryption scheme for secure aggregation of model updates from different participants. This ensures that individual data remains private throughout the federated learning process. The encryption key management is handled by a distributed key generation (DKG) protocol, adding another layer of security. Specifically, the system utilizes `phe.Paillier` library to perform homomorphic operations on model gradients.

*   **Blockchain-Based DAG for Model Provenance:** Utilizes a permissioned blockchain (e.g., Hyperledger Fabric) to create an immutable directed acyclic graph (DAG) representing the model's training history. Each node in the DAG contains metadata about the training round, including data source identifiers, model parameters, cryptographic hashes of model updates, and timestamps. The DAG structure allows for efficient traversal and verification of the model's lineage. Transactions include serialized JSON objects containing the relevant provenance data, hashed using SHA-256 for integrity verification.

*   **Decentralized Federated Learning Framework:** Provides a framework for coordinating federated learning across multiple participants. Participants can register with the network, download the latest model, train it on their local data, and submit encrypted model updates. The framework includes mechanisms for verifying the integrity of model updates and selecting a representative sample of participants for each training round.

*   **Verifiable Model Performance Metrics:** Integrates a mechanism for verifying the performance of the aggregated model on a held-out validation dataset. The validation process is performed by a trusted validator, and the results are recorded on the blockchain, providing an independent assessment of the model's accuracy and reliability. Statistical analysis is performed and recorded to ensure the quality of training and flag any inconsistencies.

*   **Secure Multi-Party Computation (MPC) Integration (Optional):** Supports integration with secure multi-party computation (MPC) techniques for further enhancing data privacy. MPC can be used to perform computations on encrypted data without revealing the underlying values. This feature is optional and can be enabled for applications that require the highest level of data security. We plan to integrate protocols like Shamir's Secret Sharing for improved security.

*   **Modular and Extensible Architecture:** Designed with a modular architecture that allows developers to easily customize and extend the system. The core components, such as the encryption scheme, blockchain integration, and federated learning algorithm, can be replaced or modified to meet specific application requirements. Python's object-oriented features are leveraged for building these modular components.

## Technology Stack

*   **Python:** The primary programming language used for implementing the federated learning framework, homomorphic encryption, and blockchain integration.
*   **phe (Paillier Homomorphic Encryption):** A Python library for performing Paillier homomorphic encryption operations. Used for encrypting model updates during the federated learning process.
*   **Hyperledger Fabric (or equivalent):** A permissioned blockchain platform used for creating the immutable DAG and storing model provenance information. Alternatives include Corda and Quorum.
*   **gRPC:** A high-performance, open-source universal RPC framework for client-server communication within the distributed system.
*   **Protocol Buffers:** A language-neutral, platform-neutral extensible mechanism for serializing structured data. Used for defining the data structures exchanged between participants.
*   **Docker:** Used for containerizing the application and its dependencies, making it easy to deploy and run in different environments.

## Installation

1.  Clone the repository:

    `git clone https://github.com/ezozu/CogniChain.git`

2.  Navigate to the project directory:

    `cd CogniChain`

3.  Create a virtual environment:

    `python3 -m venv venv`

4.  Activate the virtual environment:

    `source venv/bin/activate` (Linux/macOS)
    `venv\Scripts\activate` (Windows)

5.  Install the required dependencies:

    `pip install -r requirements.txt`

6.  Install Hyperledger Fabric (if you choose to use it as blockchain): Follow the official Hyperledger Fabric documentation for installation instructions. It usually involves installing Docker, Docker Compose, and the Fabric binaries.

7. Set up the Hyperledger Fabric network (if applicable). Follow the Hyperledger Fabric tutorials to deploy a basic network or adapt your existing network configuration.

## Configuration

CogniChain utilizes environment variables for configuration. Create a `.env` file in the project root directory and define the following variables:

*   `BLOCKCHAIN_URL`: The URL of the blockchain node.
*   `PHE_KEY_SIZE`: The size of the Paillier encryption key (e.g., 2048).
*   `FEDERATED_LEARNING_ROUNDS`: The number of federated learning rounds to perform.
*   `PARTICIPANT_ID`: A unique identifier for the participant.
*   `DATASET_PATH`: The path to the local dataset.
*   `MODEL_SAVE_PATH`: The path where the trained model will be saved.
* `MPC_ENABLED` (optional): Set to `true` to enable Secure Multi-Party Computation integration (defaults to false).

Example `.env` file:

BLOCKCHAIN_URL=grpc://localhost:7051
PHE_KEY_SIZE=2048
FEDERATED_LEARNING_ROUNDS=10
PARTICIPANT_ID=participant1
DATASET_PATH=./data/dataset.csv
MODEL_SAVE_PATH=./models/trained_model.pth
MPC_ENABLED=false

## Usage

First, start the blockchain network. For Hyperledger Fabric, this usually involves running the `docker-compose up` command.

Next, run the participant node:

python3 participant.py

The `participant.py` script will connect to the blockchain, download the latest model (if available), train it on the local dataset, encrypt the model updates, and submit them to the aggregator.

Aggregator node:

python3 aggregator.py

The `aggregator.py` script will receive encrypted model updates from participants, aggregate them using homomorphic encryption, decrypt the aggregated model, and update the global model. The updated model parameters, along with other relevant information, will be recorded on the blockchain.

API Documentation will be added in future releases.

## Contributing

We welcome contributions to CogniChain! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Implement your changes and write unit tests.
4.  Submit a pull request with a detailed description of your changes.
5.  Ensure that your code adheres to the project's coding style.
6.  All contributions must be licensed under the MIT License.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ezozu/CogniChain/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to thank the open-source community for their contributions to the libraries and tools used in this project.