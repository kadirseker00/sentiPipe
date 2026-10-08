# sentiPipe — Multilingual sentiment analysis research code

Research notebooks accompanying **Abdulkadir Şeker's** article:

> **From Language Identification to Topic Modelling: A Fully Integrated Pipeline for Multilingual Aspect-Based Sentiment Analysis and Component-Level Insights**
>
> *Expert Systems*, 43(7), e70300 (2026).
>
> [Read the open-access article on Wiley](https://onlinelibrary.wiley.com/doi/full/10.1111/exsy.70300) · [DOI: 10.1111/exsy.70300](https://doi.org/10.1111/exsy.70300) · [Author ORCID](https://orcid.org/0000-0002-4552-2676)

The study evaluates **language identification, machine translation, sentiment classification and topic modelling** using M-ABSA and the Multilingual Amazon Reviews Corpus (MARC). This repository shares exploratory code for several of those components. Read the [research overview](https://kadirseker00.github.io/sentiPipe/) for the questions behind the study.

## Research questions

- **How does translation affect multilingual sentiment analysis?** The paper compares translation systems and sentiment classification on original reviews and English translations; see Sections 4.2–4.3.
- **How do LLMs compare with traditional language identification models?** Section 4.1 examines dataset-dependent differences on M-ABSA and MARC, including model combinations.
- **How can individual NLP pipeline components be evaluated?** The study examines language confusion, translation differences, sentiment errors and topic modelling under component-specific evaluation settings.

Consult the article for results, sampling, configurations and limitations. Dataset sizes do not imply that every record was evaluated in every experiment.

## Notebook guide

| Notebook | Purpose | Configured local input |
| --- | --- | --- |
| [genai_analysis.ipynb](notebooks/genai_analysis.ipynb) | Gemini-based translation, sentiment and topic annotation | `data/MARC_with_languages` or `data/MABSA_with_languages`; select one load cell |
| [topic_sentiment_models.ipynb](notebooks/topic_sentiment_models.ipynb) | VADER / Hugging Face sentiment comparisons; LDA, NMF, BERTopic and Top2Vec experiments | `data/MABSA_translate_sentiment_topic_all` |
| [translate_comparison_mabsa.ipynb](notebooks/translate_comparison_mabsa.ipynb) | Historical translation comparison using Marian / Helsinki, DeepL and M2M100 | `data/MARC_translate_sentiment_topic_all` |
| [translate_comparison_marc.ipynb](notebooks/translate_comparison_marc.ipynb) | Translation comparison including NLLB; similarity evaluation | `data/MARC_translate_sentiment_topic_all` |
| [other_analysis.ipynb](notebooks/other_analysis.ipynb) | Sentiment distributions, exploratory plots and label comparisons | `data/MARC_translate_sentiment_topic_all` |

**These notebooks require manual experiment selection and local intermediate datasets.** They are not a single automated reproduction of every experiment in the paper. In `genai_analysis`, loading the second dataset replaces the first; choose the load and save paths for your intended experiment. Both historical translation notebooks load MARC despite one filename containing `mabsa`. Review these paths before switching datasets.

Stored outputs and execution counts have been cleared. Data, model weights, `.env` credentials, result tables and figures are excluded from this repository. Publication edits also replace hardcoded credentials with environment variables, correct the duplicated `data/data` path and package-install typos, and place Gemini intermediate outputs under `data/`.

## Setup

Use Python 3.12 as a starting point; the original notebook environment was not version-locked. The dependency files list imported packages, rather than a tested reproduction environment.

```bash
git clone https://github.com/kadirseker00/sentiPipe.git
cd sentiPipe
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
# For LDA, BERTopic and Top2Vec sections:
python -m pip install -r requirements-topic.txt
cp .env.example .env
jupyter lab
```

Set only the keys for the services you use in your local `.env`:

| Variable | Used for |
| --- | --- |
| `GOOGLE_API_KEY` | Gemini annotation cells |
| `DEEPL_API_KEY` | DeepL translation cells |
| `HF_TOKEN` | Hugging Face inference cells |

The setup cell anchors relative paths to the repository root. Model identifiers, hosted inference URLs and service settings retain the historical experiments; check their current availability before running API cells. Translation models download substantial weights, and external API cells can incur service charges. Notebook sections can be installed and run separately.

### Prepare local data

Obtain source data from its creators:

- [M-ABSA repository](https://github.com/swaggy66/M-ABSA) and [dataset paper](https://arxiv.org/abs/2502.11824).
- [MARC dataset](https://www.kaggle.com/datasets/mexwell/amazon-reviews-multi), as linked in the article's Data Availability Statement.

The `*_with_languages` and `*_translate_sentiment_topic_all` directories are **local intermediate Hugging Face datasets**, not names of downloadable public dataset packages. Prepare the appropriate schema and save a dataset with `Dataset.save_to_disk(...)` before using `load_from_disk(...)`. Inspect the selected notebook cells for required columns, such as review text, language, sentiment, translation and topic annotations. The repository does not include the complete preprocessing needed to rebuild every intermediate from raw source data. Follow the dataset creators' terms and cite their work.

### Small offline example

To check the VADER baseline without datasets or API keys:

```bash
python -m pip install vaderSentiment
python examples/vader_demo.py
```

This example uses three synthetic **English** sentences. It demonstrates the baseline interface and does not reproduce the paper's multilingual experiments or results.

## Citation

If this research informs your work, please cite the published article. The root [CITATION.cff](CITATION.cff) sets the article as the preferred citation for GitHub's **Cite this repository** feature. [CITATION.bib](CITATION.bib) provides BibTeX.

```bibtex
@article{seker2026multilingual,
  author = {Şeker, Abdulkadir},
  title = {From Language Identification to Topic Modelling: A Fully Integrated Pipeline for Multilingual Aspect-Based Sentiment Analysis and Component-Level Insights},
  journal = {Expert Systems},
  year = {2026},
  volume = {43},
  number = {7},
  pages = {e70300},
  doi = {10.1111/exsy.70300},
  url = {https://doi.org/10.1111/exsy.70300}
}
```

## Attribution

`genai_analysis.ipynb` retains its original Google LLC copyright and Apache-2.0 notice. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [the license text](licenses/Apache-2.0.txt). No additional repository-wide license is assigned here.
