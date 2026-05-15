# Dataset Setup

The notebooks use ArtBench-10 and expect it at this exact local path:

```text
data/artbench-10
```

The `data/` directory is intentionally ignored by git because the image dataset is large. Anyone cloning the repository needs to download the dataset locally before rerunning the notebooks.

## Kaggle Download

1. Install and configure the Kaggle CLI:

   ```bash
   pip install kaggle
   ```

2. Create a Kaggle API token from your Kaggle account settings and place `kaggle.json` in the default Kaggle credentials location.

   On Linux or macOS:

   ```bash
   mkdir -p ~/.kaggle
   mv kaggle.json ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json
   ```

   On Windows, place it here:

   ```text
   C:\Users\<your-user>\.kaggle\kaggle.json
   ```

3. Download and unzip ArtBench-10:

   ```bash
   kaggle datasets download -d alexanderliao/artbench10 -p data --unzip
   ```

4. After extraction, make sure the folder that contains `train/` and `test/` is named:

   ```text
   data/artbench-10
   ```

   If Kaggle extracts the dataset under a slightly different folder name, rename or move that folder so the final layout matches the expected structure below.

## Expected Layout

```text
data/
  artbench-10/
    train/
      art_nouveau/
      baroque/
      expressionism/
      impressionism/
      post_impressionism/
      realism/
      renaissance/
      romanticism/
      surrealism/
      ukiyo_e/
    test/
      art_nouveau/
      baroque/
      expressionism/
      impressionism/
      post_impressionism/
      realism/
      renaissance/
      romanticism/
      surrealism/
      ukiyo_e/
```

Expected image counts:

| Split | Images |
|---|---:|
| `train` | 50,000 |
| `test` | 10,000 |

## Validate the Dataset

Run this command from the repository root:

```bash
python scripts/check_dataset.py
```

The script checks that `data/artbench-10` exists, verifies the expected class folders, and reports image counts for the train and test splits.

If the script fails, fix the folder structure before running the notebooks. All notebooks currently use the hard-coded path `data/artbench-10`.
