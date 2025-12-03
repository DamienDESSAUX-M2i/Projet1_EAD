import io
from pathlib import Path

import pandas as pd

rep_path: Path = Path(__file__).parent.resolve()

df_creditcard1: pd.DataFrame = pd.read_csv(rep_path.joinpath("data/creditcard1.csv"))
df_creditcard2: pd.DataFrame = pd.read_csv(rep_path.joinpath("data/creditcard2.csv"))
df_creditcard3: pd.DataFrame = pd.read_csv(rep_path.joinpath("data/creditcard3.csv"))
df_creditcard: pd.DataFrame = pd.concat(
    [df_creditcard1, df_creditcard2, df_creditcard3], axis=0
)

report_content: list[str] = []
report_content.append("# Analyse univariée")
report_content.append("Dataset : creditcard")

report_content.append("## Infos")
buffer = io.StringIO()
df_creditcard.info(buf=buffer)
report_content.append(buffer.getvalue())

report_creditcard_path: Path = rep_path.joinpath("report1_creditcard.md")
with open(report_creditcard_path, "wt", encoding="utf-8") as report:
    report.writelines("\n".join(report_content))
