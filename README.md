# Predicting the Winner of the Division 1 NCAA March Madness Tournament

## Overview
This project aims to predict the winner of the NCAA March Madness tournament using neural networks. The NCAA Men's Basketball Tournament, commonly referred to as March Madness, is a single-elimination tournament played each spring in the United States. The outcome of each game is highly unpredictable, making it an interesting challenge for predictive modeling.

## Dataset
The dataset used for this analysis contains historical data of NCAA basketball games. The “Final Data” consisted of preprocessing various datasets:

- **Ratings:** Power Ratings for every tournament team since 2016 from ABC News. ABC News bought out 538 and shut down their sports projections, so expect no new tournament power ratings for following seasons.
- **Team Resumes:** Statistics for every tournament team's resumes since 2008 from Bart Torvik. The ranks of every statistic are ranked out of all Division I College Basketball Teams. The NET RPI statistic uses the NET statistic from 2019 onwards and the RPI statistic from 2008 - 2018.
- **Tournament Matchups:** The matchups and final score of each team in the tournament. Each matchup is every two rows.
- **Team Results:** How well each team has performed in the tournament since 2008.
- **Heat Check:** Statistics for every tournament team since 2013 from Heat Check CBB.
- **Upset Seed:** The seed information of each upset. An upset is defined as Team A beating Team B with Team A's seed being 2 or more seeds lower than Team B. For example, a 7 seed beating a 5 seed is an upset and a 9 seed beating and 8 seed is not an upset.
- **Upset Count:** The upset count per year and round since 2008. An upset is defined as Team A beating Team B with Team A's seed being 2 or more seeds lower than Team B. For example, a 7 seed beating a 5 seed is an upset and a 9 seed beating and 8 seed is not an upset.

These datasets contained a variety of metrics that influenced the neural network model, such as various power metrics based on a teams division performance.

## Methodology
1. **Data Preprocessing:** Cleaned and preprocessed the datasets to handle missing values, normalize features, and engineer relevant features for modeling. (seen in Data Clean notebook)
2. **Feature Selection:** Selected relevant features using techniques such as correlation analysis, feature importance, and domain knowledge. (Seen in Models notebook)
3. **Model Building:** Implemented neural network models using frameworks such as TensorFlow. Experimented with various architectures. (Seen in Models notebook)
4. **Model Training:** Trained the neural network models on historical tournament data using techniques like hyperparameter tuning to optimize performance. (Seen in Models notebook)
5. **Model Evaluation:** Evaluated the models using metrics such as accuracy and loss values. (Seen in Models notebook)
6. **Prediction:** Used the trained models to predict the outcomes of future NCAA March Madness tournaments. (Seen in Models notebook)

## Results
The neural network models encountered some issues in predicting the winners of NCAA March Madness tournament games. Specifically, there was a mismatch in the number of features between the trained model and the 2024 input data, which led to an error. This indicates that the preprocessing steps applied to the training data and X_2024 might not be the same, or X_2024 might be missing some features present in the training data.

Despite this setback, it’s important to remember that due to the inherent unpredictability of the tournament, predictions will always contain some level of uncertainty. To improve the predictive performance, it’s crucial to ensure that the input data for prediction matches the structure of the training data. This includes applying the same preprocessing steps and ensuring the same number of features. Further refinement of the models and incorporation of additional features could also potentially enhance the accuracy of the predictions.

## Contributors
- Thomas Gauerke
- Rich Varos
- John Parente

## Sources

- The dataset used in this research was obtained from Kaggle: `https://www.kaggle.com/datasets/nishaanamin/march-madness-data?select=Upset+Count.csv`
- This project was assisted by GitHub Copilot and OpenAI's ChatGPT

## Acknowledgements
We would like to express our gratitude to the following Python libraries and their contributors, which have been instrumental in the success of this project:

- `pandas` and `numpy` for data manipulation and numerical operations.
- `sklearn.model_selection` and `sklearn.preprocessing` for functions like `train_test_split` and `RobustScaler` which helped in preparing the dataset for the model.
- `tensorflow.keras.models` and `tensorflow.keras.layers` for building the structure of the neural network models.
- `tensorflow` for providing the backend for Keras and other machine learning operations.
- `sklearn.preprocessing.LabelEncoder` and `OneHotEncoder` for encoding categorical variables.
- `kerastuner` for facilitating the hyperparameter tuning of the models.

We express our gratitude to the developers and maintainers of these libraries for their invaluable contributions to the open-source community.

