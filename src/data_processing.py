from pathlib import Path
import pandas as pd


def load_marketing_data(data_path):
    """
    读取营销 A/B Test 原始数据，并统一字段名格式。
    
    Parameters
    ----------
    data_path : str or Path
        原始数据文件路径。
    
    Returns
    -------
    pd.DataFrame
        清洗好字段名后的 DataFrame。
    """
    data_path = Path(data_path)

    if not data_path.exists():
        raise FileNotFoundError(f"数据文件不存在: {data_path}")

    df = pd.read_csv(data_path)

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df