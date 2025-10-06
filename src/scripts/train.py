from pathlib import Path
import yaml
from google1d.data import load_csv
from google1d.features import add_engagement_features

def main():
    cfg = yaml.safe_load(open("configs/config.yaml"))
    df = load_csv(cfg["paths"]["raw_file"])
    df = add_engagement_features(df)
    out = Path(cfg["paths"]["processed_dir"]).resolve() / "sample.parquet"
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out, index=False)
    print("Saved:", out)

if __name__ == "__main__":
    main()
