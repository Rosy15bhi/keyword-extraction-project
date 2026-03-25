from pathlib import Path
import nltk
from rake_nltk import Rake


def ensure_nltk_resources() -> None:
    """Download required NLTK resources if missing."""
    try:
        nltk.data.find("corpora/stopwords")
    except LookupError:
        nltk.download("stopwords")

    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")


def extract_keywords(input_file: Path, output_file: Path) -> None:
    """Read text from file, extract keywords with RAKE, and save results."""
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    text = input_file.read_text(encoding="utf-8").strip()

    if not text:
        raise ValueError("Input text file is empty.")

    rake = Rake()
    rake.extract_keywords_from_text(text)

    ranked_phrases = rake.get_ranked_phrases_with_scores()

    output_lines = ["Extracted keywords:\n"]

    for score, phrase in ranked_phrases:
        output_lines.append(f"{score:.2f} - {phrase}")

    output_text = "\n".join(output_lines)
    output_file.write_text(output_text, encoding="utf-8")

    print("\nKeywords extracted successfully:\n")
    print(output_text)
    print(f"\nResults saved in: {output_file}")


def main() -> None:
    ensure_nltk_resources()

    project_root = Path(__file__).resolve().parent.parent
    input_file = project_root / "data" / "sample_text.txt"
    output_file = project_root / "outputs" / "keywords_output.txt"

    extract_keywords(input_file, output_file)

if __name__ == "__main__":
    main()
    
