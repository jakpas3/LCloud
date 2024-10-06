# S3 Bucket Management CLI

## Description
This CLI tool provides a set of operations for managing AWS S3 buckets, including listing files, uploading files to a specified location within a bucket, filtering files based on a regex, and deleting files that match a regex pattern. It is designed for both interactive use and automation tasks.

## Features
- **List Files**: Retrieve all files under a specific prefix in an S3 bucket.
- **Upload Files**: Upload local files to a predefined location within an S3 bucket.
- **Filter Files**: List files that match a specific regex pattern.
- **Delete Files**: Remove files from an S3 bucket that match a regex pattern.

## Installation

### Prerequisites
- Python 3.x
- `boto3` library
- `python-dotenv` library (for managing environment variables securely)
- AWS account with access to S3

### Setup
1. **Clone the repository:**
   ```
   git clone https://github.com/jakpas3/LCloud.git
   cd lcloud
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Configure your environment variables:**
   - Create `.env` file.
   - Update the `.env` file with your AWS credentials:
     ```
     AWS_ACCESS_KEY_ID=your_access_key_id_here
     AWS_SECRET_ACCESS_KEY=your_secret_access_key_here
     ```

## Usage

### Running the CLI
To start the CLI, run the following command in your terminal:
```
python main.py
```

### Commands
- **List files**:
  ```
  Enter command: list <bucket_name> <prefix>
  ```
- **Upload a file**:
  ```
  Enter command: upload <file_path> <bucket_name> <prefix>
  ```
- **Filter files**:
  ```
  Enter command: filter <bucket_name> <prefix> <regex>
  ```
- **Delete files**:
  ```
  Enter command: delete <bucket_name> <prefix> <regex>
  ```
- **Exit the CLI**:
  ```
  Enter command: exit
  ```

### Interactive Mode
The CLI supports an interactive mode where commands can be entered one at a time. Simply start the CLI and follow the prompts.


