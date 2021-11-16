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
        data = X.copy()
        opcionesLP = {'APPLIANCES': 6,'BUSINESS': 1,'CAR_NEW':2,'CAR_USED':3,'EDUCATION':4,'FURNITURE':5,'OTHER':0,'RADIO_TV':7,'REPAIRS':8,'RETRAINING':9,'VACATION':10}
        data['LOAN_PURPOSE']=data['LOAN_PURPOSE'].replace(opcionesLP)
        data['LOAN_PURPOSE']=data['LOAN_PURPOSE'].astype(float, errors = 'raise')
        data['CHECKING_BALANCE']=data['CHECKING_BALANCE'].replace(['NO_CHECKING'],0)
        data['CHECKING_BALANCE']=data['CHECKING_BALANCE'].astype(float, errors = 'raise')
        opcionesCH = {'ALL_CREDITS_PAID_BACK': 2,'CREDITS_PAID_TO_DATE': 1,'NO_CREDITS':0,'OUTSTANDING_CREDIT':3,'PRIOR_PAYMENTS_DELAYED':4}
        data['CREDIT_HISTORY']=data['CREDIT_HISTORY'].replace(opcionesCH)
        data['CREDIT_HISTORY']=data['CREDIT_HISTORY'].astype(float, errors = 'raise')
        data['EXISTING_SAVINGS']=data['EXISTING_SAVINGS'].replace(['UNKNOWN'],0)
        data['EXISTING_SAVINGS']=data['EXISTING_SAVINGS'].astype(float, errors = 'raise')
        return data
