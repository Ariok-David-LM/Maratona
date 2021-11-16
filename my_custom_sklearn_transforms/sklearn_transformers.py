from sklearn.base import BaseEstimator, TransformerMixin

class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()
        return data.drop(labels=self.columns, axis='columns')

class transformNum(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        opcionesLP = {'APPLIANCES': 0,'BUSINESS': 1,'CAR_NEW':2,'CAR_USED':3,'EDUCATION':4,'FURNITURE':5,'OTHER':6,'RADIO_TV':7,'REPAIRS':8,'RETRAINING':9,'VACATION':10}
        X['LOAN_PURPOSE']=X.LOAN_PURPOSE.map(opcionesLP)
        X['CHECKING_BALANCE']=X['CHECKING_BALANCE'].replace(['NO_CHECKING'],0)
        X['CHECKING_BALANCE'] = X['CHECKING_BALANCE'].astype(float, errors = 'raise')
        opcionesCH = {'ALL_CREDITS_PAID_BACK': 0,'CREDITS_PAID_TO_DATE': 1,'NO_CREDITS':2,'OUTSTANDING_CREDIT':3,'PRIOR_PAYMENTS_DELAYED':4}
        X['CREDIT_HISTORY']=X.CREDIT_HISTORY.map(opcionesCH)
        X['EXISTING_SAVINGS']=X['EXISTING_SAVINGS'].replace(['UNKNOWN'],0)
        X['EXISTING_SAVINGS'] = X['EXISTING_SAVINGS'].astype(float, errors = 'raise')
        opcionesP = {'UNKNOWN': 0,'CAR_OTHER': 1,'REAL_ESTATE':2,'SAVINGS_INSURANCE':3}
        X['PROPERTY']=X.PROPERTY.map(opcionesP)
        opcionesH = {'FREE': 0,'OWN': 1,'RENT':2}
        X['HOUSING']=X.HOUSING.map(opcionesH)
        return X
