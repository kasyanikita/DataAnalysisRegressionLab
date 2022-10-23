from sklearn.utils.fixes import sklearn
import src.config as cfg
from src.utils import get_params
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from catboost import CatBoostRegressor
from sklearn.ensemble import StackingRegressor, RandomForestRegressor

real_pipe = Pipeline([
    ('imputer', SimpleImputer()),
    ('scaler', StandardScaler())
    ]
)

cat_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='NA')),
    ('ohe', OneHotEncoder(handle_unknown='ignore', sparse=False))
    ]
)

preprocess_pipe = ColumnTransformer(transformers=[
    ('real_cols', real_pipe, cfg.REAL_COLS),
    ('cat_cols', cat_pipe, cfg.CAT_COLS),
    ('ohe_cols', 'passthrough', cfg.NEW_OHE)
    ]
)

base_model = LinearRegression()

sklearn_model = Pipeline([
    ('preprocess', preprocess_pipe),
    ('model', base_model)
    ]
)

params = get_params()

catboost = CatBoostRegressor(iterations=50, cat_features=cfg.CAT_COLS, random_seed=cfg.RS)

estimators = [('lr', sklearn_model ), ('cat', catboost)]

stack = StackingRegressor(estimators, final_estimator=RandomForestRegressor(n_estimators=params['n_estimators'], random_state=42))
