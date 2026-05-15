from pathlib import Path


DATA_DIR = Path("data/artbench-10")
EXPECTED_CLASSES = [
    "art_nouveau",
    "baroque",
    "expressionism",
    "impressionism",
    "post_impressionism",
    "realism",
    "renaissance",
    "romanticism",
    "surrealism",
    "ukiyo_e",
]
EXPECTED_COUNTS = {
    "train": 50000,
    "test": 10000,
}
IMAGE_EXTENSIONS = {
    ".bmp",
    ".gif",
    ".jpeg",
    ".jpg",
    ".png",
    ".tif",
    ".tiff",
    ".webp",
}


def count_images(path: Path) -> int:
    return sum(
        1
        for file_path in path.rglob("*")
        if file_path.is_file() and file_path.suffix.lower() in IMAGE_EXTENSIONS
    )


def main() -> int:
    if not DATA_DIR.exists():
        print(f"Missing dataset directory: {DATA_DIR}")
        print("See DATASET.md for download and setup instructions.")
        return 1

    ok = True

    for split, expected_count in EXPECTED_COUNTS.items():
        split_dir = DATA_DIR / split
        if not split_dir.exists():
            print(f"Missing split directory: {split_dir}")
            ok = False
            continue

        actual_classes = sorted(
            child.name for child in split_dir.iterdir() if child.is_dir()
        )
        missing_classes = sorted(set(EXPECTED_CLASSES) - set(actual_classes))
        extra_classes = sorted(set(actual_classes) - set(EXPECTED_CLASSES))

        if missing_classes:
            print(f"{split}: missing classes: {', '.join(missing_classes)}")
            ok = False
        if extra_classes:
            print(f"{split}: unexpected classes: {', '.join(extra_classes)}")
            ok = False

        image_count = count_images(split_dir)
        status = "OK" if image_count == expected_count else "CHECK"
        print(f"{split}: {image_count:,} images ({status}; expected {expected_count:,})")

        if image_count != expected_count:
            ok = False

    if ok:
        print("Dataset layout looks ready for the notebooks.")
        return 0

    print("Dataset layout needs attention before rerunning the notebooks.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
