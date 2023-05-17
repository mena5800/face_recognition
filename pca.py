import numpy as np

class PCA:
    """
    Principal Component Analysis (PCA)
    """
    
    def __init__(self, n_components=None):
        self.n_components = n_components
        self.components_ = None
        self.mean_ = None
        self.explained_variance_ratio_ = None
    
    def fit(self, X):
        """
        Fit the PCA model to the data.
        
        Args:
        X: numpy array of shape (n_samples, n_features)
        """
        # Subtract the mean of each feature
        self.mean_ = np.mean(X, axis=0)
        X = X - self.mean_
        
        # Calculate the covariance matrix
        cov = np.cov(X, rowvar=False)
        
        # Calculate the top n_components eigenvectors using the power iteration method
        eigenvalues, eigenvectors = np.linalg.eigh(cov)
        sort_indices = np.argsort(eigenvalues)[::-1]
        eigenvectors = eigenvectors[:,sort_indices]
        if self.n_components is not None:
            self.components_ = eigenvectors[:,:self.n_components]
            self.explained_variance_ratio_ = eigenvalues[sort_indices][:self.n_components] / np.sum(eigenvalues)
        else:
            self.components_ = eigenvectors
            self.explained_variance_ratio_ = eigenvalues[sort_indices] / np.sum(eigenvalues)
    
    def transform(self, X):
        """
        Transform the data using the fitted PCA model.
        
        Args:
        X: numpy array of shape (n_samples, n_features)
        
        Returns:
        X_pca: numpy array of shape (n_samples, n_components)
        """
        # Subtract the mean of each feature
        X = X - self.mean_
        
        # Project the data onto the top n_components eigenvectors
        if self.n_components is not None:
            components = self.components_
        else:
            components = np.identity(X.shape[1])
        X_pca = np.dot(X, components)
        
        return X_pca