from datasets import load_dataset
from datasets import concatenate_datasets


def load_raw_data():

    dataset = load_dataset(
        "onyx-dot-app/EnterpriseRAG-Bench",
        "documents",
        split="test"
    )

    sources = {
        "slack": 2,
        "gmail": 2,
        "confluence": 2,
        "jira": 2,
        "github": 2,
        "fireflies": 2
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