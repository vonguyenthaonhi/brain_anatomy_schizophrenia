# Predict schizophrenia using brain anatomy
Predict schizophrenia from brain grey matter (GM). schizophrenia is associated with diffuse and complex pattern of brain atrophy. We will try to learn a predictor of the clinical status (patient with schizophrenia vs. healthy control) using GM measurements on the brain participants.

## Authors: VO Nguyen Thao Nhi, TARVERDIAN Mariam, LEBRETON Louis

## Dataset
There are 410 samples in the training set and 103 samples in the test set.

## Evaluation metrics
The main Evaluation metrics is ROC-AUC score

## Installation
1. Clone GitHub :

    ```bash
    git clone https://github.com/vonguyenthaonhi/brain_anatomy_schizophrenia.git
    cd brain_anatomy_schizophrenia
    ```

2. Create a virtual environment :

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment :

    - **Windows** :

        ```bash
        .\venv\Scripts\Activate
        ```

    - **Linux/Mac** :

        ```bash
        source venv/bin/activate
        ```

4. Install required packages

    ```bash
    pip install -r requirements.txt
    ```
    
## Auteurs

- [Vo Nguyen Thao Nhi](https://github.com/vonguyenthaonhi)
- [Tarvedian Mariam](https://github.com/Maro18287)
- [Lebreton Louis](https://github.com/louis-lebreton)
