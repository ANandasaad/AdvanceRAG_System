from datasets import load_dataset
from datasets import concatenate_datasets


def load_raw_data():

    dataset = load_dataset(
        "onyx-dot-app/EnterpriseRAG-Bench",
        "documents",
        split="test"
    )

    sources = {
        "slack": 500,
        "gmail": 500,
        "confluence": 500,
        "jira": 1000,
        "github": 1000,
        "fireflies": 500
    }

    subsets = []

    for source, limit in sources.items():

        filtered = dataset.filter(
            lambda x: x["source_type"] == source
        )

        filtered = filtered.select(
            range(min(limit, len(filtered)))
        )

        subsets.append(filtered)

    final_dataset = concatenate_datasets(
        subsets
    )

    return final_dataset