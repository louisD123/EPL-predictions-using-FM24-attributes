import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def my_PCA(df, n_components=None):
    """
    Runs PCA on numeric columns of df.
    
    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset
    n_components : int or None
        Number of PCA components. If None -> keep all.

    Returns
    -------
    pca_df : pandas.DataFrame
        DataFrame containing the PCA components.
    model : sklearn.decomposition.PCA
        Fitted PCA model (so you can inspect variance, components, etc.)
    scaler : sklearn.preprocessing.StandardScaler
        Fitted scaler (useful for transforming future data)
    """
    # 1) Select only numeric columns
    numeric_df = df.select_dtypes(include='number')

    # 2) Scale features (VERY important for PCA)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(numeric_df)

    # 3) Fit PCA
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)

    # 4) Build output DataFrame
    columns = [f"PCA_{i+1}" for i in range(X_pca.shape[1])]
    pca_df = pd.DataFrame(X_pca, columns=columns, index=df.index)

    return pca_df, pca, scaler


