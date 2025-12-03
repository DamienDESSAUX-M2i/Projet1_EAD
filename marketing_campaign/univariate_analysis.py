import io
from pathlib import Path

import pandas as pd

rep_path: Path = Path(__file__).parent.resolve()

df_marketing_campaign: pd.DataFrame = pd.read_csv(
    rep_path.joinpath("data/marketing_campaign.csv"), sep=";"
)

report_content: list[str] = []
report_content.append("# Analyse univariée")
report_content.append("Dataset : marketing_campaign")

report_content.append("## Infos")
buffer = io.StringIO()
df_marketing_campaign.info(buf=buffer)
report_content.append(buffer.getvalue())

report_marketing_campaign_path: Path = rep_path.joinpath(
    "report1_marketing_campaign.md"
)
with open(report_marketing_campaign_path, "wt", encoding="utf-8") as report:
    report.writelines("\n".join(report_content))
