# Customer Segmentation using K-Means Clustering

This project applies **K-Means clustering** to segment mall customers based on their **age** and **spending score**.  
The objective is to demonstrate unsupervised learning, cluster selection using the elbow method, and visual interpretation of customer groups.

---

## Objective

To identify distinct customer segments using K-Means clustering for exploratory analysis and basic customer profiling.

---

## Dataset

- **File:** `Mall_Customers.csv`
- **Source:** Mall customer demographic and spending data

### Features Used
- Age  
- Spending_Score  

The `Genre` column is numerically encoded but not used for clustering.

---

## Workflow

1. Load and inspect dataset
2. Encode categorical values
3. Select features for clustering
4. Apply the elbow method to determine optimal number of clusters
5. Train K-Means model
6. Visualize customer clusters and centroids

---

## Clustering Details

- **Algorithm:** K-Means
- **Initialization:** k-means++
- **Optimal Clusters:** 5 (chosen using elbow method)
- **Random State:** 42

---

## Visualization

### Elbow Method
Plots Within-Cluster Sum of Squares (WCSS) against the number of clusters to identify the optimal value of *k*.

### Cluster Visualization
Scatter plot of customer age vs spending score, colored by cluster, with cluster centroids highlighted.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
