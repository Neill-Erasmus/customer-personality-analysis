# Customer Personality Analysis

This project employs the K-Means clustering algorithm for customer segmentation through personality analysis. Utilizing a dataset featuring diverse customer attributes, the K-Means algorithm facilitates the grouping of customers with analogous traits into distinct segments.

## K-Means Clustering Algorithm

K-Means is an unsupervised machine learning algorithm used for clustering and partitioning data into distinct groups. It aims to divide a dataset into K clusters, where each cluster is characterized by its centroid. The algorithm iteratively assigns data points to the nearest centroid and updates the centroids based on the mean of the points in each cluster. This process continues until convergence, optimizing the within-cluster sum of squares. K-Means is widely applied in various domains for pattern recognition, customer segmentation, and image compression.

## Dataset Overview

Customer Personality Analysis entails a comprehensive exploration of ideal customer profiles for a company. This examination enhances the comprehension of customers, empowering businesses to customize products to align with the unique needs, behaviors, and concerns of distinct customer types.

Through the process of Customer Personality Analysis, businesses can fine-tune their products according to the preferences of specific customer segments. Instead of expending resources on marketing a new product to the entire customer database, companies can pinpoint segments most likely to show interest in the product. Subsequently, targeted marketing efforts can be channeled towards these specific segments, optimizing resource utilization and heightening the probability of successful product adoption.

### Features

- Id: Unique identifier for each individual in the dataset.
- Year_Birth: The birth year of the individual.
- Education: The highest level of education attained by the individual.
- Marital_Status: The marital status of the individual.
- Income: The annual income of the individual.
- Kidhome: The number of young children in the household.
- Teenhome: The number of teenagers in the household.
- Dt_Customer: The date when the customer was first enrolled or became a part of the company's database.
- Recency: The number of days since the last purchase or interaction.
- MntWines: The amount spent on wines.
- MntFruits: The amount spent on fruits.
- MntMeatProducts: The amount spent on meat products.
- MntFishProducts: The amount spent on fish products.
- MntSweetProducts: The amount spent on sweet products.
- MntGoldProds: The amount spent on gold products.
- NumDealsPurchases: The number of purchases made with a discount or as part of a deal.
- NumWebPurchases: The number of purchases made through the company's website.
- NumCatalogPurchases: The number of purchases made through catalogs.
- NumStorePurchases: The number of purchases made in physical stores.
- NumWebVisitsMonth: The number of visits to the company's website in a month.
- AcceptedCmp3: Binary indicator (1 or 0) whether the individual accepted the third marketing campaign.
- AcceptedCmp4: Binary indicator (1 or 0) whether the individual accepted the fourth marketing campaign.
- AcceptedCmp5: Binary indicator (1 or 0) whether the individual accepted the fifth marketing campaign.
- AcceptedCmp1: Binary indicator (1 or 0) whether the individual accepted the first marketing campaign.
- AcceptedCmp2: Binary indicator (1 or 0) whether the individual accepted the second marketing campaign.
- Complain: Binary indicator (1 or 0) whether the individual has made a complaint.
- Z_CostContact: A constant cost associated with contacting a customer.
- Z_Revenue: A constant revenue associated with a successful campaign response.
- Response: Binary indicator (1 or 0) whether the individual responded to the marketing campaign.

[Dataset](https://www.kaggle.com/datasets/vishakhdapat/customer-segmentation-clustering)

## Building the Model

### Elbow Method for Optimal Cluster Selection

The Elbow Method is a technique to determine the optimal number of clusters (K) in a K-Means clustering algorithm. It involves running K-Means on the dataset for a range of K values and plotting the within-cluster sum of squares (WCSS) against the number of clusters. The "elbow" in the plot represents the point where adding more clusters doesn't significantly reduce WCSS. The optimal K is typically located at this elbow point, as it strikes a balance between minimizing intra-cluster variance and avoiding overfitting. The method helps in finding a suitable number of clusters for meaningful data segmentation without unnecessary complexity.

<div style="text-align:center;">
    <img src="https://github.com/Neill-Erasmus/customer-personality-analysis/assets/141222943/08e18633-ac51-4354-893e-39b4cc3474d5" alt="output">
</div>

Upon analyzing the Elbow Method graph, it reveals that the elbow point, a critical indicator for optimal cluster selection, is identified at 4 clusters. Although the clusters show a trend of converging towards 10, we opt for simplicity and interpretability, choosing 4 clusters as an optimal balance for effective segmentation in our model.

## Evaluating the Model

### Silhouette Score (0.54)

The silhouette score measures how well-defined the clusters are. A higher score indicates well-separated clusters. A score around 0.54 suggests reasonably distinct and appropriately clustered segments.

### Calinski-Harabasz Index (4966.12)

This index evaluates the ratio of between-cluster variance to within-cluster variance. A higher Calinski-Harabasz score indicates well-separated and dense clusters. With a score of 4966.12, the clusters demonstrate a good balance between cohesion and separation.

### Davies-Bouldin Index (0.41)

The Davies-Bouldin Index assesses the compactness and separability of clusters. A lower score indicates better clustering. A value of 0.41 suggests that the clusters are relatively compact and well-separated, contributing to effective customer segmentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
