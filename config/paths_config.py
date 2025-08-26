import os

###################### DATA INGESTION ############################3

RAW_DIR = "C:/Users/tegbe/Downloads/MLOps Project/Anime_Reccomendation_Project/Code/artifacts/raw"
CONFIG_PATH = "C:/Users/tegbe/Downloads/MLOps Project/Anime_Reccomendation_Project/Code/config/config.yaml"


######################## DATA PROCESSING ##########################

PROCESSED_DIR = "C:/Users/tegbe/Downloads/MLOps Project/Anime_Reccomendation_Project/Code/artifacts/processed"
ANIMELIST_CSV = "C:/Users/tegbe/Downloads/MLOps Project/Anime_Reccomendation_Project/Code/artifacts/raw/animelist.csv"
ANIME_CSV = "C:/Users/tegbe/Downloads/MLOps Project/Anime_Reccomendation_Project/Code/artifacts/raw/anime.csv"
ANIMESYNOPSIS_CSV = "C:/Users/tegbe/Downloads/MLOps Project/Anime_Reccomendation_Project/Code/artifacts/raw/anime_with_synopsis.csv"

X_TRAIN_ARRAY = os.path.join(PROCESSED_DIR,"X_train_array.pkl")
X_TEST_ARRAY = os.path.join(PROCESSED_DIR,"X_test_array.pkl")
Y_TRAIN = os.path.join(PROCESSED_DIR,"y_train.pkl")
Y_TEST = os.path.join(PROCESSED_DIR,"y_test.pkl")

RATING_DF = os.path.join(PROCESSED_DIR,"rating_df.csv")
DF = os.path.join(PROCESSED_DIR,"anime_df.csv")
SYNOPSIS_DF = os.path.join(PROCESSED_DIR,"synopsis_df.csv")

USER2USER_ENCODED = "C:/Users/tegbe/Downloads/MLOps Project/Anime_Reccomendation_Project/Code/artifacts/processed/user2user_encoded.pkl"
USER2USER_DECODED = "C:/Users/tegbe/Downloads/MLOps Project/Anime_Reccomendation_Project/Code/artifacts/processed/user2user_decoded.pkl"

ANIME2ANIME_ENCODED = "C:/Users/tegbe/Downloads/MLOps Project/Anime_Reccomendation_Project/Code/artifacts/processed/anim2anime_encoded.pkl"
ANIME2ANIME_DECODED = "C:/Users/tegbe/Downloads/MLOps Project/Anime_Reccomendation_Project/Code/artifacts/processed/anim2anime_decoded.pkl"


###################### MODEL TRAINING #######################

MODEL_DIR = "C:/Users/tegbe/Downloads/MLOps Project/Anime_Reccomendation_Project/Code/artifacts/model"
WEIGHTS_DIR = "C:/Users/tegbe/Downloads/MLOps Project/Anime_Reccomendation_Project/Code/artifacts/weights"
MODEL_PATH = os.path.join(MODEL_DIR,"model.h5")
ANIME_WEIGHTS_PATH = os.path.join(WEIGHTS_DIR,"anime_weights.pkl")
USER_WEIGHTS_PATH = os.path.join(WEIGHTS_DIR,"user_weights.pkl")
CHECKPOINT_FILE_PATH = "C:/Users/tegbe/Downloads/MLOps Project/Anime_Reccomendation_Project/Code/artifacts/model_checkpoint/weights.weights.h5"